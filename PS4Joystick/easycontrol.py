from UDPComms import Publisher
import time 
# look into joystickinterface.py for control outputs
# drive_pub = Publisher(8830) = controls movement of pupper (basically mode 1)
# arm_pub = Publisher(8410) = controls more movements of upper (mode 2)
# mode 2 is what you can do when pupper is not in trot mode when using a controller.
drive_pub = Publisher(8830)
arm_pub = Publisher(8410)
# L1 = activate/disactivate
# R1 = transition between Rest mode and Trot mode.
# circle = dance or hold for 3 seconds to turn off system
# trinagle  = NOTHING 
# X = jump
# L2 = nothing
# R2 = Nothing
# ly = forward or backwards
# lx = left or right
# rx = turn left or right (pitch)
# ry = pitches the robot forward
def activate():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
def lean():
    target_vel = {"x": 0.0,
                  "y": 0.8,
                  "z": 0.0, # (r_trigger - l_trigger)/2,
                  "yaw": 0,  # r_side,
                  "pitch": 0, # r_forward,
                  "roll": 0,  # (r_shoulder - l_shoulder),
                  "grip": 0,  # cross - square,
                  "hat":  0, # hat,
                  "reset": 0,  # reset,
                  "resetdock": 0,  #reset_dock,
                  "trueXYZ": 0,  # circle,
                  "dock": 0}  # triangle}
    arm_pub.send(target_vel)

def trot():
    drive_pub.send({"L1": 0, 
            "R1": 1, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
    
def move_forward():
    # while True:
    drive_pub.send({"L1": 0, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0.8, 
            "lx": 0.2, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
if __name__ == "__main__":
    activate()
    # trot()
    time.sleep(1)
    trot()
    time.sleep(1)

    while True:
        move_forward()
    # trot_stop()
    # activate_stop()