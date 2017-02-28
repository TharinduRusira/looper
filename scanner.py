'''
scans the code and extract loop nest information
1. depth
2. loop bounds
3. input sizes
...
...

'''
import re
from costmodel import *

class Scanner:
    def __init__(self, file):
        self.file = file

    def scan_loop(self):

        fp = open(self.file,'r')
        d = 0                       #number of loops
        loop_ids = []
        stms = 0                    #number of stms
        stmt_list = []
        limits= []
        stmt_ready = False
        rbracks = 0
        lbracks = 0
        inside = False
        linenumber = 0
        mem = {}                #global accesses, cache/registry accesses, memory reuse info
        arith = {}              #+, - , *, /, %,

        while True:
            line = fp.readline()

            if line == '':                                  #EOF
                break
            linenumber = linenumber + 1  # line number

            if line.strip() == '\n':            #empty line
                continue

            if 'for' in line:
                #extract the loop control logic
                inside = True
                d = d + 1  # new loop level
                stmt_ready = True

                l = re.split(r'\(|\)', line.strip())        #ideally this should break the line into 3 parts, l[1] has the loop control data
                l1 = l[1].split(';')                        #again, 3 pieces
                idx = l1[0].split('=')[0]
                if idx not in loop_ids:
                    loop_ids.append(idx)
                start = l1[0].split('=')[1]
                l2 = re.split(r'<|>|<=|>=',l1[1])
                end = l2[1]
                limits.append((idx, start,end))
                                                            # TODO: extract loop bounds and infer if they are > 0
                continue

            if '{' in line:
                if inside and d>0:
                    lbracks = lbracks + 1
                    stmt_ready = True
                continue

            if '}' in line:
                if inside:
                    rbracks = rbracks + 1
                if lbracks == rbracks:              #braces are balanced
                    stmt_ready = False
                    inside = False                  #leaving the loop nest
                else:
                    stmt_ready = True
                continue

            if line.strip().endswith(';'): #any other line
                if stmt_ready:
                    stms = stms + 1
                    stmt_ready = False
                    stmt_list.append([])
                if stms > 0 and inside:
                    (stmt_list[stms-1]).append(line.strip())

                    #extract computational and memory info
                    add = line.count('+')
                    sub = line.count('-')
                    mul = line.count('*')
                    div = line.count('/')
                    mod = line.count('%')
                    arith.update({'add':add, 'sub':sub, 'mul':mul, 'div':div, 'mod':mod})

                continue

        c = cost(mem= mem, arith=arith, tot_lines=linenumber)
        return {"depth":d, 'stms':stms, 'loops':loop_ids, 'lines': linenumber,
                'stms_list': stmt_list, 'mem':c['memcost'], 'arith': c['arithcost']}
