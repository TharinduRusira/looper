'''
defines a simple cost model to evaluate the nature of loop statements
will consider arithmetic operations, memory accesses etc.
'''

def cost(mem, arith, tot_lines, tot_itrs):
    #return cost
    #mc = mem['memops']/tot_lines
    mc = 1
    ac = float(arith['add']+arith['sub']+8*arith['mul']+10*arith['div']+10*arith['mod'])/float(tot_lines)    #weighted arithmetic cost per line

    return {'memcost':mc, 'arithcost': ac}