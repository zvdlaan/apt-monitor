# -*- coding: utf-8 -*-

"""This module contains the main handler of the application.
"""

import web
import json
import collections
import models.temp_model
import subprocess

render = web.template.render('views')


class IndexHandler(object):
	def GET(self):
		return 'Home page'


class TempsHandler(object):
	def GET(self):
		return render.base()

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
			tempData_list.append( collections.OrderedDict( [ ('Id', item.Id), ('Month' , item.Month), ('Day', item.Day), ('Year', item.Year), ('Time', str(item.Time) ), ('Timestamp', item.Timestamp ), ('Temp',float(item.Temp) ) ] ) )

		if tempStats[0]['NumRowsInQuery'] == 0:
			tempData_dict = {'results': tempData_list, 'min': tempStats[0]['Min'] , 'max': tempStats[0]['Max'], 'mean': tempStats[0]['Mean'], 'stddev': tempStats[0]['Stddev'] }
		else:
			tempData_dict = {'results': tempData_list, 'min': float(tempStats[0]['Min']) , 'max': float(tempStats[0]['Max']), 'mean': float(tempStats[0]['Mean']), 'stddev': float(tempStats[0]['Stddev']) }

		return json.dumps( tempData_dict, indent=4 )


class CurrentTempHandler(object):
	def GET(self):
		web.header('Content-Type', 'application/json')

		tempData = {'temp': float(models.temp_model.get_current_temp()[0].Temp) }

		return json.dumps( tempData )


class WebcamHandler(object):
	def GET(self):
		#process = subprocess.Popen(['sudo','/home/zvdlaan/Desktop/start-webcam.sh'])
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
				process = subprocess.Popen(['sudo','/var/www/scripts/start-webcam.sh'])
				returnData['webcam'] = 'started'
			elif data.webcam == "stop":
				process = subprocess.Popen(['sudo','/var/www/scripts/stop-webcam.sh'])
				process.communicate()
				if process.returncode == 0:
					returnData['webcam'] = 'stopped'
				else:
					returnData['webcam'] = 'error: webcam off command did not execute properly. The webcam may have already been off'
			else:
				returnData['webcam'] = 'error: webcam form-data value must be start or stop'

		return json.dumps( returnData )
