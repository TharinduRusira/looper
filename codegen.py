'''
Code generation for CHiLL scripts

''' 
from abc import ABCMeta, abstractmethod

keyword ={
		"IMPORT" : "from chill import *",
		"PARAN_L": "(", 
		"PARAN_R" : ")", 
		"SQR_L" : "[", 
		"SQR_R" : "]", 
		"SOURCE": "source",
		"PROCEDURE" : "procedure", 
		"LOOP" : "loop", 
		"KNOWN" : "known", 
		"P_CODE": "print_code()", 
		"P_DEP": "print_dep()", 
		"P_SPACE": "print_space()", 
		"EXIT": "exit()", 
		#"remove_dep", 
		"DELIM" : ','
		#"ORIGINAL" : 'original()',
		}


class CHiLLCodeGen(object):

	def __init__(self):
		print 'Initializing CHiLLCodeGen...'

	def generate_chill_script(self, sourcename, procedurename, looplevel1, known = None, transformations = None, printcode = False):
		script = "chill.script"

		fp = open(script,'w',0)

		if fp is None:
			print 'ERROR: opening a new CHiLL script failed...'
			exit()

		#Write mandatory fields of the script
		fp.write(keyword['IMPORT']+'\n')
		fp.write(keyword['SOURCE'] + '(\'' +sourcename +'\')\n')
		fp.write(keyword['PROCEDURE']+ '(\'' +procedurename+'\')\n')
		fp.write(keyword['LOOP'] + '(' + str(looplevel1) + ')\n')

		if known is not None:
			#write individual known statements
			#known_list = ''
			for condition in known:
				#known_list+= '\''+ condition +'\','
				fp.write(keyword['KNOWN']+keyword['PARAN_L']+ condition + keyword['PARAN_R']+'\n')
			#known_list+= '\''+known[-1]+'\''
		else: 
			print 'WARNING: No known conditions detected...'

		# insert transformations to the script

		if transformations is not None:
			i = 1  # keep track of which transformation is being processed in the current iteration
			for t in transformations:
				line = ''
				if t[0] is 'original':  # we consider original() as a transformation
					line += 'original()'
					fp.write(line + '\n')
				elif t[0] is 'distribute':
					line += 'distribute' + keyword['PARAN_L']
					# t[1] = set<int> stms
					line += keyword['SQR_L']
					for stmt in t[1][:-1]:
						line += str(stmt) + keyword['DELIM']
					line += str(t[1][-1])
					line += keyword['SQR_R'] + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2])
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'fuse':
					line += 'fuse' + keyword['PARAN_L']
					# t[1] = set<int> stms
					line += keyword['SQR_L']
					for stmt in t[1][:-1]:
						line += str(stmt) + keyword['DELIM']
					line += str(t[1][-1])
					line += keyword['SQR_R'] + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2])
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'nonsigular':
					print 'INFO: nonsingular is not yet supported...'

				elif t[0] is 'peel':
					line += 'peel' + keyword['PARAN_L']
					# t[1] = int stms
					line += str(t[1]) + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2])
					# t[3] = amount OPTIONAL
					if (len(t) == 4):
						line += keyword['DELIM'] + t[3]
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'permute':
					line += 'permute' + keyword['PARAN_L']
					# two versions of permute
					if len(t) == 2:
						line += keyword['SQR_L']
						for p in t[1][:-1]:
							line += str(p) + keyword['DELIM']
						line += str(t[1][-1])
						line += keyword['SQR_R']
						line += keyword['PARAN_R']
						fp.write(line + '\n')
					elif len(t) == 3:
						print 'INFO: \'permute\' with the second parameter is not yet supported...'
					else:
						print 'ERROR: Invalid input detected for \'perumte\'...'

				elif t[0] is 'reverse':
					line += 'reverse' + keyword['PARAN_L']
					# t[1] = set<int> stms
					line += keyword['SQR_L']
					for stmt in t[1][:-1]:
						line += str(stmt) + keyword['DELIM']
					line += str(t[1][-1])
					line += keyword['SQR_R'] + keyword['DELIM']
					# t[2] = int level
					line += str(t[2])
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'scale':
					print 'INFO: \'scale\' is not yet supported...'
				elif t[0] is 'shift':
					pass
				elif t[0] is 'shift_to':
					line += 'shift_to' + keyword['PARAN_L']
					# t[1] = int stmt
					# t[2] = int loop
					# t[3] = int amount
					line += str(t[1]) + keyword['DELIM'] + str(t[2]) + keyword['DELIM'] + str(t[3])
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'skew':
					line += 'skew' + keyword['PARAN_L']
					# t[1] = set<int> stmts
					line += keyword['SQR_L']
					for stmt in t[1][:-1]:
						line += str(stmt) + keyword['DELIM']
					line += str(t[1][-1])
					line += keyword['SQR_R'] + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2]) + keyword['DELIM']
					# t[3] = vector<int> amount
					line += keyword['SQR_L']
					for amount in t[3][:-1]:
						line += str(amount) + keyword['DELIM']
					line += str(t[3][-1]) + keyword['SQR_R']
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'split':
					line += 'split' + keyword['PARAN_L']
					# t[1] = int stmt
					line += str(t[1]) + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2]) + keyword['DELIM']
					# t[3] = expr eg "L2 < 5"
					line += '"' + t[3] + '"'  # passed as a string
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				elif t[0] is 'tile':
					line += 'tile' + keyword['PARAN_L']
					# t[1] = int stmt
					line += str(t[1]) + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2]) + keyword['DELIM']
					# t[3] = int tile_size
					line += str(t[3])
					# now check for optional arguments
					# we can handle this case later if necessary for the experiments
					line += keyword['PARAN_R']
					fp.write(line + '\n')
				elif t[0] is 'unroll':
					line += 'unroll' + keyword['PARAN_L']
					# t[1] = int stmt
					line += str(t[1]) + keyword['DELIM']
					# t[2] = int loop
					line += str(t[2]) + keyword['DELIM']
					# t[3] = int unroll_amount
					line += str(t[3])
					# t[4] = int cleanup_split_level OPTIONAL
					if (len(t) == 5):
						line += keyword['DELIM'] + str(t[4])
					line += keyword['PARAN_R']
					fp.write(line + '\n')

				else:
					print 'ERROR: No valid transformation detected...'
					fp.close()
					exit(-1)

				i = i + 1
			else:
				print 'WARNING: No transformations specified...'
				#fp.close()
				#exit(0)

		if printcode is True:
			fp.write('print_code()')

		print 'INFO: CHiLL script generated successfully...'
		fp.close()

# class CHiLLTune(MeasurementInterface):
# 	"""
# 	This is the interface class users should implement with the two mandatory functaions
# 	1. manipulator(self)
# 	2. run(self,desired_result,input,limit)
# 	"""
# 	__metaclass__ = ABCMeta
#
# 	def __init__(self):
# 		print 'Initializing CHiLLTune...'
# 		self.codegenerator = CHiLLCodeGen()
#
# 	@abstractmethod
# 	def manipulator(self):
# 		pass
#
# 	@abstractmethod
# 	def run(self,desired_result,input,limit):
# 		#super(MeasurementInterface,self).run(desired_result,input,limit)
# 		pass
#
# 	def generate_chill_scrpit(self, sourcename, procedurename, format1, looplevel1, looplevel2=None, known = None, transformations=None, printcode = False):
# 		#try:
# 		self.codegenerator.generate_chill_script(sourcename, procedurename, format1, looplevel1, looplevel2, known, transformations, printcode)
# 		#except Exception as e:
# 		#	print 'ERROR: CHiLL script generation failed...'+ str(e)