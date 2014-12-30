jQuery(document).ready(function () {
	 var tempDataBaseURL = "http://localhost/tempData";	
	  
	 var updateCurrentTemp = function () {
 	 	jQuery.getJSON(tempDataBaseURL + '/current', function (data) { 
			 document.getElementById('current-temp').innerHTML = 'Current Temp: ' + String(data.temp);
		})
		.fail(function () {
			alert("error");
		});
		setTimeout(updateCurrentTemp, 1000);
	 };	 
	 updateCurrentTemp();	 
	 
	 var tempDataBaseURL = "http://localhost/tempData";		 
	 jQuery('.tabs .tab-links a').on('click', function (e) {
		
		var currentAttrValue = jQuery(this).attr('href');
	
		var idOfSelectedTab = jQuery('.tabs ' + currentAttrValue).attr('id') 				 
	 
		var tempDataFullURL = tempDataBaseURL + '?time_period=' + idOfSelectedTab;
		
		var items = [];					 
		jQuery.getJSON(tempDataFullURL, function (data) {
			 
			 jQuery.each(data, function (key, val) {
				 if (key == "results") {
					 jQuery.each(val, function (index, value) {
						 items.push( {c:[{v: new Date(value.Year, value.Month - 1, value.Day, 0, 30, 00) }, {v: value.Temp} ]} );					 
						 // alert( "Id: " + value.Id + ", Time: " + value.Time + ", Temp: " + value.Temp ); 
					 });
				 } 
				 else {
					 if( val != null)
					 {
						document.getElementById(idOfSelectedTab + "-" + key).innerHTML =key + ":\t\t" + val;
					 }                    
				 }
			 });
			 google.load('visualization', '1.0', {'packages': ['corechart'], "callback" : drawChart });			 
		 })
			 .fail(function () {
			  alert("error");
		 });		 
		 
		// Show/Hide Tabs
		jQuery('.tabs ' + currentAttrValue).show().siblings().hide();

		// Change/remove current tab to active
		jQuery(this).parent('li').addClass('active').siblings().removeClass('active');

		e.preventDefault();
		
		
		function drawChart() {
		// Create the data table.
			
			var myRows = [{c:[{v: new Date(2014, 2, 28, 0, 30, 00) },
						   {v: 74.2}
					  ]},
					   {c:[{v: new Date(2014, 2, 28, 1, 30, 00) },
						   {v: 80.1}
					  ]},
					   {c:[{v: new Date(2014, 2, 28, 2, 30, 00) },
						   {v: 76.0}
					  ]}
				]		
			
			var mydataObject = 
			{
				cols: [{id: 'date', label: 'Time', type: 'datetime'},
						   {id: 'temp', label: 'Indoor Temp', type: 'number'}
				],
				rows: items	 // eventually put items
			}
			
			var data = new google.visualization.DataTable( mydataObject );

			// Set chart options
			var options = {
				'title': 'Temperature Monitoring',
				'curveType': 'function',
				'vAxis': {'title':'Temp (deg F)', 'minValue':65},
				'hAxis': {'title':'Time', 'slantedTextAngle': 45, 'slantedText': true, },
				'width': 700,
				'height': 500
			};
			
			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.LineChart(document.getElementById(idOfSelectedTab + '-chart-div'));
			chart.draw(data, options);
		}			 		
	}); 	 
});   
