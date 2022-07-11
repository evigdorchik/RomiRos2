#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class RomiAstarNode(Node):
    def __init__(self):
        super().__init__("romi_astar_comms")
        self.astar_publisher = self.create_publisher()


def main(args=None):
    rclpy.init(args=args)
    node = RomiAstarNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()