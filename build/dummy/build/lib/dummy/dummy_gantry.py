import rclpy
from rclpy import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point
import time

class DummyGantry(Node):

    def __init__(self):
        super().__init__('dummy_gantry', namespace='gantry')

        #set up publishers
        self.mode_pub = self.create_publisher(String, 'setMode', 10)

        #set up subscribers
        self.mode_sub = self.create_subscription(String, 'setMode', self.read_mode(), 10)
        self.goto_sub = self.create_subscription(Point, 'gotoLocation', self.read_goto(), 10)

        #useful variables
        self.current_mode = None
        self.current_point = None

        self.hold_msg = String(data="HOLD")
        self.goto_msg = String(data="GOTO")

    def read_mode(self, msg):
        self.current_mode = msg

    def read_goto(self, msg):
        self.current_point = msg
        self.handle_goto(self, msg)

    def handle_goto(self, point):
        if self.current_mode == "GOTO":
            self.get_logger().info(f"recieved location {point.x, point.y, point.z}. starting wait time")
            
            self.current_mode = "GOTO"
            self.mode_pub(self.goto_msg)
            rclpy.spin_once(timeout_sec=1.0)

            time.sleep(5)

            self.current_mode = "HOLD"
        else:
            self.get_logger().info("not the right mode")

def main():
    rclpy.init()
    ros_node = DummyGantry()
    rclpy.spin(ros_node)
    ros_node.destroy_node()
    rclpy.shutdown()

            





        




