
paceOptions = {
  ajax: true,
  elements: {
    selectors: ['.g']
  }
};

var width = 800,
	height = 500,
	centered;

ajaxWordsData();
ajaxMarriageAgeData();
ajaxJobData();
ajaxSchoolData();
var stateData = getStateData();
var marriageData = getMarriageData();
var jobData = getJobData();
var schoolData = getSchoolData();
var startingState;


var quantize = d3.scale.quantize()
  .domain([0.0001, 0.0002])
  .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));  

var quantizeMarriage = d3.scale.quantize()
  .domain([23, 32])
  .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));  

var projection = d3.geo.albersUsa()
 .scale(1070)
 .translate([width / 2, height / 2]);

var path = d3.geo.path()
	.projection(projection); //or projection

var svg = d3.select("#content").append("svg")
	.attr("width", width)
	.attr("height", height);

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([0, 0])
  .html(function(d) {
    changeInfoBox(d);
    return stateToolTip(d);
  });

var currentOption = 0;

function stateToolTip(d){
  var currentState = $.grep(marriageData, function(c) { return c.id == d.id });
  var stateId = d.properties.name;
  return "<div style='padding: 10px; text-align: center;'><span style='line-height:0.8em; font-size: 14px'>"+stateId+"</span></div>";
}

function changeInfoBox(d){
  if (currentOption < 2) {
    schoolInfo(d);
  }
  else if (currentOption == 2) {
    jobInfo(d);
  }
  else {
     marriageInfo(d);
  }
}

function marriageInfo(d){
  var currentState = $.grep(marriageData, function(c) { return c.id == d.id });
  var stateId = d.properties.name;
  var maleAge = currentState[0].maleAge;
  var femaleAge = currentState[0].femaleAge;
  var babyAge = currentState[0].babyAge;

  drawMarriageGraph(femaleAge, maleAge, babyAge);
}

function jobInfo(d){
  var currentState = $.grep(jobData, function(c) { return c.id == d.id });
  var stateId = d.properties.name;
  var unemploymentA = currentState[0].unemploymentAll;
  var unemployment = currentState[0].unemploymentYoung;
  var employment = currentState[0].employmentYoung;

  drawJobGraph(unemploymentA, unemployment, employment);
}

function schoolInfo(d){
  var currentState = $.grep(schoolData, function(c) { return c.id == d.id });
  var stateId = d.properties.name;
  var hs = currentState[0].hs;
  var b = currentState[0].bachelors;

  drawSchoolGraph(hs,b);
}

svg.append("rect")
  	.attr("class", "background")
  	.attr("width", width)
  	.attr("height", height)
  	.on("click", clicked);

svg.call(tip);

var g = svg.append("g");

d3.json("https://dl.dropboxusercontent.com/u/23549740/us-state.json", function(error, us) {
 // console.log(us);
  g.append("g")
    .attr("class", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter().append("path")
      .attr("class", function(d) { 
        if (d.id == 01){
          startingState = d;
          changeInfoBox(startingState);
        }
        return decideColor(d.id, "option"); })
      .attr("id", function(d) { return d.id})
      .attr("d", path)
      .on("click", clicked)
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);


  g.append("path")
      .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
      .attr("class", "stateBorders")
      .attr("d", path);
});


function changeMap(option) {
  //console.log("Starting to update map");
  $("path:not(.stateBorders)").each(function(){
    var idName = $(this).attr('id');
    var color = decideColor(idName, option);
    var oldClass = $(this).attr('class');
    d3.select(this).attr("class", color);
    currentOption = option;
   });
  
 // console.log("Done updating map");
}

$(function() {
    $( "#slider" ).slider({
      value:0,
      min: 0,
      max: 4,
      step: 1,
      slide: function( event, ui ) {
        changeMap(ui.value);
        changeInfoBox(startingState);
      }
    });
  });


function decideColor(id, option) {
  var currentstate = $.grep(stateData, function(c) { return c.id == id });
  var numToQuantize = 0;
  if (currentstate.length == 1) {
    if (option == 0) { numToQuantize = currentstate[0].tid0; }
    else if (option == 1) { numToQuantize = currentstate[0].tid1; }
    else if (option == 2) { numToQuantize = currentstate[0].tid2; }
    else if (option == 3) { numToQuantize = currentstate[0].tid3; }
    else if (option == 4) { numToQuantize = currentstate[0].tid4; }
    else { numToQuantize = currentstate[0].tid0; }
  }
  return quantize(numToQuantize)
}


function clicked(d) {
  var x, y, k;

  if (d && centered !== d) {
    var centroid = path.centroid(d);
    x = centroid[0];
    y = centroid[1];
    k = 4;
    centered = d;
  } else {
    x = width / 2;
    y = height / 2;
    k = 1;
    centered = null;
  }

  g.selectAll("path")
      .classed(centered && function(d) { return d === centered; });

  g.transition()
      .duration(750)
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
      .style("stroke-width", 1.5 / k + "px");
}


$(document).ready(function(){
  $('.moreInfo').click(function(event){
  event.preventDefault();
  $('.overlay').show();
  });
   
  $('.overlayClose').click(function(){
  $('.overlay').hide();
  });
   
  $('.overlay').click(function(){
      $('.overlay').hide();
  })
  $('.overlayContent').click(function(){
      return false;
  });

});
