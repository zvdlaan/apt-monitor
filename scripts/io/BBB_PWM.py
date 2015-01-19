import sys
import subprocess 
import string


acceptablePwmPins = ['P8_13', 'P8_19', 'P9_14', 'P9_16']
availableOperations = ['run', 'duty', 'period', 'frequency', 'polarity']

def RunCommand( command ):
	process = subprocess.Popen( command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )	
	response = process.communicate()
	returnDict = { 'returncode': process.returncode, 'output':response[0].rstrip(), 'error': response[1].rstrip() }
	return returnDict

def InitializePin( outputPin, period=None, duty=None, polarity=None ):
	if outputPin not in acceptablePwmPins:
		print outputPin + ' is an invalid pwm pin. Acceptable pins are ' + ', '.join(acceptablePwmPins)
	else:	
		findSlotsLocation = RunCommand( """sudo find /sys/devices/bone_capemgr.*/ -name "slots" """ )
		if findSlotsLocation['returncode'] != 0:
			print "Could not find the path to .../bone_capemgr.*/slots"	
		else:
			turnOnPwmCommand = """sudo sh -c "echo 'am33xx_pwm' > """ + findSlotsLocation['output'] + """" """ 
			turnOnPwm = RunCommand( turnOnPwmCommand )
			if turnOnPwm['returncode'] != 0:
				print "PWM ports could not be enabled.  " + turnOnPwmCommand + " command failed." 
			else:				
				setupOutputPinCommand = """sudo sh -c "echo 'bone_pwm_""" + outputPin + """' > """ +  findSlotsLocation['output'] + """" """ 
				setupOutputPin = RunCommand( setupOutputPinCommand )
				if setupOutputPin['returncode'] != 1:
					print "Pin " + outputpin + " could not be enabled. " + setupOutputPinCommand + " command failed."
				else:
					SetRun( outputPin, 0)
					"""if period is None:
						SetPeriod(outputPin, 500000)
					else:
						SetPeriod(outputPin, period)
					if duty is None:
						SetDuty(outputPin, 0)
					else:
						SetDuty(outputPin, duty)
					if polarity is None:
						SetPolarity(outputPin, 1)
					else:
						SetPolarity(outputPin, polarity)"""
					SetRun( outputPin, 1)				
								
					print "PWM driver and pin " + outputPin + " enabled"
					
			
	
def SetRun( outputPin, value ):	  
	if outputPin not in acceptablePwmPins:
		print outputPin + ' is an invalid pwm pin. Acceptable pins are ' + ', '.join(acceptablePwmPins)
	else:
		if value not in [0,1]:
			print 'run value must be 0 or 1'
		else:	
			findRunCmd = """find /sys/devices/ocp.3/pwm_test_""" + outputPin + """.*/run"""
                	findRun = RunCommand( findRunCmd )
 			if findRun['returncode'] != 0:
                        	print 'Command: ' + findRunCmd + ' failed'
                	else:				
				runCommand = """sudo sh -c "echo '""" + str(value) + """' > """ + findRun['output'] + """" """
				run = RunCommand( runCommand )
				if run['returncode'] != 0:
					print 'Command: ' + runCommand + ' failed'
				else:				
					print '"run" set to ' + str(value)

def GetValue( outputPin, operation ):
	if outputPin not in acceptablePwmPins:
                print outputPin + ' is an invalid pwm pin. Acceptable pins are ' + ', '.join(acceptablePwmPins)
        else:
		if type not in availableOperations:
			print 'can only get values for ', '.join(availableOperations)
		else:
			findOperationCmd = """find /sys/devices/ocp.3/pwm_test_""" + outputPin + """.*/""" + operation
	                findOperation = RunCommand( findOperationCmd )
	       		if findOperation['returncode'] != 0:
	                	print 'Command: ' + findOperationCmd + ' failed' 
	            	else:
				operationValueCommand = """sudo cat """ + findOperation['output']
				operationValue = RunCommand( operationValueCommand )
	                      	if operationValue['returncode'] != 0:
	                        	print 'Command: ' + operationValueCommand + ' failed'
	                	else:
	                        	return int( operationValue['output'] )
	return -1
"""							
def GetRun( outputPin ):	  
	if outputPin not in acceptablePwmPins:
		print outputPin + ' is an invalid pwm pin. Acceptable pins are ' + ', '.join(acceptablePwmPins)
	else:	
		findRunCmd = """find /sys/devices/ocp.3/pwm_test_""" + outputPin + """.*/run"""
                findRun = RunCommand( findRunCmd )
       		if findRun['returncode'] != 0:
                	print 'Command: ' + findRunCmd + ' failed' 
            	else:
			runValueCommand = """sudo cat """ + findRun['output']
			runValue = RunCommand( runValueCommand )
                      	if runValue['returncode'] != 0:
                        	print 'Command: ' + runValueCommand + ' failed'
                	else:
                        	return int( runValue['output'] )
	return -1

"""		
def GetRun( outputPin ):	  
	return GetValue( outputPin, 'run')


