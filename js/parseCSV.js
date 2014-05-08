function getCSVData(){
	var result = [];
	$(document).ready(function() {
	    $.ajax({
	        type: "GET",
	        url: "sampleWords.csv",
	        async: false,
	        dataType: "text",
	        success: function(data) {result = processData(data);}
	     });
	});
	return result;
}

function County(id, a, b, c, d, e, f, g, h, i, j, k) {
	this.id = id;
	this.tid0 = a;
	this.tid1 = b;
	this.tid2 = c;
	this.tid3 = d;
	this.tid4 = e;
	this.tid5 = f;
	this.tid6 = g;
	this.tid7 = h;
	this.tid8 = i;
	this.tid9 = j;
	this.tid10 = k;
}

function processData(data) {
	var allTextLines = data.split(/\r\n|\n|\r/);
	var headers = allTextLines[0].split(',');
	var countyData = [];

	for (var i = 1; i < allTextLines.length; i++) {
		var countyInfo = allTextLines[i].split(',');
		var county = new County(countyInfo[0], countyInfo[1], countyInfo[2], countyInfo[3], countyInfo[4], countyInfo[5], countyInfo[6], countyInfo[7], countyInfo[8], countyInfo[9], countyInfo[10], countyInfo[11]);
		countyData.push(county);
	}
	return countyData;
}

