from src.Command import Command
from src.State import BehaviorState, State
import numpy as np
import time
from MangDang.mini_pupper.HardwareInterface import HardwareInterface

state = State()
command = Command()
hardware_interface = HardwareInterface()

state.quat_orientation = np.array([1,0,0,0])

state.behavior_state = BehaviorState.TROT

command.horizontal_velocity = np.array([0.1,0])

# controller.run(state, command,disp)
hardware_interface.set_actuator_postions(state.joint_angles)