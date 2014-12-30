
--CREATE DATABASE DB_VandyApt;

DROP TABLE IF EXISTS AmbientRoomTemp;

CREATE TABLE AmbientRoomTemp
(
	Id INT NOT NULL AUTO_INCREMENT,
	MeasuredTime TIMESTAMP,
	Temp DECIMAL(4,1),
	PRIMARY KEY (Id)
);

CREATE TABLE InstantaneousAmbientRoomTemp
(
	Id INT NOT NULL AUTO_INCREMENT,
	Temp DECIMAL(4,1),
	PRIMARY KEY (Id)
);

-- Day
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 00:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 01:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 02:00:00' , 76 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 03:00:00' , 76 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 04:00:00' , 76 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-29 05:00:00' , 76 );


--Week
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 00:00:00' , 71 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 01:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 02:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 03:00:00' , 72 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 04:00:00' , 68 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 05:00:00' , 69);
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 06:00:00' , 70 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 07:00:00' , 71 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 08:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 09:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 10:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 11:00:00' , 78 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 12:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-28 13:00:00' , 80 );


--Month
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 00:00:00' , 71 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 01:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 02:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 03:00:00' , 72 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 04:00:00' , 68 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 05:00:00' , 69);
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 06:00:00' , 70 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 07:00:00' , 71 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 08:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 09:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 10:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 11:00:00' , 78 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 12:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-17 13:00:00' , 80 );


--Max
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-12-04 00:00:00' , 71 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-11-07 01:00:00' , 74 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-10-08 02:00:00' , 75 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2014-09-04 03:00:00' , 72 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2013-12-10 04:00:00' , 68 );
INSERT INTO AmbientRoomTemp (MeasuredTime, Temp) VALUES( '2012-01-11 05:00:00' , 69);

COMMIT;


