#!/usr/bin/python

'''
import subprocess 

#script, inputPin = argv
#script = argv

#acceptableInputPins = [ 'AIN0', 'AIN1', 'AIN11', 'AIN13', 'AIN14', 'AIN15', 'AIN16', 'AIN7']

# make sure adc driver is setup
#setupAdc = subprocess.call( 'echo cape-bone-iio > /sys/devices/bone_capemgr.*/slots')

# find 'AIN 1' 

#command = "find /sys/ -name '*AIN1'"  # the shell command
#process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
#fileNameAIN1 = process.communicate()[0]

adcFile = open("/home/WONDERLAN/zach.vanderlaan/Desktop/dummyfile")
value = adcFile.read()

	# millivolts = reading * 1800  # 1.8V reference = 1800 mV
    #temp_c = (millivolts - 500) / 10
    
temp_c = (float(value) - 500) / 10
temp_f = (temp_c * 9/5) + 32

print temp_f
'''

import BBB_ADC as ADC

ADC.Initialize()
print ADC.GetValueRaw( 'P9-40' )
print ADC.GetValueScaled( 'P9-40' )
print ADC.GetValueMillivolts( 'P9-40' )


