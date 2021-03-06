# -*- coding: utf-8 -*-

"""This module contains the main handler of the application.
"""

import web
import json
import collections
import models.temp_model
import subprocess

#--------------------
# Initialize PWM pin
import sys
sys.path.insert(0, '/var/www/vandy-apt/scripts/io')
import BBB_PWM as PWM
#---------------------------


render = web.template.render('views')


class IndexHandler(object):
	def GET(self):
		return render.index()


class TempsHandler(object):
	def GET(self):
		return render.temps()

class TempDataHandler(object):
	def GET(self):
		web.header('Content-Type', 'application/json')
		params = web.input( time_period='all' )

		if params.time_period == 'day':
			tempData = models.temp_model.get_temps_day()
			tempStats = list(models.temp_model.get_temps_day_stats())
		elif params.time_period == 'week':
			tempData = models.temp_model.get_temps_week()
			tempStats = list(models.temp_model.get_temps_week_stats())
		elif params.time_period == 'month':
			tempData = models.temp_model.get_temps_month()
			tempStats = list(models.temp_model.get_temps_month_stats())
		elif params.time_period == 'all':
			tempData = models.temp_model.get_temps_all()
			tempStats = list(models.temp_model.get_temps_all_stats())

		tempData_list = []

		for item in tempData:
			tempData_list.append( collections.OrderedDict( [ ('Id', item.Id), ('Month' , item.Month), ('Day', item.Day), ('Year', item.Year), ('Time', str(item.Time) ), ('Timestamp', item.Timestamp ), ('InsideTemp',float(item.InsideTemp) ), ('OutsideTemp',float(item.OutsideTemp) ) ] ) )
		
		if tempStats[0]['NumRowsInQuery'] == 0:
			tempData_dict = {'results': tempData_list, 'inside-min': tempStats[0]['InsideMin'] , 'inside-max': tempStats[0]['InsideMax'], 'inside-mean': tempStats[0]['InsideMean'], 'inside-stddev': tempStats[0]['InsideStddev'], 'outside-min': tempStats[0]['OutsideMin'] , 'outside-max': tempStats[0]['OutsideMax'], 'outside-mean': tempStats[0]['OutsideMean'], 'outside-stddev': tempStats[0]['OutsideStddev'] }
		else:
			tempData_dict = {'results': tempData_list, 'inside-min': float(tempStats[0]['InsideMin']) , 'inside-max': float(tempStats[0]['InsideMax']), 'inside-mean': float(tempStats[0]['InsideMean']), 'inside-stddev': float(tempStats[0]['InsideStddev']), 'outside-min': float(tempStats[0]['OutsideMin']) , 'outside-max': float(tempStats[0]['OutsideMax']), 'outside-mean': float(tempStats[0]['OutsideMean']), 'outside-stddev': float(tempStats[0]['OutsideStddev']) }

		return json.dumps( tempData_dict, indent=4 )


class CurrentTempHandler(object):
	def GET(self):
		web.header('Content-Type', 'application/json')

		tempData = {'inside-temp': float(models.temp_model.get_current_temp()[0]['InsideTemp']) }

		return json.dumps( tempData )


class WebcamHandler(object):
	def GET(self):
		return render.webcam()

class BbControlHandler(object):
	def GET(self):
		return 'bbControl page'

	def POST(self):
		web.header('Content-Type', 'application/json')
		data = web.input()
		returnData = collections.OrderedDict()

		if 'webcam' in data:
			if data.webcam == "start":
				process = subprocess.Popen(['sudo','/var/www/vandy-apt/scripts/start-webcam.sh'])
				returnData['webcam'] = 'started'
			elif data.webcam == "stop":
				process = subprocess.Popen(['sudo','/var/www/vandy-apt/scripts/stop-webcam.sh'])
				process.communicate()
				if process.returncode == 0:
					returnData['webcam'] = 'stopped'
				else:
					returnData['webcam'] = 'error: webcam off command did not execute properly. The webcam may have already been off'
			else:
				returnData['webcam'] = 'error: webcam form-data value must be start or stop'

		if 'servo-angle' in data:
			try:
				servoAngleInt = int(data['servo-angle'])
				if servoAngleInt not in [0, 90, 180]:
					returnData['servo-angle'] = 'error: servo-angle value must be 0-180' 
				else:	
					pwmPin = 'P8_13'
					rc_init = PWM.InitializePin(pwmPin)
					rc_setFrequency = PWM.SetFrequency(pwmPin, 60)
					if rc_init != 0:
						returnData['servo-angle'] = 'error: problem initializing PWM pin'
					elif rc_setFrequency != 0: 
						returnData['servo-angle'] = 'error: problem setting duty cycle'
					else:
						# switched values of 0 and 180 to make 180 go clockwise
						if servoAngleInt == 0:
							duty = 2380000
						elif servoAngleInt == 90:
							duty = 1420000
						elif servoAngleInt == 180: 
							duty = 560000
						rc_setDuty = PWM.SetDuty('P8_13', duty)
						if rc_setDuty != 0:
							returnData['servo-angle'] = 'error: problem setting duty cycle'
						else:
							returnData['servo-angle'] = int(data['servo-angle'])	
				
			except ValueError:
				returnData['servo-angle'] = 'error: servo-angle value must be 0-180'
			

		return json.dumps( returnData )
