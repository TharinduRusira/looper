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
import time
import os


class Sequencer(MeasurementInterface):

    def __init__(self, xform, fn, p):
        self.xform = xform
        self.cfile = {'path':fn, 'name': '{}'.format(fn.split('/')[-1]) , 'procedure': p}
        self.cg = CHiLLCodeGen()

    def config(self):

        cm = ConfigurationManipulator()
        fdata = Scanner(self.cfile['name'])

        if self.xform is 'tile':
            cm.add_parameter(EnumParameter('size',[0,4,8,16,32]))
            cm.add_parameter(IntegerParameter('ll', 1, fdata['depth'])) #consider tiling for each loop
        elif self.xform is 'unroll':
            cm.add_parameter(EnumParameter('unroll',['unroll0','unroll4','unroll8','unroll16']))
        #add other xforms we allow

        else:
            print 'error: unknown transform \''+ self.xform +' \'\n'

    def execute(self, config):
        #consumes a configuration, generates and compile code, return SUCCESS/FAILURE

        if self.xform is 'tile':
            #TODO: build a valid transformation and generate corresponding CHiLL script
            self.cg.generate_chill_script(self.cfile['name'], self.cfile['procedure'], looplevel1=0, transformations=['tile', 0, cfg['ll'], cfg['tile']] )

            #TODO: generate code, compile, run, measure time, repeat


        RET = self.call_program('chill xform.script')
        if(RET):
            return -1e-10 #bad configuration
        cmp_result = self.call_program('gcc -O3 rose_' + self.cfile['name'] +' -o bin.tmp')
        assert cmp_result['returncode'] == 0

        start = time.clock()*1000
        run_result = self.call_program('./bin.tmp')
        elapsed = time.clock()*1000 - start

        os.remove('xform.chill')
        os.remove('bin.tmp')


        return elapsed

    def run(self,desired_result,input,limit):
        cfg = desired_result.configuration.data
        ret_val = self.execute(cfg)
        return Result(time = ret_val)

    def save_final_config(self, config):
        pass

