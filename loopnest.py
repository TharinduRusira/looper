'''
Implements a single loop nest, which is referred to as a 'layer' in the context of a loop map
'''
class Loop:
    def __init__(self,lo=None,high=None,interval=None):
        self.lo = lo;
        self.high = high
        self.interval = interval

class LoopNest:
    def __init__(self, n):
        self.num_loops = n
        self.loop_list = []

    #append a new loop to the end of the list
    #in loop nest, this is the new innermost loop
    def add_loop(self, lo=None,hi=None,interval=None):
        self.loop_list.append(Loop(lo,hi,interval))
        return self.loop_list

    #remove innermost loop
    def remove_loop(self):
        self.loop_list = self.loop_list[0:-1]
        return self.loop_list

    #add one loop after kth loop
    def add_one_after(self, k, lo=None,hi=None,interval=None):
        head = self.loop_list[:k]
        head.append(Loop(lo,hi,interval))
        self.loop_list = head + self.loop_list[k:]
        return self.loop_list

    #remove k-th loop
    def remove_one_after(self,k):
        head = self.loop_list[:k]
        self.loop_list = head + self.loop_list[k+1:]
        return self.loop_list


