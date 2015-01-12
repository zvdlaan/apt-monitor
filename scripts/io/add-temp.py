#!/usr/bin/python

import MySQLdb
import BBB_ADC as ADC

ADC.Initialize()

millivolts = ADC.GetValueMillivolts( 'P9-40' )

temp_c = (float(millivolts) - 500) / 10
temp_f = (temp_c * 9/5) + 32

print temp_f


db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="bone", # your username
                      passwd="307592", # your password
                      db="DB_VandyApt") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( NOW(), (%s) )", temp_f )

db.commit()

cur.close()
db.close()

