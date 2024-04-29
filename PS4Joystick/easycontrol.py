from UDPComms import Publisher

a=Publisher(8830)
def activate(a):
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

activate()
# # a.send({"L1": 1, 
# #         "R1": 0, 
# #         "x": 0, 
# #         "circle": 0, 
# #         "triangle": 0, 
# #         "L2": 0, 
# #         "R2": 0, 
# #         "ly": 0, 
# #         "lx": 0, 
# #         "rx": 0, 
# #         "message_rate": 1, 
# #         "ry": 0, 
# #         "dpady": 0, 
# #         "dpadx": 0}) 

# if __name__ == "__main__":
#     a=Publisher(8830)
#     activate(a)