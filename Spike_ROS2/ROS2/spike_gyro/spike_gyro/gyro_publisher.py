from time import sleep
import serial

import rclpy
from rclpy.node import Node

from spike_interfaces.msg import Gyro


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('gyro_publisher')
        self.publisher_ = self.create_publisher(Gyro, 'gyro', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.serialPort = serial.Serial(port = '/dev/ttyS0',
         baudrate = 115200,
         timeout = 1)


    def timer_callback(self):
        msg = Gyro()
        print('I created the callback func')
        data = self.serialPort.readline().decode('utf-8')
        print(data)
        data = list(map(int,data[1:-2].split(',')))
        print(data)
        msg.pitch = data[0]
        msg.roll = data[1]
        msg.yaw = data[2]
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

