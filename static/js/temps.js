jQuery(document).ready(function () {
	
	jQuery.ajaxSetup({ timeout: 10000
	});
	
	 var tempDataBaseURL = "http://vandy.ydns.eu:8080/tempData";
	 var weatherQuery = 'http://api.openweathermap.org/data/2.5/weather?q=holland&units=imperial';

	 var updateCurrentTemp = function () {
 	 	jQuery.getJSON(tempDataBaseURL + '/current', function (data) {
			 document.getElementById('current-inside-temp').innerHTML = 'Inside: <strong>' + String( (data.temp).toFixed(1) ) + '&#176;F</strong>';
		})
		.fail(function () {
			document.getElementById('current-inside-temp').innerHTML = 'N/A'
		});
	
		jQuery.getJSON(weatherQuery, function (data) {
			 document.getElementById('current-outside-temp').innerHTML = 'Holland: <strong>' + String((data.main.temp).toFixed(1)) + '&#176;F</strong> (' + String(data.weather[0].description) + ')';
		})
		.fail(function () {
			document.getElementById('current-outside-temp').innerHTML = 'N/A'
		});
		
		setTimeout(updateCurrentTemp, 30000);
	 };
	
	function getData( timeOfDay ) {	
			
		var tempDataFullURL = tempDataBaseURL + '?time_period=' + timeOfDay;
		var items = [];
		jQuery.getJSON(tempDataFullURL, function (data) {

			 jQuery.each(data, function (key, val) {
				 if (key == "results") {
					 jQuery.each(val, function (index, value) {
						items.push( {c:[{v: new Date(value.Timestamp * 1000) }, {v: value.Temp} ]} );
					 });
				 } else {
					 if( val != null)
					 {
						document.getElementById(key + "-inside").innerHTML = val;
					 }
					 else
					 {
						 document.getElementById(key + "-inside").innerHTML = "";
					 }
				 }
			 });
			 google.load('visualization', '1.0', {'packages': ['corechart'], "callback" : drawChart });
		 })
			 .fail(function () {
			  alert("error");
		 });
		 
		 function drawChart() {
		// Create the data table.

			var mydataObject =
			{
				cols: [{id: 'date', label: 'Time', type: 'datetime'},
					{id: 'temp', label: 'Indoor Temp', type: 'number'}
				],
				rows: items
			}

			var data = new google.visualization.DataTable( mydataObject );
			data.sort(0);

			var now = new Date();
			var today = new Date( now.getFullYear(), now.getMonth(), now.getDate() );
			var weekAgo = new Date( today.getFullYear(), today.getMonth(), today.getDate() - 7 );
			var monthAgo =  new Date( today.getFullYear(), today.getMonth() - 1, today.getDate() );

			// Set chart options
			var options = {
				'title': 'Temperature Monitoring',
				'curveType': 'function',
				'vAxis': {'title':'Temp (deg F)', 'minValue':60, 'maxValue':80 },
				'hAxis': {'title':'Time', 'slantedTextAngle': 45, 'slantedText': true, 'viewWindowMode':'explicit', 'viewWindow': { 'max':now } },  // 'gridlines': {'count': 9},
				'width': 550,
				'height': 300
			};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.LineChart(document.getElementById('chart'));
			chart.draw(data, options);
		}	 
		 			
	}
	
	function clearAllButtons() {
		jQuery('#day').css("background-color", "#D3D3D3");
		jQuery('#week').css("background-color", "#D3D3D3");
		jQuery('#month').css("background-color", "#D3D3D3");
		jQuery('#all').css("background-color", "#D3D3D3");
	}
	
	//initialize 
	clearAllButtons();
	updateCurrentTemp();	 
	getData('day');
	
	jQuery('#day').click( function() {
		clearAllButtons();
		jQuery('#day').css("background-color", "#708D70");
		getData('day')
	});
	
	jQuery('#week').click( function() {
		clearAllButtons();
		jQuery('#week').css("background-color", "#708D70");
		getData('week')
	});
	
	jQuery('#month').click( function() {
		clearAllButtons();
		jQuery('#month').css("background-color", "#708D70");
		getData('month')
	});
	
	jQuery('#all').click( function() {
		clearAllButtons();
		jQuery('#all').css("background-color", "#708D70");
		getData('all')
	});
});
