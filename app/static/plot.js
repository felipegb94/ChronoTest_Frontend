var first = true;
var charts = [];


function drawChart(run_name) {
    var run_names = []; // Number of machines + name
    var runs = []; //  2D Array containing. Cols =  Number of machines, Rows = Run
            
    if(first){
        run_names = tests.run_names;

        /* Load runs for each machine */
        for(var i = 0; i < run_names.length; i++){
            run = run_names[i];
            runs.push(tests[run]);
        }

        /* Load metric names */
        for(metric in runs[0][0].metrics){
            metrics.push(metric);
        }  
    }
    else{
        run_name = run_name.getAttribute('id');
        run_names.push(run_name);
        runs.push(tests[run_name]);
    }

	plot(metrics, run_names, runs);

}


function plot(metrics, run_names, runs){
	for(var i = 0; i < metrics.length; i++){

		metric_name = metrics[i];
		table = [['x']];

		for(var j = 0; j < run_names.length; j++){
			table[0].push(run_names[j]);
		}

		for(var j = 0; j < runs[0].length; j++){
			date = new Date(runs[0][j].timestamp);
			row = [date];

			for(var k = 0; k < runs.length; k++){
				try{
					data_point = runs[k][j].metrics[metric_name];
				}catch(TypeError){
					console.log(runs[k][j]);
					data_point = 0;
				}
				row.push(data_point);
			}
			table.push(row);
		}

		var data = google.visualization.arrayToDataTable(table);
		var options = { 
						title: metric_name, 
						legend: { position: 'bottom' },
						backgroundColor: '#F6F6F6',
						series: { 0: {color: '#e2431e'},
								  1: {color: '#1c91c0'},	
								  2: {color: '#f1ca3a'}	
								}
					   };

		if(first){
			var div = document.createElement("div");
        	div.setAttribute('id', metric_name); // and make sure myclass has some styles in css
        	div.setAttribute('class', 'metric');
        	document.getElementById('metrics').appendChild(div);

        	var chart = new google.visualization.LineChart(
        									document.getElementById(metric_name));
        	chart.draw(data, options);
        	charts.push(chart);
    	}
    	else{
    		var div = document.getElementById(metric_name);
    		charts[i].draw(data, options)

    	}

	}
	if(first){
		first = false;
	}
}






