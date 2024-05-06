from UDPComms import Publisher
import time

# drive_pub = Publisher(8830) = controls movement of pupper (basically mode 1)
# arm_pub = Publisher(8410) = controls more movements of upper (mode 2)
# mode 2 is what you can do when pupper is not in trot mode when using a controller.
drive_pub = Publisher(8830) 
# arm_pub = Publisher(8410)
# L1 = activate/disactivate
# R1 = transition between Rest mode and Trot mode.
# circle = dance or hold for 3 seconds to turn off system
# trinagle  = NOTHING 
# X = jump
# L2 = nothing
# R2 = Nothing
# The range for the following are form (-1, 1)
# ly = forward or backwards
# lx = left or right
# rx = turn left or right (pitch)
# ry = pitches the robot forward

is_on = False
is_trotting = False

def make_cmd(command = {}, toggle_activation=False, toggle_trot=False, jump=False, l2=False, r2=False, y=0, x=0, xy_yaw=0, xy_pitch=0, circle=False, triangle=False, dpadx=0, dpady=0, message_rate=20):
    command["L1"] = int(toggle_activation)
    command["R1"] = int(toggle_trot)
    command["x"] = int(jump)
    command["circle"] = int(circle)
    command["triangle"] = int(triangle)
    command["L2"] = int(l2)
    command["R2"] = int(r2)
    command["ly"] = y
    command["lx"] = x
    command["rx"] = xy_yaw
    command["message_rate"] = message_rate
    command["ry"] = xy_pitch
    command["dpady"] = dpady
    command["dpadx"] = dpadx

    return command

def activate():
    global is_on
    if not is_on:
        drive_pub.send(make_cmd(toggle_activation=True))
        # print(make_cmd(toggle_activation=True))
        is_on = True

def deactivate():
    global is_on, is_trotting

    toggle_trot = False
    if is_trotting:
        toggle_trot = True

    if is_on:
        drive_pub.send(make_cmd(toggle_activation=True))
        # print(make_cmd(toggle_activation=True, toggle_trot=toggle_trot))
        is_on = False
        is_trotting = False

def move(dir: str='None'):
    global is_trotting

    if dir == 'None':
        stop_moving()
    else:
        x = 0
        if 'left' in dir:
            x = -1
        elif 'right' in dir:
            x = 1
        
        y = 0
        if 'forward' in dir:
            y = 1
        elif 'back' in dir:
            y = -1

        toggle_trot = False
        if not is_trotting:
            toggle_trot = True

        drive_pub.send(make_cmd(toggle_trot=toggle_trot, x=y, y=y))
        # print(make_cmd(toggle_trot=toggle_trot, x=x, y=y))
        is_trotting = True

def turn(dir: str='None'):
    global toggle_trot

    if dir == 'None':
        stop_moving()
    else:
        xy_yaw = 0
        if 'right' in dir:
            xy_yaw = 1
        elif 'left' in dir:
            xy_yaw = -1
        
        y = 0
        if 'forward' in dir:
            y = 1
        elif 'back' in dir:
            y = -1

        toggle_trot = False
        if not is_trotting:
            toggle_trot = True

        drive_pub.send(make_cmd(toggle_trot=toggle_trot, y=y, xy_yaw=xy_yaw))
        # print(make_cmd(toggle_trot=toggle_trot, y=y, xy_yaw=xy_yaw))
        is_trotting = True

def stop_moving():
    global is_trotting

    toggle_trot = False
    if is_trotting:
        toggle_trot = True
    
    # drive_pub.send(make_cmd(toggle_trot=toggle_trot))
    print(make_cmd(toggle_trot=toggle_trot))
    is_trotting = False

# TODO: create functions that allow the robot to move around (forward,back,right,left,....)
# Remember: The inputs are mainly digital except for the lx,ly and rx,ry controls.
# The digital inputs do not reset after being call unless you design them to! (i.e., if you press L1 it will remaind press)
# Each action needs to be press once then can be ignored (you don't have to keep L1 as 1 you can create an activate function the forget about it)   
# TODO: make the robot move through the racing track
if __name__ == "__main__":
    activate()
    move('forward')
    time.sleep(2)
    move('right')
    time.sleep(2)
    move('forward-right')
    time.sleep(2)
    deactivate()
    