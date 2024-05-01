#!/usr/bin/env python3

import numpy as np
import time
from src.IMU import IMU
from src.Controller import Controller
from src.JoystickInterface import JoystickInterface
from src.State import BehaviorState, State
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from MangDang.mini_pupper.display import Display
from src.MovementScheme import MovementScheme
from src.danceSample import MovementLib


def main(use_imu=False):
    state = State()
    config = Configuration()
    hardware_interface = HardwareInterface()
    movementCtl = MovementScheme(MovementLib)

    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()

    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )

    # Read imu data. Orientation will be None if no data was available
    quat_orientation = (
        imu.read_orientation() if use_imu else np.array([1, 0, 0, 0])
    )
    state.quat_orientation = quat_orientation

    movementCtl.runMovementScheme()
    legsLocation = movementCtl.getMovemenLegsLocation()
    attitudes = movementCtl.getMovemenAttitude()
    speed = movementCtl.getMovemenSpeed()
    print(speed, attitudes, legsLocation) 
    hardware_interface.set_actuator_postions(state.joint_angles)

if __name__ == "__main__":
    main()
