#!/usr/bin/python

import MySQLdb
import BBB_ADC as ADC
import time

ADC.Initialize()

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="bone", # your username
                      passwd="307592", # your password
                      db="DB_VandyApt") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()


while True:	
	millivolts = ADC.GetValueMillivolts( 'P9-40' )
	temp_c = (float(millivolts) - 500) / 10
	temp_f = (temp_c * 9/5) + 32
	cur.execute("UPDATE InstantaneousAmbientRoomTemp SET Temp=(%s) WHERE Id=1", temp_f )
	db.commit()
	time.sleep(1)	

cur.close()
db.close()

