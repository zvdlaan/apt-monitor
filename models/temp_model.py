import web

db = web.database(dbn='mysql', db='DB_VandyApt', user='bone', pw='307592' )

def get_temps_all():
    return db.select('Temperature', what='Id, MONTH(MeasuredTime) AS Month, DAY(MeasuredTime) AS Day, YEAR(MeasuredTime) AS Year, TIME(MeasuredTime) AS Time, UNIX_TIMESTAMP(MeasuredTime) AS Timestamp, InsideTemp, OutsideTemp',  order='Id');

def get_temps_all_stats():
	return db.query('SELECT COUNT(*) AS NumRowsInQuery, MIN(InsideTemp) AS InsideMin, MAX(InsideTemp) AS InsideMax, AVG(InsideTemp) As InsideMean, STD(InsideTemp) AS InsideStddev FROM Temperature');

def get_temps_day():
    return db.select('Temperature', what='Id, MONTH(MeasuredTime) AS Month, DAY(MeasuredTime) AS Day, YEAR(MeasuredTime) AS Year, TIME(MeasuredTime) AS Time, UNIX_TIMESTAMP(MeasuredTime) AS Timestamp, InsideTemp, OutsideTemp', where='MeasuredTime >= DATE(NOW())', order='Id');
    
def get_temps_day_stats():
	return db.query('SELECT COUNT(*) AS NumRowsInQuery, MIN(InsideTemp) AS InsideMin, MAX(InsideTemp) AS InsideMax, AVG(InsideTemp) As InsideMean, STD(InsideTemp) AS InsideStddev FROM Temperature WHERE MeasuredTime >= DATE(NOW())');    
    
def get_temps_week():
    return db.select('Temperature', what='Id, MONTH(MeasuredTime) AS Month, DAY(MeasuredTime) AS Day, YEAR(MeasuredTime) AS Year, TIME(MeasuredTime) AS Time, UNIX_TIMESTAMP(MeasuredTime) AS Timestamp, InsideTemp, OutsideTemp', where='MeasuredTime >= DATE(NOW()) - INTERVAL 1 WEEK', order='Id');

def get_temps_week_stats():
	return db.query('SELECT COUNT(*) AS NumRowsInQuery, MIN(InsideTemp) AS InsideMin, MAX(InsideTemp) AS InsideMax, AVG(InsideTemp) As InsideMean, STD(InsideTemp) AS InsideStddev FROM Temperature WHERE MeasuredTime >= DATE(NOW()) - INTERVAL 1 WEEK');    

def get_temps_month():
    return db.select('Temperature', what='Id, MONTH(MeasuredTime) AS Month, DAY(MeasuredTime) AS Day, YEAR(MeasuredTime) AS Year, TIME(MeasuredTime) AS Time, UNIX_TIMESTAMP(MeasuredTime) AS Timestamp, InsideTemp, OutsideTemp', where='MeasuredTime >= DATE(NOW()) - INTERVAL 1 MONTH', order='Id');

def get_temps_month_stats():
	return db.query('SELECT COUNT(*) AS NumRowsInQuery, MIN(InsideTemp) AS InsideMin, MAX(InsideTemp) AS InsideMax, AVG(InsideTemp) As InsideMean, STD(InsideTemp) AS InsideStddev FROM Temperature WHERE MeasuredTime >= DATE(NOW()) - INTERVAL 1 MONTH');    

def get_current_temp():
	return db.select('InstantaneousTemperature', what='InsideTemp' );
