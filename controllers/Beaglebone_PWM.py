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

def GetHzFromNanoSeconds( nanoSeconds ):
	frequency = float( 1000000000 / nanoSeconds )
	return int(frequency)

def GetNanoSecondsFromHz( hz ):
	period = float( 1000000000 / hz )
	return int(period)

def InitializePin( outputPin, period=None, duty=None, polarity=None ):
	if outputPin not in acceptablePwmPins:
		print outputPin + ' is an invalid pwm pin. Acceptable pins are ' + ', '.join(acceptablePwmPins)
	else:	
		findSlotsLocation = RunCommand( """sudo find /sys/devices/bone_capemgr.*/ -name "slots" """ )
		if findSlotsLocation['returncode'] != 0:
			return "Could not find the path to .../bone_capemgr.*/slots" +  findSlotsLocation['error']	
		else:
			return "Found path to slots: " + findSlotsLocation['output']
