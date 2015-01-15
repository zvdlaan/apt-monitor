#!/usr/bin/python

import BBB_ADC as ADC

ADC.Initialize()

millivolts = ADC.GetValueMillivolts( 'P9-40' )

temp_c = (float(millivolts) - 500) / 10
temp_f = (temp_c * 9/5) + 32

print temp_f


