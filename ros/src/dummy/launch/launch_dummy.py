from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    lidar_node = Node(
        package = "dummy",
        executable = "dummy_lidar",
        name = "dummy_lidar",
    )

    service_node = Node(
        package="dummy",
        executable="gantry_capture_service",
        name="gantry_capture_service"
    )

    return LaunchDescription([
        lidar_node,
        service_node
    ])
