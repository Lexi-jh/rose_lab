import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from sensor_msgs.msg import PointCloud2

from datetime import datetime, timedelta
import subprocess
import shutil
from pathlib import Path
import json
import random
import time
import threading


from gantry_lidar_interfaces.srv import (
    Capture,
    DownloadName,
    DownloadTimeRange,
    DeleteName,
    DeleteTimeRange,
)


#file stuff and opening remote server function
DATA_DIR = Path.home() / "RoSE_Bags"
TIME_STR = "%Y-%m-%dT%H-%M-%S"

def start_http_server():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return subprocess.Popen([
        "python3",
        "-m",
        "http.server",
        "8000",
        "--directory",
        str(DATA_DIR),
        "--bind",
        "0.0.0.0",
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
        
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        # Start HTTP server to expose recorded bags
        try:
            self.http_server_process = start_http_server()
        except Exception as exc:
            self.http_server_process = None
            self.get_logger().warning(f'Failed to start HTTP server: {exc}')

        #variables
        self.lidar_data = None
        self.recording_active = False
        self.session_info = None
        self.filename = None

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
        try:
            duration = max(float(request.duration), 0.0)
            sensors = list(request.sensors)
            outname = str(request.outname or "").strip()

            if duration <= 0.0:
                raise ValueError('duration must be > 0 seconds')

            if not outname:
                raise ValueError('outname must be provided')

            if self.recording_active:
                raise RuntimeError('capture already in progress')

            base_topics = ["/tf", "/tf_static", "/gantry/gantry_status/gantry_state"]
            extra_topics = self._topics_from_sensors(sensors)
            if not extra_topics:
                extra_topics = [str(sensor) for sensor in sensors if isinstance(sensor, str) and sensor]
            topics = list(dict.fromkeys(base_topics + extra_topics))

            self._start_fake_capture(outname, sensors, topics)
            self.get_logger().info(f"Simulating capture for {duration}s with topics: {topics}")

            time.sleep(duration)

            stopped, details = self._stop_fake_capture(expected_duration=duration)
            if not stopped:
                raise RuntimeError('failed to finalize fake capture')

            response.outdata = json.dumps({
                "status": "ACK",
                "duration": duration,
                "sensors": sensors,
                "topics": topics,
                "outname": details.get("outname"),
                "fake_bag_path": details.get("bag_path"),
                "frames_per_sensor": details.get("frames_per_sensor"),
                "http_url": details.get("http_url"),
            })

        except Exception as e:
            self._stop_fake_capture()
            response.outdata = json.dumps({"status": "ERROR", "reason": str(e)})
        return response

    def download_name_callback(self, request, response):
        """
        Download bags by name. All bags with matching name will be downloaded (although there should only be one)
        """
        try:
            outname = request.name

            # Get matches newest first
            matches = sorted(DATA_DIR.glob(f"{outname}*"), reverse=True)
            if not matches:
                self.get_logger().info('Download name request failed, file not found.')
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
            outname = request.name
            if outname == "":
                self.get_logger().info(f"Must delete a named file if deleting by name. Delete by time range instead.")
                response.outdata = json.dumps({"status": "ERROR", "reason": "Can't delete unnamed file. Delete by time range instead."})
                return response
            # Match directories like: "outname"
            matches = list(DATA_DIR.glob(f"{outname}*"))
            
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

    def download_time_range_callback(self, request, response):
        try:
            start = parse_time(request.start) if request.start else None
            end = parse_time(request.end) if request.end else None
            if start and end and start > end:
                raise ValueError('start must be <= end')
        except ValueError as exc:
            response.outdata = json.dumps({"success": False, "error": str(exc)})
            return response

        matches = [path.name for path in self._bags_within_range(start, end)]
        urls = [f"http://0.0.0.0:8000/{name}" for name in matches]

        response.outdata = json.dumps({
            "success": True,
            "urls": urls,
        })
        return response

    def delete_time_range_callback(self, request, response):
        try:
            start = parse_time(request.start) if request.start else None
            end = parse_time(request.end) if request.end else None
            if start and end and start > end:
                raise ValueError('start must be <= end')
        except ValueError as exc:
            response.outdata = json.dumps({"success": False, "error": str(exc)})
            return response

        deleted = []
        for bag_dir in self._bags_within_range(start, end):
            shutil.rmtree(bag_dir, ignore_errors=True)
            deleted.append(bag_dir.name)

        response.outdata = json.dumps({
            "success": True,
            "deleted": deleted,
        })
        return response

    def _bags_within_range(self, start, end):
        results = []
        for path in DATA_DIR.iterdir():
            if not path.is_dir():
                continue
            timestamp = self._timestamp_from_name(path.name)
            if not timestamp:
                continue
            if start and timestamp < start:
                continue
            if end and timestamp > end:
                continue
            results.append(path)
        results.sort(key=lambda p: p.name)
        return results

    @staticmethod
    def _timestamp_from_name(name: str):
        try:
            _, ts = name.rsplit('_', 1)
            return datetime.strptime(ts, TIME_STR)
        except (ValueError, IndexError):
            return None

    @staticmethod
    def _topics_from_sensors(sensors):
        topic_map = {
            'lidar': 'points',
            'points': 'points',
            'gantry_lidar': 'points',
        }
        topics = []
        for sensor in sensors:
            if not isinstance(sensor, str):
                continue
            sensor_str = sensor.strip()
            if not sensor_str:
                continue
            if sensor_str.startswith('/'):
                topics.append(sensor_str)
                continue
            topic = topic_map.get(sensor_str.lower())
            if topic:
                topics.append(topic)
        return list(dict.fromkeys(topics))

    def _start_fake_capture(self, outname, sensors, topics):
        timestamp = datetime.now().strftime(TIME_STR)
        self.filename = f"{outname}_{timestamp}"
        bag_path = (DATA_DIR / self.filename).resolve()
        bag_path.mkdir(parents=True, exist_ok=True)

        metadata = {
            "outname": self.filename,
            "requested_name": outname,
            "started_at": datetime.now().isoformat(),
            "sensors": list(sensors),
            "topics": list(topics),
            "mode": "dummy",
        }
        (bag_path / "metadata.json").write_text(json.dumps(metadata, indent=2))

        self.session_info = {
            "path": bag_path,
            "sensors": list(sensors),
            "topics": list(topics),
            "started_at": time.time(),
            "metadata": metadata,
        }
        self.recording_active = True
        self.get_logger().info(f"Preparing fake gantry capture at: {bag_path}")
        self.get_logger().info("Topics:\n  " + "\n  ".join(topics))
        return self.session_info

    def _write_fake_frames(self, bag_path, sensors, duration):
        approx_frames = max(5, int(round(duration)))
        approx_frames = min(approx_frames, 300)
        if approx_frames <= 0:
            approx_frames = 5

        frames = []
        base_time = datetime.now()
        for idx in range(approx_frames):
            ts = base_time + timedelta(milliseconds=200 * idx)
            frame = {"timestamp": ts.isoformat(), "sensors": {}}
            for sensor in sensors:
                sensor_name = sensor if isinstance(sensor, str) else f"sensor_{idx}"
                frame["sensors"][sensor_name] = {
                    "point_count": random.randint(500, 2000),
                    "intensity_mean": round(random.uniform(0.0, 1.0), 4),
                    "range_min": round(random.uniform(0.3, 1.0), 3),
                    "range_max": round(random.uniform(5.0, 20.0), 3),
                    "note": "synthetic gantry lidar frame",
                }
            frames.append(frame)

        (bag_path / "frames.json").write_text(json.dumps(frames, indent=2))
        bag_file = bag_path / f"{bag_path.name}.db3"
        bag_file.write_text("FAKE ROS2 BAG CONTENT. Generated by dummy_service for testing.\n")
        return len(frames)

    def _stop_fake_capture(self, expected_duration=None):
        if not self.recording_active or not self.session_info:
            return False, {}

        bag_path = self.session_info["path"]
        sensors = self.session_info["sensors"]
        topics = self.session_info["topics"]
        started_at = self.session_info["started_at"]
        current_name = self.filename

        duration = expected_duration
        if duration is None:
            duration = max(0.0, time.time() - started_at)

        frame_count = self._write_fake_frames(bag_path, sensors, duration)

        metadata = dict(self.session_info["metadata"])
        metadata.update({
            "stopped_at": datetime.now().isoformat(),
            "duration_seconds": duration,
            "frames_per_sensor": frame_count,
            "fake_data": True,
            "http_url": f"http://0.0.0.0:8000/{bag_path.name}",
        })
        (bag_path / "metadata.json").write_text(json.dumps(metadata, indent=2))

        details = {
            "outname": current_name,
            "bag_path": str(bag_path),
            "duration": duration,
            "frames_per_sensor": frame_count,
            "topics": topics,
            "http_url": metadata["http_url"],
        }

        self.recording_active = False
        self.session_info = None
        self.filename = None

        return True, details

    def destroy_node(self):
        if self.recording_active:
            self.get_logger().info('Finalizing active fake capture before shutdown')
            self._stop_fake_capture()

        if self.http_server_process and self.http_server_process.poll() is None:
            self.get_logger().info('Stopping HTTP server')
            self.http_server_process.terminate()
            try:
                self.http_server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.http_server_process.kill()
        self.http_server_process = None

        return super().destroy_node()




def main(args=None):
    rclpy.init(args=args)
    node = DummyService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
