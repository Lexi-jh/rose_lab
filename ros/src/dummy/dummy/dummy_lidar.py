#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
import numpy as np
import os
import math
import struct
from builtin_interfaces.msg import Time

class DummyLidar(Node):
    def __init__(self):
        super().__init__('dummy_lidar')

        # Parameters with defaults
        self.declare_parameter('topic', 'points')
        self.declare_parameter('rate', 10.0)  # Hz
        self.declare_parameter('width', 160)   # horizontal resolution
        self.declare_parameter('height', 120)  # vertical resolution (organized -> height>1)
        self.declare_parameter('fov_x_deg', 70.0)   # horizontal FOV degrees
        self.declare_parameter('fov_y_deg', 55.0)   # vertical FOV degrees
        self.declare_parameter('max_range', 9.0)
        self.declare_parameter('min_range', 0.2)
        self.declare_parameter('noise_std', 0.02)   # meters
        self.declare_parameter('frame_id', 'l515_frame')

        topic = self.get_parameter('topic').get_parameter_value().string_value
        rate = self.get_parameter('rate').get_parameter_value().double_value
        self.width = int(self.get_parameter('width').get_parameter_value().integer_value)
        self.height = int(self.get_parameter('height').get_parameter_value().integer_value)
        self.fov_x = math.radians(self.get_parameter('fov_x_deg').get_parameter_value().double_value)
        self.fov_y = math.radians(self.get_parameter('fov_y_deg').get_parameter_value().double_value)
        self.max_range = float(self.get_parameter('max_range').get_parameter_value().double_value)
        self.min_range = float(self.get_parameter('min_range').get_parameter_value().double_value)
        self.noise_std = float(self.get_parameter('noise_std').get_parameter_value().double_value)
        self.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value

        self.pub = self.create_publisher(PointCloud2, topic, 10)
        period = 1.0 / float(rate)
        self.create_timer(period, self.timer_callback)
        self.get_logger().info(f"Publishing fake L515 on '{topic}' at {rate}Hz, resolution {self.width}x{self.height}")

        # Precompute angle grids
        xs = np.linspace(-self.fov_x/2.0, self.fov_x/2.0, self.width)
        ys = np.linspace(-self.fov_y/2.0, self.fov_y/2.0, self.height)
        self.xv, self.yv = np.meshgrid(xs, ys)  # shape (height, width)

    def timer_callback(self):
        # Generate depth frame (height x width)
        # Example surface: vary with angles to make interesting shape
        depth = 3.0 + 0.5*np.sin(3.0*self.xv) + 0.3*np.cos(2.0*self.yv)
        depth += np.random.normal(0.0, self.noise_std, size=depth.shape)
        depth = np.clip(depth, self.min_range, self.max_range)

        # Convert to point cloud: project from angular grid to XYZ
        # x = z * tan(theta_x), y = z * tan(theta_y), z = z
        X = depth * np.tan(self.xv)
        Y = depth * np.tan(self.yv)
        Z = depth

        # Flatten to N x 3
        points = np.stack((X, Y, Z), axis=-1).reshape(-1, 3).astype(np.float32)

        # Build PointCloud2 message
        msg = PointCloud2()
        now = self.get_clock().now().to_msg()
        msg.header.stamp = now
        msg.header.frame_id = self.frame_id
        msg.height = 1
        msg.width = points.shape[0]
        msg.is_dense = False
        msg.is_bigendian = False

        # Fields: x, y, z as float32
        msg.fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1)
        ]
        msg.point_step = 12  # 3 * 4 bytes
        msg.row_step = msg.point_step * points.shape[0]
        msg.data = points.tobytes()

        # Publish
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DummyLidar()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

