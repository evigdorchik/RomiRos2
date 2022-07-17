#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from romi_interfaces.msg import RomiState
from a_star import AStar


class RomiAstarNode(Node):
    def __init__(self):
        super().__init__("romi_astar_comms")

        self.leds_ = [False, False, False]
        self.notes_ = ""
        self.motors_ = [0, 0]
        self.buttons_ = [False, False, False]
        self.battery_millivolts_ = 0
        self.analog_ = [0, 0, 0, 0, 0, 0]
        self.encoders_ = [0, 0]

        self.astar_publisher_ = self.create_publisher(RomiState,"romi_state", 10)
        self.astar_timer_ = self.create_timer(0.01, self.publish_state)

    def publish_state(self):
        msg = RomiState()
        msg.leds = self.leds_
        msg.notes = self.notes_
        msg.motors_ = self.motors_
        msg.buttons_ = self.buttons_
        msg.battery_millivolts_ = self.buttons_
        msg.analog_ = self.analog_
        msg.encoders_ = self.encoders_



def main(args=None):
    rclpy.init(args=args)
    node = RomiAstarNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()