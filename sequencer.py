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
        loop_range=[]
        stms_range = []
        itrs = []

        if self.xform == 'tile':
            amount_range = [4,8,16,32,64]
        elif self.xform == 'unroll':
            amount_range = [4, 8, 16, 32, 64]
        else:                                       #change later as necessary
            amount_range = [4, 8, 16, 32, 64]

        for n in range(len(self.fdata['loop_nests'])):
            loop_range.append(range(1,self.fdata['loop_nests'][n]+1 ))             # num loops in the n-th nest
            stms_range.append(range(0,self.fdata['stmt_nest'][n]))             # num stms in the n-th nest

            itrs.append(list(itertools.product(loop_range[n],stms_range[n], amount_range)))      #len(nests) number of iterators

        #print loop_range
        #print stms_range
        #print itrs

        return itrs

    def run(self, itrs):

        csvout = open('data/data_'+self.xform+'_'+self.cfile['name'].split('.c')[0]+'.csv','a+')
        csvwriter = csv.writer(csvout, delimiter=',')
        csvreader = csv.reader(csvout)

        l = None
        n = 0                       #current nest

        if self.xform == 'tile':

            for line in csvreader:
                l = line
                break

            if l is None:
                csvwriter.writerow(['nests', 'stms', 'arithmetic', 'memory', 'tiled nest', 'tiled loop', 'tiled stmt', 'tile size',
                         'cost'])  # headers
            for itr in itrs:
                for i in itr:
                    self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=n,
                                                  transformations=[['tile', i[1], i[0], i[2]]])                             #generate CHiLL script
                    p = Popen('chill xform.script'.split(), stdout=PIPE, stderr=PIPE)                                       #transform code
                    p.communicate()         #wait for the returncode
                    #verify p.returncode, if 0, success. Else invalid, cost = -INF

                    print p.returncode
                    if p.returncode != 0 :
                        print 'invalid!'
                        elapsed = -1000.0
                    else:
                        #compile run rose_*.c and get execution time
                        p1 = Popen(('gcc rose_'+self.cfile['name']+' -o tmp.bin').split(), stdout=PIPE, stderr=PIPE)
                        p1.communicate()

                        if  p1.returncode != 0:
                            print 'compiling transformed code failed with error code '+ str(p1.returncode) + '\n'
                            continue

                        start = time.clock()
                        p2 = Popen('./tmp.bin', stdout=PIPE, stderr=PIPE)
                        elapsed = time.clock()*1000 - start*1000        #in ms
                        p2.communicate()
                        if p2.returncode != 0:          #verify success before committing results
                            print 'Iteration ' + str(i) + ' failed  with error code ' + str(p2.returncode) + '\n'
                            continue

                    #fp = open(self.xform + '_data.txt', 'a')
                    #fp.write(str(i[0])+ ','+ str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(self.fdata['arith']) + ',' + str(self.fdata['mem']) + ',' + str(cost)+'\n')
                    #fp.close()
                    csvwriter.writerow([self.fdata['loop_nests'] , self.fdata['stmt_nest'], str(self.fdata['arith']), str(self.fdata['mem']), n, i[0], i[1], i[2], elapsed])

                n += 1          #go to next loop nest
                    #clean
                    #os.remove('xform.script')     #remove chill script
                    #os.remove('rose_'+self.cfile['name'])
                    #os.remove('tmp.bin')
            csvout.close()

        elif self.xform == 'unroll':
            for line in csvreader:
                l = line
                break
            if l is None:
                csvwriter.writerow(['nests', 'stms', 'arithmetic', 'memory', 'unrolled nest', 'unrolled loop', 'unrolled stmt',
                         'unroll size', 'cost'])  # headers
            for itr in itrs:
                for i in itr:
                    self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=n,
                                                  transformations=[['unroll', i[1], i[0], i[2]]])

                    p = Popen('chill xform.script'.split(), stdout=PIPE, stderr=PIPE)
                    p.communicate()         #wait for the returncode
                    #verify p.returncode, if 0, success. Else invalid, cost = -INF
                    print p.returncode
                    if p.returncode != 0 :
                        print 'invalid'
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

                    csvwriter.writerow([self.fdata['loop_nests'] , self.fdata['stmt_nest'], str(self.fdata['arith']), str(self.fdata['mem']), n, i[0], i[1], i[2], elapsed])

                n += 1

                    #clean
                    #os.remove() #chill script
                    #os.remove('rose_'+self.cfile['name'])
                    #os.remove('tmp.bin')
            csvout.close()

        elif self.xform == 'peel':
            for line in csvreader:
                l = line
                break
            if l is None:
                csvwriter.writerow(['nests', 'stms', 'arithmetic', 'memory', 'peeled nest' ,'peeled loop', 'peeled stmt',
                         'peel amount', 'cost'])  # headers
            for itr in itrs:
                for i in itr:
                    self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=n,
                                                  transformations=[['peel', i[1], i[0], i[2]]])

                    p = Popen('chill xform.script'.split(), stdout=PIPE, stderr=PIPE)
                    p.communicate()         #wait for the returncode
                    #verify p.returncode, if 0, success. Else invalid, cost = -INF
                    print p.returncode

                    if p.returncode != 0 :
                        print 'invalid'
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

                    csvwriter.writerow([self.fdata['loop_nests'] , self.fdata['stmt_nest'], str(self.fdata['arith']), str(self.fdata['mem']), n, i[0], i[1], i[2], elapsed])

                n += 1

            csvout.close()

        elif self.xform == 'scale':
            pass

        elif self.xform == 'shift_to':
            pass
        else:
            print 'error: unknown transform \''+self.xform+'\'\n'
            exit(-1)

        #fp.close()



