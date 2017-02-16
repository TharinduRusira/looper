from loopmap import *
from loopnest import *

def test1_layer():
    try:
        l = Layer("not of Loopnest type")
    except TypeError:
        print 'TypeError\n'