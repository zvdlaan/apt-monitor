
DROP TABLE IF EXISTS Temperature;
DROP TABLE IF EXISTS InstantaneousTemperature;

CREATE TABLE Temperature
(
	Id INT NOT NULL AUTO_INCREMENT,
	MeasuredTime DATETIME,
	InsideTemp DECIMAL(4,1),
	OutsideTemp DECIMAL(4,1),
	PRIMARY KEY (Id)
);

CREATE TABLE InstantaneousTemperature
(
	Id INT NOT NULL AUTO_INCREMENT,
	InsideTemp DECIMAL(4,1),
	PRIMARY KEY (Id)
);

INSERT INTO InstantaneousTemperature VALUES (1, 73.2);

INSERT INTO Temperature (MeasuredTime, Temp) VALUES( '2014-12-31 00:00:00' , 74 );
INSERT INTO Temperature (MeasuredTime, Temp) VALUES( '2014-12-31 01:00:00' , 75 );

COMMIT;
