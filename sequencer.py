'''
1. generate sequences
2. compose corresponding CHiLL script
3. call CHiLL to transform code
4. Run transformed code
5. Evaluate performance (time)
'''
import opentuner
import argparse
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
import re

argparser = argparse.ArgumentParser(parents=opentuner.argparsers())
argparser.add_argument('xform', help = 'transformation')
argparser.add_argument('path', help = 'C file path')
argparser.add_argument('procedure', help='procedure name')

class Sequencer(MeasurementInterface):

    def __init__(self, *pargs, **kwargs):
        super(Sequencer, self).__init__(*pargs, **kwargs)
        self.xform = args.xform
        fn = args.path.split('/')[-1]
        dir = re.sub(fn, '', args.path)
        self.cfile = {'path': args.path, 'name': fn, 'dir': dir, 'procedure': args.procedure}
        self.cg = CHiLLCodeGen()

    def manipulator(self):

        cm = ConfigurationManipulator()
        fdata = Scanner(self.cfile['path']).scan_loop()

        if self.xform == 'tile':
            cm.add_parameter(EnumParameter('size',[0,4,8,16,32]))
            cm.add_parameter(IntegerParameter('ll', 1, fdata['depth'])) #consider tiling for each loop
        elif self.xform == 'unroll':
            cm.add_parameter(EnumParameter('unroll',['unroll0','unroll4','unroll8','unroll16']))
        #add other xforms we allow

        else:
            print 'error: unknown transform \''+ self.xform +'\'\n'
            exit(-1)
        return cm

    def execute(self, config):
        #consumes a configuration, generates and compile code, return SUCCESS/FAILURE

        if self.xform == 'tile':
            #TODO: build a valid transformation and generate corresponding CHiLL script
            self.cg.generate_chill_script(self.cfile['path'], self.cfile['procedure'], looplevel1=0, transformations=[['tile', 0, config['ll'], config['size']]] )

            #TODO: generate code, compile, run, measure time, repeat


        RET = self.call_program('chill '+ self.cfile['dir'] +'xform.script')
        if(RET['returncode']):
            return -1e-10 #bad configuration
        cmp_result = self.call_program('gcc -O3 rose_' + self.cfile['name'] +' -o bin.tmp')
        assert cmp_result['returncode'] == 0

        start = time.clock()*1000
        #TODO: generate random input and test
        run_result = self.call_program('./bin.tmp')
        elapsed = time.clock()*1000 - start
        assert run_result['returncode'] == 0
        os.remove('xform.script')
        os.remove('rose_'+self.cfile['name'])
        os.remove('bin.tmp')

        return elapsed

    def run(self,desired_result,input,limit):
        cfg = desired_result.configuration.data
        ret_val = self.execute(cfg)
        return Result(time = ret_val)

    def save_final_config(self, config):
        self.manipulator().save_to_file(config.data, 'chill_final_config.json')


if __name__ == '__main__':
    opentuner.init_logging()
    args = argparser.parse_args()
    Sequencer.main(args)
