import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import yaml
from builtin_interfaces.msg import Time

class GantryTrajectory(Node):
    def __init__(self):
        super().__init__('path_publisher')

        self.trajectory_pub = self.create_publisher(Path, 'gantry/SetTrajectory', 10)
        self.mode_pub = self.create_publisher(String, '/gantry/setMode', 10) 
        self.test_name = str(input("File name: "))

        with open(f"{self.test_name}.yaml", "r") as f:
            waypoints = yaml.safe_load(f)

        path_msg = Path()

        #look at message details tomorrow morning
        path_msg.header.frame_id = "map"
        for point in waypoints:
            pose = PoseStamped()
            pose.header.frame_id="map"
            pose.pose.position.x = float(point["position_x"])
            pose.pose.position.y = float(point["position_y"])
            pose.pose.position.z = 0  
            pose.pose.orientation.x = 0
            pose.pose.orientation.y = 0
            pose.pose.orientation.z = 0
            pose.pose.orientation.w = 1.0

            sec = int(point["time"])
            nsec=int((point["time"]-sec)*1e9)
            pose.header.stamp = Time(sec=sec, nanosec=nsec)

            path_msg.poses.append(pose)

        
        mode_msg = String()
        mode_msg.data = "TRAJECTORY" #the other mode is HOLD, and GOTO is used to get to the starting position
        self.mode_pub.publish(mode_msg)
        self.trajectory_pub.publish(path_msg)
        self.get_logger().info(f"Published path with {len(path_msg.poses)} poses")

        rclpy.spin_once(self, timeout_sec=1.0)  # spin once to let publish happen
        self.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    GantryTrajectory()


if __name__ == "__main__":
    main()









