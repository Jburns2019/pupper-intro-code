#!/usr/bin/env python3

import os
import sys
import time

# This is a script that will allow you to move each indidual servo!
# With this you will be able to make custom movements.
# below is an example of how might you use this, build on it if you think it is helpful
# What you need to change is the pwm# value which matches each servo
# pwm1 = J15 connection on the board
# pwm 2 = J14...... pwm16 = J1
# ranges:  0 degree(echo 500000), 90 degree(echo 1500000), 180 degree(echo 2500000)

# The following test was done plugging in an extra servo to J15

verbose = False
zero = 500000
ninety = 1500000
one_eight = 2500000

def foot_angle(deg=0):
    return int(deg*(one_eight-zero)/180.0 + zero)

def send_angle(angle=0, servo_num=10):
    os.system(f"echo {foot_angle(angle)} > /sys/class/pwm/pwmchip0/pwm{servo_num}/duty_cycle")

    if verbose:
        print(f'Moved servo {servo_num} to {angle}.')

def make_front_left_foot_walk():
    # send_angle(20, 10)
    # send_angle(20, 11)

    # for i in range(40, 140, 20):
    #     send_angle(i, 10)
    #     time.sleep(3)
    
    # send_angle(20, 11)
    
    # for i in range(40, 120, 20):
    #     send_angle(i, 11)
    #     time.sleep(3)

    start = [(70, 90), (100, 90), (100, 40), (30, 70)]
    # send_angle(100, 11)
    # send_angle(90, 10)
    while True:
        for hip, leg in start:
            send_angle(hip, 11)
            send_angle(leg, 10)
            time.sleep(.1)
            
            send_angle(hip, 13)
            send_angle(leg, 14)
            time.sleep(.1)

            send_angle(hip, 4)
            send_angle(leg, 5)
            time.sleep(.1)

            send_angle(hip, 7)
            send_angle(leg, 8)
            time.sleep(.1)

def main():
    os.system("sudo systemctl stop robot")
    make_front_left_foot_walk()
    os.system("sudo systemctl stop robot")

if __name__ == "__main__":
    main()