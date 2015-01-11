import MySQLdb
import random

temp_f = random.randint(68, 77)

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="DB_VandyApt") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( NOW(), (%s) )", temp_f )

db.commit()

cur.close()
db.close()
