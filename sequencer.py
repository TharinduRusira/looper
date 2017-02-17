'''
1. generate sequences
2. compose corresponding CHiLL script
3. call CHiLL to transform code
4. Run transformed code
5. Evaluate performance (time)
'''

from opentuner import *
from opentuner import MeasurementInterface
from opentuner import Result
from opentuner import EnumParameter
from opentuner import IntegerParameter
from codegen import *
from transform import *
from scanner import *

class Sequencer(MeasurementInterface):

    def __init__(self, xform, fn, p):
        self.xform = xform
        self.cfile = {'name':fn, 'procedure': p}
        self.cg = CHiLLCodeGen()

    def config(self):

        cm = ConfigurationManipulator()
        fdata = Scanner(self.cfile['name'])

        if self.xform is 'tile':
            cm.add_parameter(EnumParameter('tile',['noop','tile8','tile16','tile32']))
            cm.add_parameter(IntegerParameter('ll', 1, fdata['depth'])) #consider tiling for each loop
        elif self.xform is 'unroll':
            cm.add_parameter(EnumParameter('unroll',['noop','unroll4','unroll8','unroll16']))
        #add other xforms we allow

        else:
            print 'error: unknown transform \''+ self.xform +' \'\n'


    def run(self,desired_result,input,limit):
        cfg = desired_result.configuration.data
        if self.xform is 'tile':
            #TODO: build a valid transformation and generate corresponding CHiLL script
            cg.generate_chill_script(self.cfile['name'], self.cfile['procedure'], cfg['ll'], transformations=[] )

            #TODO: generate code, compile, run, measure time, repeat


    def save_final_config(self, config):
        pass

