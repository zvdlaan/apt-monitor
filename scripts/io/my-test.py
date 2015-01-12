#!/usr/bin/python

import BBB_ADC as ADC

ADC.Initialize()
print ADC.GetValueRaw( 'P9-40' )


