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
import math

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
        num_itrs = []           #number of iterations for each loop level
        symbols = {}            #hold #define values
        vars = {}               #hold variable names
        mem = {}                #global accesses, cache/registry accesses, memory reuse info
        arith = {}              #+, - , *, /, %,
        add = 0
        sub = 0
        mul = 0
        div = 0
        mod = 0

        while True:
            line = fp.readline()

            if line == '':                                  #EOF
                break
            linenumber = linenumber + 1  # line number

            if line.strip() == '\n':            #empty line
                continue

            if '#define' in line:                               #currently, symbols are only read via #define
                l = line.split(' ')
                symbols.update({l[1].strip(): int(l[2])})

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

                if end.strip() in symbols:
                    end = symbols[end.strip()]

                limits.append((idx, start,end))
                                                            # TODO: extract loop bounds and infer if they are > 0
                step = l1[2]
                if '++' in step or '--' in step:
                    step_size = 1
                else:
                    #i = i + x
                    rhs = (step.split('=')[1]).strip()
                    step_size = int(re.split(r'\+|-|\*|/',rhs)[-1])
                num_itrs.append(math.ceil((int(end) - int(start))/step_size))

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
                    add = add + line.count('+')
                    sub = sub + line.count('-')
                    mul = mul + line.count('*')
                    div = div + line.count('/')
                    mod = mod + line.count('%')
                    arith.update({'add':add, 'sub':sub, 'mul':mul, 'div':div, 'mod':mod})
                continue


        c = cost(mem= mem, arith=arith, tot_lines=linenumber)
        return {"depth":d, 'stms':stms, 'loops':loop_ids, 'lines': linenumber,
                'stms_list': stmt_list, 'mem':c['memcost'], 'arith': c['arithcost']}
