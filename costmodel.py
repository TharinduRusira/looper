'''
defines a simple cost model to evaluate the nature of loop statements
will consider arithmetic operations, memory accesses etc.
'''

def cost(mem, arith, tot_lines, tot_itrs, nests, num_nests):
    #return cost

    mc = []         #mem cost per nest
    ac = []         #arith cost per nest

    #modify tot_itrs with nest info
    for n in range(num_nests):
        mc.append(float(mem[n]['ref']*tot_itrs[n]/tot_lines))
        ac.append(float(arith[n]['add']+arith[n]['sub']+8*arith[n]['mul']+10*arith[n]['div']+10*arith[n]['mod'])/float(tot_lines))    #weighted arithmetic cost per line

    return {'memcost':mc, 'arithcost': ac}