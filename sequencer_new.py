'''
1. generate all possible inputs
2. compose corresponding CHiLL script
3. call CHiLL to transform code
4. Run transformed code
5. Evaluate performance (time)
6. Save results to a custom database
'''

import sqlite3
import itertools
import os
import time
import re

from codegen import *
from scanner import *

class Sequencer:



    def __init__(self, xform, path, procedure):
        self.xform = xform
        self.path = path
        self.procedure = procedure

        fn = self.path.split('/')[-1]
        dir = re.sub(fn, '', self.path)

        self.cfile = {'path': self.path, 'name': fn, 'dir': dir, 'procedure': self.procedure}
        self.fdata = Scanner(self.cfile['path']).scan_loop()
        self.cg = CHiLLCodeGen()

    def generate_space(self):
        input_range = [1, 2, 3, 4, 5, 6]  # log(input size)
        loop_range = range(1, self.fdata['depth']+1)
        stms_range = range(0, self.fdata['depth'])
        amount_range = [4,8,16,32,64]
        itr = list(itertools.product(input_range,loop_range,stms_range, amount_range))
        return itr


    def run(self, itr):
        if self.xform == 'tile':
            for i in itr:
                # TODO: inject input size to the C file
                #TODO: generate chill script
                self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=i[1],
                                              transformations=[['tile', i[2], i[1], i[3]]])
                #TODO: compile the transformead code
                #TODO: run and measure time
                #TODO: write record to database
        else:
            print 'error: unknown transform \''+self.xform+'\'\n'
            exit(-1)



