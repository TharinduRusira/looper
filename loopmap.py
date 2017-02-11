'''
create a loop layer for each transform. This will link loops from the previous version to the new version.
 This is useful in case
    1. automatically generating transformation sequences
    2. to rollback a transformation and restore the previous state
'''

from loopnest import LoopNest

class Layer:
    def __init__(self,nest):
        if type(nest) is LoopNest:
            self.layer = nest
        else:
            raise TypeError


class LoopMap:
    def __init__(self):
        self.layers = []
        self.links = []

    def add_layer(self,layer):
        self.layers.append(layer)

    #add a link from x-th layer's i-th loop to (x+1)-th layer's j-th loop.

    def link_i_to_j(self,x,i,j):
        assert(x <= len(self.layers)-1)
        assert(i <= len(self.layers[x]) and j <= len(self.layers[x+1]) )
        (self.links[i][x]).append(j)