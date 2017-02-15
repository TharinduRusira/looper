'''
This class explains the changes to the loop nest as a result of different transforms
It computes the affect of each transform and map the current loop layer to the next loop layer
'''
from loopnest import *
from loopmap import *


# for each new transformation,
#   1. create a new layer
#   2. based on the transform's nature and parameters, decide the number of loops in the next layer
#   3. map loop levels accordingly


class Transform:
    def tile(self, loop):
        pass

    def unroll(self,loop):
        pass

    def permute(self, loop_list):
        pass

    def fuse(self, loop_list):
        pass

    def distribute(self, loop):
        pass

