from tutorial_interfaces.srv import ControlSpeed #imports the service type AddTwoInts
from time import sleep
import serial

import rclpy
from rclpy.node import Node

class MinimalService(Node):

   def __init__(self):
       super().__init__('minimal_service') #sets the node name
       self.srv = self.create_service(ControlSpeed, 'control_speed', self.control_speed_callback)

       self.serialPort0 = serial.Serial(port = '/dev/ttyS0',
        baudrate = 115200,
        timeout= 1)

   def control_speed_callback(self, request, response):
       self.get_logger().info('Incoming request\n MOTOR_SPEED: %d' %(request.speed))
       response.success = True
       print(type(request.speed))
       self.serialPortWriteBytes(bytes(str(request.speed),'utf-8'))
       print('I wrote the bytes')
       feedback = self.serialPort0.read(100)
       print(feedback)  
       return response

   def serialPortWriteBytes(self, writeBytes):
      self.serialPort0.write(writeBytes)
      return


def main(args=None):
   rclpy.init(args=args)

   minimal_service = MinimalService()

   rclpy.spin(minimal_service)

   rclpy.shutdown()


if __name__ == '__main__':
   main()
