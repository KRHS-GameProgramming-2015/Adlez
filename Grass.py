from SoftBlock import *

class Grass(SoftBlock):
    def __init__(self, pos=[0,0], blockSize = 25):
        image = "Block/Block Images/grass.png"
        SoftBlock.__init__(self, image, pos, blockSize)

class BigGrass(SoftBlock):
    def __init__(self, pos=[0,0], blockSize = 25):
        image = "Block/Block Images/grass5x5.png"
        SoftBlock.__init__(self, image, pos, blockSize)
