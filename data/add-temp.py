import MySQLdb
import random

temp_f = random.randint(69, 74)

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
