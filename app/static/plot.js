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
		console.log(table);


		var data = google.visualization.arrayToDataTable(table);


		var options = {
			title: metric_name,
			legend: { position: 'bottom' }
		};

		var div = document.createElement("div");
                div.setAttribute('id', i); // and make sure myclass has some styles in css
                document.body.appendChild(div);

                var chart = new google.visualization.LineChart(
                	document.getElementById(i));
                chart.draw(data, options);
                
    }
}




    