import rclpy
#import pidcontrol as pid
from math import atan2, asin
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class Balance(Node):

    def __init__(self):
        super().__init__('balance')
        print('is this working?')
        self.odomSubscriber = self.create_subscription(
            Odometry, '/spike/odom', self.callback, 10)
        self.velPublisher = self.create_publisher(Twist, '/spike/cmd_vel', 10)
        self.odomSubscriber
        self.pitchPrev = 0
        self.setPoint = 0  # radians
        self.Kp = 8
        self.Ki = 0.6
        self.Kd = 0.1
        self.errorPrev = 0
        self.integral = 0
        self.result = 0

    def callback(self, msg):
        x = msg.pose.pose.orientation.x
        y = msg.pose.pose.orientation.y
        z = msg.pose.pose.orientation.z
        w = msg.pose.pose.orientation.w

        pitch = self.Quarternion_2_Euler(x, y, z, w)
        print('pitch ', pitch)
        # calculate error
        error = self.setPoint - pitch

        # anti windup:
        if self.result < 100:
            self.integral = self.integral + (error*0.25)
        else:
            self.integral = self.integral

        derivative = error - self.errorPrev
        # reassign the error to errorPrev

        self.errorPrev = error
        self.result = (error * self.Kp) + (derivative * self.Kd) + \
            (self.integral * self.Ki)
        # print(result)

        if -0.03 < self.result < 0.0175:
            self.result = 0.0

        if 0.0175 < self.result < 0.03:
            self.result = 0.0

        vel = Twist()
        vel.linear.x = -1*self.result

        self.velPublisher.publish(vel)

    def Quarternion_2_Euler(self, x, y, z, w):
        #sinp = 2 * (w * y - z * x)
        #pitch = asin(sinp)
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = atan2(sinr_cosp, cosr_cosp)
        return roll


def main(args=None):
    rclpy.init(args=args)
    print('initialized rclpy')
    balance = Balance()
    print('initialized Node')

    rclpy.spin(balance)
    print('Spun up the node')

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    balance.destroy_node()
    print('shutting down')
    rclpy.shutdown()


if __name__ == '__main__':
    main()
