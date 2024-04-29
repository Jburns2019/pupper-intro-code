from UDPComms import Publisher
# look into joystickinterface.py for control outputs

a=Publisher(8830)

def activate():
    a.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 1, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def trot():
    a.send({"R1": 1})

# a.send({"L1": 1, "R1": 0, "x": 0, "circle": 0, "triangle": 0, "L2": 0, "R2": 0, "ly": 0, "lx": 0, "rx": 0, "message_rate": 1, "ry": 0, "dpady": 0, "dpadx": 0}) 
if __name__ == "__main__":
    activate()
    # trot()