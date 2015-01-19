#!/usr/bin/python

import BBB_PWM as PWM

#PWM.InitializePin('P8_13')

PWM.SetFrequency('P8_13', 60)
print PWM.GetFrequency('P8_13')
print "duty_min: " + str(float(.03*PWM.GetPeriod('P8_13')))+ "ns"
print "duty_max: " + str(float(.145*PWM.GetPeriod('P8_13'))) + "ns"

