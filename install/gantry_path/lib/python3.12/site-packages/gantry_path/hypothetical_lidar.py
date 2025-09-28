import rclpy
from rclpy.node import Node
from gantry_lidar_interfaces.srv import Capture, DownloadName, BagStart, DeleteName
from std_srvs.srv import Trigger
from std_msgs.msg import Bool
import subprocess
from pathlib import Path
import json
import time



class LidarScan(Node):
    def __init__(self):
        super().__init__('lidar_scan')

        #service client setup
        self.gant_capture = self.create_client(Capture, "gantry_capture_service/capture")
        self.gant_download = self.create_client(DownloadName, "gantry_capture_service/download/name")
        self.gant_delete = self.create_client(DeleteName, "gantry_capture_service/delete/name")

        # wait for core services to be available
        while not self.gant_capture.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for capture service...")
        while not self.gant_download.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for download service...")
        while not self.gant_delete.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for delete service...")

        #set up service client for bag nodes
        self.start_bag_serv = []
        self.stop_bag_serv = []
        self.discover_baggers()

        self.path = str(Path.home() / "rosbags" / "912-test")
        Path(self.path).mkdir(parents=True, exist_ok=True)
        # default name prefix for capture (avoid missing attribute)
        self.test_name = time.strftime("%Y%m%d_%H%M%S")

        # one-shot guard so we run capture only once per node lifetime
        self._has_run = False

        # subscribe for trigger
        self.trigger_sub = self.create_subscription(
            Bool,
            'start_lidar',
            self.lidar_trigger_cb,
            10,
        )




    def discover_baggers(self):
        
        all_nodes = self.get_node_names()
        print(all_nodes)
        for name in all_nodes:
            if "bag" in name:
                start_bag = self.create_client(BagStart, f"{name}/start")
                self.get_logger().info(f"service name:{name}/start")
                stop_bag = self.create_client(Trigger, f"{name}/stop")
                self.get_logger().info(f"service name:{name}/stop")
                if not start_bag.wait_for_service(timeout_sec=2.0):
                    self.get_logger().error(f"{name} start service not connected")
                    continue

                if not stop_bag.wait_for_service(timeout_sec=2.0):
                    self.get_logger().error(f"{name} stop service not connected")
                    continue

                self.start_bag_serv.append(start_bag)
                self.stop_bag_serv.append(stop_bag)

                self.get_logger().info(f"connected to bag services on {name}")


    def start_bags(self):
        request = BagStart.Request()
        request.uri = self.path
        for client in self.start_bag_serv:
            client.call_async(request)
            self.get_logger().info(f"started bagger")
        return
    
    def stop_bags(self):
        for client in self.stop_bag_serv:
            client.call_async(Trigger.Request())
            self.get_logger().info(f"stopped bagger")

    def start_lidar(self):
        capture_request = Capture.Request()
        capture_request.outname = self.test_name + "_lidar"
        capture_request.sensors = ["l515_center", "l515_west", "l515_east"]
        capture_request.duration = 10.0
        future_cap = self.gant_capture.call_async(capture_request)
        return future_cap

    def lidar_trigger_cb(self, msg: Bool):
        # If True and not already executed, run once
        if not msg.data:
            self.get_logger().info("Start lidar flag is False; ignoring.")
            return
        if self._has_run:
            self.get_logger().info("Lidar run already completed; ignoring trigger.")
            return

        self._has_run = True
        self.get_logger().info("Received True trigger; starting one-shot lidar capture.")

        # Start baggers
        self.start_bags()

        # Start lidar capture and chain completion callbacks
        future_cap = self.start_lidar()

        def on_capture_done(fut):
            try:
                response_cap = fut.result()
            except Exception as exc:  # noqa: BLE001
                self.get_logger().error(f"Capture failed: {exc}")
                self.stop_bags()
                return

            lidar_cap_data = json.loads(response_cap.outdata)
            downloadname_request = DownloadName.Request()
            downloadname_request.name = lidar_cap_data.get("outname", "")
            self.get_logger().info(f"Lidar bag name: {downloadname_request.name}")

            future_down = self.gant_download.call_async(downloadname_request)

            def on_download_done(fut_down):
                try:
                    downloadname_response = fut_down.result()
                except Exception as exc:  # noqa: BLE001
                    self.get_logger().error(f"Download lookup failed: {exc}")
                    self.stop_bags()
                    return

                downloadname_response_dict = json.loads(downloadname_response.outdata)
                cap_url = downloadname_response_dict.get("url", "")
                if not cap_url:
                    self.get_logger().error("No download URL returned; stopping bags.")
                    self.stop_bags()
                    return

                self.get_logger().info(f"Lidar bag download url: {cap_url}")
                subprocess.Popen(["wget", "-r", "-P", f"{self.path}", f"{cap_url}"])

                # give downloader some time, then stop bags
                def stop_after_download():
                    self.stop_bags()
                    self.get_logger().info("Trial complete.")
                    self.get_logger().info(f"Bag saved to {self.path}")
                    # make timer one-shot by cancelling after first call
                    try:
                        if hasattr(self, '_stop_timer') and self._stop_timer is not None:
                            self._stop_timer.cancel()
                            self._stop_timer = None
                    except Exception:
                        pass
                    # Optionally, shutdown after run:
                    # rclpy.shutdown()

                # create one-shot timer (10s) to stop bags
                self._stop_timer = self.create_timer(10.0, stop_after_download)

            future_down.add_done_callback(on_download_done)

        future_cap.add_done_callback(on_capture_done)
    

def main(args=None):
    rclpy.init(args=args)

    node = LidarScan()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
