'''
scans the code and extract loop nest information
1. depth
2. loop bounds
3. input sizes
...
...

'''

class Scanner:
    def __init__(self, file):
        self.file = file

    def scan_loop(self):
        fp = open(self.file,'r')
        d = 0
        for line in fp:
            if 'for' in line:
                d = d+1     #will work for simple loop nests
                #TODO: extract loop bounds and infer if they are > 0

        return {"depth":d}
