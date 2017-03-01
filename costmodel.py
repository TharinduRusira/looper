'''
defines a simple cost model to evaluate the nature of loop statements
will consider arithmetic operations, memory accesses etc.
'''

def cost(mem, arith, tot_lines):
    #return cost
    #mc = mem['memops']/tot_lines
    mc = 1
    ac = (arith['add']+arith['sub']+8*arith['mul']+10*arith['div']+10*arith['mod'])/tot_lines    #weighted arithmetic cost per line

    return {'memcost':mc, 'arithcost': ac}