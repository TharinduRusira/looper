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
import operator

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

        nests = []              #number of loop nests, and their depths. nests[i] = depth of i-th nest
        nest = 0                #current loop nest
        newNest = True

        inside = False
        linenumber = 0
        num_itrs = []           #number of iterations for each loop level
        num_itrs_per_nest = []
        symbols = {}            #hold #define values
        vars = []               #hold variable names
        mem = {'ref':0}                #global accesses, cache/registry accesses, memory reuse info
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

            if line.strip().startswith('//'):
                continue

            if '#define' in line:                               #currently, symbols are only read via #define
                l = line.split(' ')
                try:
                    symbols.update({l[1].strip(): int(l[2])})
                except ValueError:
                    continue

            if  line.strip().startswith('float'):
                if '=' in line:
                    first = (re.split(r'=', line)[0]).strip()
                    vars.append(first.split()[1].strip())
                else:
                    #a line that declares float data. Assume format float A[N][N]
                    #assume one declaration for a line
                    first = (re.split(r'\[', line))[0]
                    #now remove the data type 'float'
                    vars.append(first.split()[1])


            if 'for' in line:
                #extract the loop control logic
                inside = True
                d = d + 1  # new loop level
                if newNest:
                    nest +=1
                    nests.append(0)
                    newNest = False
                    num_itrs_per_nest.append(0)

                nests[nest-1] += 1

                stmt_ready = True
                gotStart = False
                gotEnd = False

                l = re.split(r'\(|\)', line.strip())        #ideally this should break the line into 3 parts, l[1] has the loop control data
                l1 = l[1].split(';')                        #again, 3 pieces
                idx = l1[0].split('=')[0]
                if idx not in loop_ids:
                    loop_ids.append(idx.strip())
                start = l1[0].split('=')[1]

                if start.strip() in symbols:              #if terminate condition is a defined variable
                    start = symbols[start.strip()]
                elif start.strip() in loop_ids:
                    start = math.log(max(symbols.iteritems(), key=operator.itemgetter(1))[1]) #a heuristic approximation of the log2 of the largest symbol
                else:
                    #start bound is most likely an expression including either a symbol or another loop bound
                    for symbol in symbols:              #more complicated end conditions such as N-1, ...
                        if symbol in re.split(r'\+|-|\*', start.strip()):
                            start = symbols[symbol]
                            gotStart = True
                            break
                    if not gotStart:
                        for var in loop_ids:
                            if var in re.split(r'\+|-|\*', start.strip()):
                                start = math.log(max(symbols.iteritems(), key=operator.itemgetter(1))[1]) #a heuristic approximation of the log2 of the largest symbol
                                break

                l2 = re.split(r'<=|>=|<|>|',l1[1])
                end = l2[1]

                if end.strip() in symbols:              #if terminate condition is a defined variable
                    end = symbols[end.strip()]
                elif end.strip() in loop_ids:
                    end = math.log(max(symbols.iteritems(), key=operator.itemgetter(1))[1])  # a heuristic approximation of the log2 of the largest symbol
                else:
                    for symbol in symbols:
                        if symbol in re.split(r'\+|-|\*', end.strip()):
                            end = symbols[symbol]
                            print end
                            gotEnd = True
                            break
                    if not gotEnd:
                        for var in loop_ids:
                            if var in re.split(r'\+|-|\*', end.strip()):
                                end = math.log(max(symbols.iteritems(), key=operator.itemgetter(1))[1]) #a heuristic approximation of the log2 of the largest symbol
                                break

                limits.append((idx, start,end))
                                                            # TODO: extract loop bounds and infer if they are > 0
                step = l1[2]
                if '++' in step or '--' in step:
                    step_size = 1
                else:
                    #i = i + x
                    rhs = (step.split('=')[1]).strip()
                    step_size = int(re.split(r'\+|-|\*|/',rhs)[-1])
                #print start, end, step_size
                x = math.fabs(math.ceil((float(end) - float(start))/step_size))
                if x == 0.0:
                    x = 1 # 0 messes up the multiplication later on
                num_itrs.append(x)
                num_itrs_per_nest[nest-1] +=x
                #continue

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
                    inside = False                 #leaving the loop nest
                    newNest = True
                else:
                    stmt_ready = True
                continue

            if line.strip().endswith(';'): #any other line
                if stmt_ready:
                    stms = stms + 1
                    stmt_ready = False
                    stmt_list.append([])
                if inside:
                    (stmt_list[stms-1]).append(line.strip())
                    #extract computational and memory info
                    add = add + line.count('+')
                    sub = sub + line.count('-')
                    mul = mul + line.count('*')
                    div = div + line.count('/')
                    mod = mod + line.count('%')

                    for v in vars:
                        if v in line:
                            mem['ref'] += line.count(v)
                continue


        tot_itrs = 1
        for loop in range(len(num_itrs)):                #limits = [(idx, start, end)]
            tot_itrs *= num_itrs[loop]       # end - start

        #print symbols
        #print limits
        #print 'Nests=', nests, 'depth=', d, 'nests=', nest
        #print num_itrs_per_nest
        #print 'iterations='+ str(tot_itrs)
        arith = {'add': add, 'sub': sub, 'mul': mul, 'div': div, 'mod': mod}
        c = cost(mem= mem, arith=arith, tot_lines=linenumber, tot_itrs=tot_itrs)
        return {"depth":d, 'stms':stms, 'loops':loop_ids, 'lines': linenumber,
                'stms_list': stmt_list, 'mem':c['memcost'], 'arith': c['arithcost']}
