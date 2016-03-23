from SoftBlock import *

class Sand(SoftBlock):
    def __init__(self, pos=[0,0], blockSize = 25):
        image = "Block/Block Images/sand.png"
        SoftBlock.__init__(self, image, pos, blockSize)
