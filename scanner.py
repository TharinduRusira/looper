'''
scans the code and extract loop nest information
1. depth
2. loop bounds
3. input sizes
...
...

'''
import re

class Scanner:
    def __init__(self, file):
        self.file = file

    def scan_loop(self):

        fp = open(self.file,'r')
        d = 0                       #number of loops
        loop_ids = []
        stms = 0                    #number of stms
        limits= []
        stmt_ready = False
        rbracks = 0
        lbracks = 0

        while True:
            line = fp.readline()
            print line
            if line == '':                                  #EOF
                break

            if 'for' in line:
                #extract the loop control logic
                
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
                if lbracks >=2 and d>0:                     #discounting 1 for the function's { and outermost loop's {
                    stmt_ready = True
                lbracks = lbracks + 1
                continue

            if '}' in line:
                rbracks = rbracks + 1
                if lbracks == rbracks:              #braces are balanced
                    stmt_ready = False
                else:
                    stmt_ready = True
                continue
            if (line.endswith(';') and stmt_ready): #any other line
                #stms.append(line.strip())              we don't need actual statements
                print 'heeyaa'
                stms = stms + 1
                stmt_ready = False

            print 'lbracks='+ str(lbracks) + '\trbracks='+str(rbracks)+'\n'

        return {"depth":d, 'stms':stms, 'loops':loop_ids}
