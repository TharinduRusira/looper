'''
defines a simple cost model to evaluate the nature of loop statements
will consider arithmetic operations, memory accesses etc.
'''

def cost(mem, arith, tot_lines):
    #return cost
    mc = mem/tot_lines
    ac = arith/tot_lines    #TODO: weight arithmetic operations and compute weighted average

    return {'memcost':mc, 'arithcost': ac}