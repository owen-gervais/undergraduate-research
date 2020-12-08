# -*- coding: utf-8 -*-
'''
@author: Owen Gervais

Credit for PID loop goes to Daniel Bekai

'''

from spike import MotorPair
import utime
import hub

def pid(kp:float, ki:float, kd:float, target:int, motor_pair)->tuple:
    #iteration counter:

    i = 0

    #defining initial values
    integral = 0
    derivative = 0
    previous_error = 0
    result = 0
    rot = hub.motion.yaw_pitch_roll()
    
    #PID loop
    while abs(rot[2]) < 30:
        i = i + 1
        rot = hub.motion.yaw_pitch_roll()
        error = target - rot[2]

        #anti windup:
        if result < 100:
            integral = integral + (error*0.25)
        else:
            integral = integral
        derivative = error - previous_error
        previous_error = error
        result = (error * kp) + (integral * ki) + (derivative * kd)
        result = -1 * int(result)
        motor_pair.start_at_power(result, 0)
    return 


def main():
    motor_pair = MotorPair('B', 'A')

    # Establishing Gains
    Kp = 8
    Kd = 0.1
    Ki = 0
    
    while True:
        target = 0
        pid(Kp, Kd, Ki, target, motor_pair)
        motor_pair.stop()

    return

main()
    


