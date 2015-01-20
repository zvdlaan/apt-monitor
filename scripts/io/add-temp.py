#!/usr/bin/python

import MySQLdb
import BBB_ADC as ADC
import requests


# get inside temp
ADC.Initialize()

millivolts = ADC.GetValueMillivolts( 'P9-40' )

temp_c = (float(millivolts) - 500) / 10
temp_f = (temp_c * 9/5) + 32

inside_temp_f = temp_f
print 'Inside: ' + str(inside_temp_f)

# get outside temp
url = "http://api.openweathermap.org/data/2.5/weather?q=holland,us&units=imperial"
r = requests.get(url).json()

main = r['main']
outside_temp_f = main['temp']

print 'Outside: ' + str(outside_temp_f)


db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="bone", # your username
                      passwd="307592", # your password
                      db="DB_VandyApt") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("""INSERT INTO Temperature (MeasuredTime, InsideTemp, OutsideTemp)
	    VALUES( NOW(), %s, %s )""", (inside_temp_f, outside_temp_f) )

db.commit()

cur.close()
db.close()

