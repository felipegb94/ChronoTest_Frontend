var first = true;
var charts = [];
function plot(metrics, run_names, runs){
	
	for(var i = 0; i < metrics.length; i++){
		metric_name = metrics[i];
		table = [['x']];

		for(var j = 0; j < run_names.length; j++){
			table[0].push(run_names[j]);
		}

		for(var j = 0; j < runs[0].length; j++){
			row = [j];
			for(var k = 0; k < runs.length; k++){
				data_point = runs[k][j].metrics[metric_name];
				row.push(data_point);
			}
			table.push(row);
		}

		var data = google.visualization.arrayToDataTable(table);
		var options = { title: metric_name, legend: { position: 'bottom' }};

		if(first){

			var div = document.createElement("div");
        	div.setAttribute('id', metric_name); // and make sure myclass has some styles in css
        	div.setAttribute('class', 'metric');
        	document.body.appendChild(div);

        	var chart = new google.visualization.LineChart(
        									document.getElementById(metric_name));
        	chart.draw(data, options);
        	charts.push(chart);
    	}
    	else{
    		console.log("Second try");
    		var div = document.getElementById(metric_name);
    		charts[i].draw(data, options)

    	}

	}
	if(first){
		first = false;
	}
}






