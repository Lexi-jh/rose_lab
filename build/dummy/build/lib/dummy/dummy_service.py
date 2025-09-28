import rclpy
from rclpy import Node
from std_srvs.srv import Trigger
from sensor_msgs.msg import PointCloud2, PointField

from datetime import datetime
import subprocess
import signal
import shutil
from pathlib import Path
import json
import time


from gantry_lidar_interfaces.srv import Capture, DownloadName, DownloadTimeRange, DeleteName, DeleteTimeRange


#file stuff and opening remote server function
DATA_DIR = Path.home() / "RoSE_Bags"
TIME_STR = "%Y-%m-%dT%H-%M-%S"

def start_http_server():
    subprocess.Popen([
        "python3", "-m", "http.server", "8000",
        "--directory", str(DATA_DIR),
        "--bind", "0.0.0.0"
    ])

def parse_time(timestr):
        return datetime.strptime(timestr, TIME_STR)

class DummyService(Node):
    def __init__(self):
        super().__init__('gantry_capture_service')

        # Info
        self.create_service(Trigger, 'gantry_capture_service/info', self.info_callback)
        
        # Capture sensor data
        self.create_service(Capture, 'gantry_capture_service/capture', self.capture_callback)

        # Download
        self.create_service(DownloadName, 'gantry_capture_service/download/name', self.download_name_callback)
        self.create_service(DownloadTimeRange, 'gantry_capture_service/download/timeRange', self.download_time_range_callback)

        # Delete
        self.create_service(DeleteName, 'gantry_capture_service/delete/name', self.delete_name_callback)
        self.create_service(DeleteTimeRange, 'gantry_capture_service/delete/timeRange', self.delete_time_range_callback)

        #create fake lidar subscriber
        self.lidar_sub = self.create_subscription(PointCloud2, 'points', self.fake_data_callback, 10)
        
        # Start HTTP server
        start_http_server()

        #variables
        self.lidar_data = None

        self.get_logger().info("Gantry capture service running")

    def fake_data_callback(self, msg):
        self.lidar_data = msg

    def info_callback(self, request, response):
        response.success = True
        response.message = "idk what to put here"
        return response

    def capture_callback(self, request, response):
        """
        Capture a bag for a set time and saves it locally, zipped
        Service Arguments
        - duration: how long to capture for
        - sensors: list of str names of sensors
        - outname: name of bag to save. bag will be saved as "outname_timestamp"
        """
        self.get_logger().info(str(DATA_DIR))
        try:
            #self.get_logger().info(request)
            #req_data = json.loads(request.data)
            duration = request.duration #req_data.get("duration", 10.0)
            sensors = request.sensors #req_data.get("sensors", [])
            outname = request.outname #req_data.get("outname", "")

            # Match directories like: "outname_*"
            #matches = list(DATA_DIR.glob(f"{outname}_*"))
            
            # If file exists 
            # if matches:
            #     self.get_logger().info(f"Filename already exists: {self.outname}")
            #     response.outdata = json.dumps({"status": "ERROR", "reason": "filename already exists"})
            #     return response
            
            # Format filename
            timestamp = datetime.now().strftime(TIME_STR)
            self.filename = f"{outname}_{timestamp}"

            # Set Topics
            topics = []
            topics.append("points")
                    

            # Capture Bag
            bag_path = (DATA_DIR / self.filename).resolve()
            self.get_logger().info(f"Capturing data: {duration}s from {topics}, output: {str(bag_path)}")
            cmd = ['ros2', 'bag', 'record', '-o', str(bag_path)] + topics
            self.record_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.get_logger().info(f"Started recording bag: {self.filename}")

            time.sleep(duration) # Delay

            # End capture
            self.record_process.send_signal(signal.SIGINT)
            self.record_process.wait()
            self.record_process = None

            self.get_logger().info(f"Stopped recording bag: {self.filename}")
           
            # Zip bag
            #self.get_logger().info(f"Making .zip archive: {self.filename}.zip")
            #shutil.make_archive(self.filename, 'zip', DATA_DIR / self.filename)

            # Delete original folder
            #self.get_logger().info(f"Deleting original: {self.filename}")
            #shutil.rmtree(DATA_DIR / self.filename)

            response.outdata = json.dumps({
                "status": "ACK",
                "duration": duration,
                "sensors": sensors,
                "outname": self.filename
            })

        except Exception as e:
            response.outdata = json.dumps({"status": "ERROR", "reason": str(e)})
        return response
    
    def download_name_callback(self, request, response):
        """
        Download bags by name. All bags with matching name will be downloaded (although there should only be one)
        """
        try:
            #data = json.loads(request.data)
            outname = request.name

            # Get matches (Should only have one)
            matches = sorted(DATA_DIR.glob(f"{outname}"), reverse=True)
            if not matches:
                self.get_logger().info(f"Download name request failed, file not found.")
                response.outdata = json.dumps({"success": False, "error": "Not found"})
                return response

            # Figure out what the http path to the zip is
            folder = matches[0].name
            ip = "0.0.0.0"
            url = f"http://{ip}:8000/{folder}"

            self.get_logger().info(f"Download name request with: {url}")

            # Return the zip path for wget by client
            response.outdata = json.dumps({
                "success": True,
                "url": url
            })

        except Exception as e:
            response.outdata = json.dumps({"success": False, "error": str(e)})
        return response

    def delete_name_callback(self, request, response):
        """
        Delete bags by name. All bags with matching name will be deleted (although there should only be one)
        """
        try:
            #data = json.loads(request.data)
            outname = request.name#data.get("name")
            if outname == "":
                self.get_logger().info(f"Must delete a named file if deleting by name. Delete by time range instead.")
                response.outdata = json.dumps({"status": "ERROR", "reason": "Can't delete unnamed file. Delete by time range instead."})
                return response
            # Match directories like: "outname"
            matches = list(DATA_DIR.glob(f"{outname}"))
            
            # No matches
            if not matches:
                response.outdata = json.dumps({
                    "success": False,
                    "error": f"No bag found with name '{outname}'"
                })
                return response

            # Get list of files to be deleted (should only be one)
            deleted = []
            for path in matches:
                if path.is_dir():
                    shutil.rmtree(path)
                    deleted.append(path.name)

            self.get_logger().info(f"Deleted {outname}")
                

            response.outdata = json.dumps({
                "success": True,
                "deleted": deleted
            })

        except Exception as e:
            response.outdata = json.dumps({"success": False, "error": str(e)})
        return response




def main(args=None):
    rclpy.init(args=args)
    node = DummyService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




