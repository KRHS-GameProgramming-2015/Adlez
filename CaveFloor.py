from SoftBlock import *

class CaveFloor(SoftBlock):
    def __init__(self, pos=[0,0], blockSize = 25):
        image = "Block/Block Images/cavefloor.png"
        SoftBlock.__init__(self, image, pos, blockSize)

