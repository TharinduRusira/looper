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
import subprocess
from subprocess import PIPE, Popen
import csv

class Sequencer:

    def __init__(self, xform, path, procedure):
        self.xform = xform
        self.path = path
        self.procedure = procedure

        fn = self.path.split('/')[-1]
        dir = re.sub(fn, '', self.path)

        self.cfile = {'path': self.path, 'name': fn, 'dir': dir, 'procedure': self.procedure}
        self.fdata = Scanner(self.cfile['path']).scan_loop()

        self.cg = CHiLLCodeGen(dir)

    def generate_space(self):
        input_range = [1, 2, 3]  # log(input size)
        loop_range = range(1, self.fdata['depth']+1)
        stms_range = range(0, self.fdata['depth'])
        amount_range = [4,8,16,32,64]
        itr = list(itertools.product(input_range,loop_range,stms_range, amount_range))
        return itr


    def run(self, itr):

        csvout = open('data_'+self.xform+'.csv','a')
        csvwriter = csv.writer(csvout, delimiter=',')

        if self.xform == 'tile':
            csvwriter.writerow(['input', 'depth', 'stms', 'arithmetic', 'memory', 'tiled loop', 'tiled stmt', 'tile size', 'cost'])                    #headers

            for i in itr:
                self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=0,
                                              transformations=[['tile', i[2], i[1], i[3]]])                             #generate CHiLL script

                p = Popen('chill xform.script'.split(), stdout=PIPE, stderr=PIPE)                                       #transform code
                p.communicate()         #wait for the returncode
                #verify p.returncode, if 0, success. Else invalid, cost = -INF

                if p.returncode != 0 :
                    elapsed = -1000.0
                else:
                    #compile run rose_*.c and get execution time
                    p1 = Popen(('gcc rose_'+self.cfile['name']+' -o tmp.bin').split(), stdout=PIPE, stderr=PIPE)
                    p1.communicate()
                    if  p1.returncode != 0:
                        print 'compiling transformed code failed with error code '+ str(p1.returncode) + '\n'
                        continue

                    start = time.clock()
                    p2 = subprocess.call('./tmp.bin')
                    elapsed = time.clock()*1000 - start*1000        #in ms
                    if p2 != 0:          #verify success before committing results
                        print 'Iteration ' + str(i) + 'failed  with error code' + str(p2) + '\n'
                        continue
                #fp = open(self.xform + '_data.txt', 'a')
                #fp.write(str(i[0])+ ','+ str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(self.fdata['arith']) + ',' + str(self.fdata['mem']) + ',' + str(cost)+'\n')
                #fp.close()
                csvwriter.writerow([i[0],self.fdata['depth'] , self.fdata['stms'], str(self.fdata['arith']), str(self.fdata['mem']), i[1], i[2], i[3], elapsed])

                #clean
                #os.remove('xform.script')     #remove chill script
                #os.remove('rose_'+self.cfile['name'])
                #os.remove('tmp.bin')

            csvout.close()

        elif self.xform == 'unroll':
            csvwriter.writerow(['input', 'depth', 'stms', 'arithmetic', 'memory', 'unrolled loop', 'unrolled stmt', 'unroll size', 'cost'])                    #headers


            for i in itr:
                self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=0,
                                              transformations=[['unroll', i[2], i[1], i[3]]])

                p = Popen('chill xform.script'.split(), stdout=PIPE, stderr=PIPE)
                p.communicate()         #wait for the returncode
                #verify p.returncode, if 0, success. Else invalid, cost = -INF
                if p.returncode != 0 :
                    elapsed = -1000.0
                else:
                    #compile run rose_*.c and get execution time
                    p1 = Popen(('gcc rose_'+self.cfile['name']+' -o tmp.bin').split(), stdout=PIPE, stderr=PIPE)
                    p1.communicate()
                    if  p1.returncode != 0:
                        print 'compiling transformed code failed with error code '+ str(p1.returncode) + '\n'
                        continue

                    start = time.clock()
                    p2 = subprocess.call('./tmp.bin')
                    elapsed = time.clock()*1000 - start*1000        #in ms
                    if p2 != 0:          #verify success before committing results
                        print 'Iteration ' + str(i) + 'failed  with error code' + str(p2) + '\n'
                        continue

                csvwriter.writerow([i[0],self.fdata['depth'] , self.fdata['stms'], str(self.fdata['arith']), str(self.fdata['mem']), i[1], i[2], i[3], elapsed])

                    #clean
                    #os.remove() #chill script
                    #os.remove('rose_'+self.cfile['name'])
                    #os.remove('tmp.bin')

        elif self.xform == 'peel':
            pass

        elif self.xform == 'scale':
            pass

        elif self.xform == 'shift_to':
            pass
        else:
            print 'error: unknown transform \''+self.xform+'\'\n'
            exit(-1)

        #fp.close()



