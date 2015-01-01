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
						items.push( {c:[{v: new Date(value.Timestamp * 1000) }, {v: value.Temp} ]} );
					 });
				 } else {
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
				'width': 700,
				'height': 500
			};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.LineChart(document.getElementById(idOfSelectedTab + '-chart-div'));
			chart.draw(data, options);
		}
	});
});

function closeIt()
{
/*	return "Any string value here forces a dialog box to \n" +
	"appear before closing the window.";*/
}
window.onbeforeunload = closeIt;
