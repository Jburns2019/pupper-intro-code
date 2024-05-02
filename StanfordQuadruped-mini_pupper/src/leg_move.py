#!/usr/bin/env python3

import os
import sys
import time

def main():
    os.system("sudo systemctl stop robot")
    os.system("echo 1500000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle")
    time.sleep(1)
    os.system("echo 2500000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle")
    time.sleep(1)
    os.system("echo 500000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle")

if __name__ == "__main__":
    main()