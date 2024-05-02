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

zero = 500000
one_eight = 2500000 
total_degrees = 180
total_pwm_change = one_eight - zero
pwm_per_degree = total_pwm_change/total_degrees


def move_servo15():
    degree_finder = zero = (pwm_per_degree * 7)
    os.system("echo" + str(degree_finder) + "> /sys/class/pwm/pwmchip0/pwm1/duty_cycle")
    time.sleep(1)
    # os.system("echo 2500000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle")
    # time.sleep(1)
    # os.system("echo 500000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle")

def main():
    os.system("sudo systemctl stop robot")

if __name__ == "__main__":
    main()