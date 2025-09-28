import rclpy
from rclpy.node import Node
from gantry_lidar_interfaces.srv import Capture, DownloadName, BagStart, DeleteName
from std_srvs.srv import Trigger
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


        #start bags
        self.start_bags()

        #send lidar service command [todo]
        future_cap = self.start_lidar()

        #wait until lidar scan done
        rclpy.spin_until_future_complete(self, future=future_cap)


        response_cap = future_cap.result()
        lidar_cap_data = json.loads(response_cap.outdata)

        downloadname_request = DownloadName.Request()
        downloadname_request.name = lidar_cap_data["outname"]

        self.get_logger().info(f"Lidar bag 1 name: {downloadname_request.name}")

        future_down = self.gant_download.call_async(downloadname_request)
        rclpy.spin_until_future_complete(self, future=future_down)
        downloadname_response = future_down.result()

        self.get_logger().info("got call")

        downloadname_response_dict = json.loads(downloadname_response.outdata)

        cap_1_url = downloadname_response_dict["url"]

        self.get_logger().info(f"Lidar bag 1 download url: {cap_1_url}")


        subprocess.Popen(["wget", "-r", "-P", f"{self.path}", f"{cap_1_url}"])

        time.sleep(10)

        self.stop_bags()
        self.get_logger().info("trial complete.")
        self.get_logger().info(f"bag saved to {self.path}")




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
    

def main(args=None):
    rclpy.init(args=args)

    try:
        LidarScan()
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()
    