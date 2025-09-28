# import rclpy
# from rclpy import Node
# from gantry_lidar_interfaces.srv import Capture, DownloadName, DownloadTimeRange, DeleteName, DeleteTimeRange

# class DummyService(Node):
#     def __init__(self):
#         super().__init__('gantry_capture_service')

#         # Info
#         self.create_service(Trigger, 'gantry_capture_service/info', self.info_callback)
        
#         # Capture sensor data
#         self.create_service(Capture, 'gantry_capture_service/capture', self.capture_callback)

#         # Download
#         self.create_service(DownloadName, 'gantry_capture_service/download/name', self.download_name_callback)
#         self.create_service(DownloadTimeRange, 'gantry_capture_service/download/timeRange', self.download_time_range_callback)

#         # Delete
#         self.create_service(DeleteName, 'gantry_capture_service/delete/name', self.delete_name_callback)
#         self.create_service(DeleteTimeRange, 'gantry_capture_service/delete/timeRange', self.delete_time_range_callback)
        
#         # Start HTTP server
#         start_http_server()

#         self.get_logger().info("Gantry capture service running")




