import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point

import queue


class DummyGantry(Node):

    def __init__(self):
        super().__init__('dummy_gantry', namespace='gantry')

        # publishers + subscribers
        self.mode_pub = self.create_publisher(String, 'setMode', 10)
        self.mode_sub = self.create_subscription(String, 'setMode', self.read_mode, 10)
        self.goto_sub = self.create_subscription(Point, 'gotoLocation', self.read_goto, 10)

        # state tracking
        self.current_mode = 'HOLD'
        self.current_point = Point()
        self.points_q = queue.Queue()
        self.travel_timer = None

        self.hold_msg = String(data='HOLD')
        self.goto_msg = String(data='GOTO')

        # publish initial mode so listeners know the simulated state
        self.mode_pub.publish(self.hold_msg)

        #debug
        self.counter = 0

    def read_mode(self, msg: String):
        self.current_mode = msg.data
        self.get_logger().debug(f'Set mode -> {self.current_mode}')
        if self.current_mode == 'GOTO':
            self.handle_goto()

    def read_goto(self, msg: Point):
        self.current_point = msg
        self.points_q.put(msg)
        self.handle_goto()

    def handle_goto(self):

        if self.points_q.empty():
            self.get_logger().info('Ignoring goto request because no target trajectory')
            rclpy.spin_once(self, timeout_sec=1.0)
            return
           
        if self.current_mode == 'HOLD':
            rclpy.spin_once(self, timeout_sec=1.0)
            return
            
        
        point = self.points_q.get()

        self.get_logger().info(
            f'Simulating move to ({point.x:.2f}, {point.y:.2f}, {point.z:.2f})'
        )

        # notify listeners that the gantry started travelling
        self.mode_pub.publish(self.goto_msg)

        # after a short delay, publish that the gantry returned to HOLD
        self.travel_timer = self.create_timer(5.0, self._finish_move)

    def _finish_move(self) -> None:
        if self.travel_timer:
            self.travel_timer.cancel()
            self.travel_timer = None

        self.current_mode = 'HOLD'
        self.mode_pub.publish(self.hold_msg)
        self.get_logger().info('Finished simulated move. Mode -> HOLD')
        self.counter += 1


def main() -> None:
    rclpy.init()
    ros_node = DummyGantry()
    try:
        rclpy.spin(ros_node)
    finally:
        ros_node.destroy_node()
        rclpy.shutdown()

