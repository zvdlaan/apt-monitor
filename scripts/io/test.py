#!/usr/bin/python

import BBB_PWM as PWM
import requests
#PWM.InitializePin('P8_13')

#PWM.SetFrequency('P8_13', 60)
#print PWM.GetFrequency('P8_13')
#print "duty_min: " + str(float(.03*PWM.GetPeriod('P8_13')))+ "ns"
#print "duty_max: " + str(float(.145*PWM.GetPeriod('P8_13'))) + "ns"

url = "http://api.openweathermap.org/data/2.5/weather?q=holland,us&units=imperial"
r = requests.get(url).json()

main = r['main']
temp = main['temp']

print type(temp)
