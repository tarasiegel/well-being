var stateData = [];
var marriageData = [];
var jobData = [];
var schoolData = [];

//STATE INFORMATION
function State(id, name, a, b, c, d, e, f, g, h, i, j, k) {
  this.id = id;
  this.name = name;
  this.tid0 = a;
  this.tid1 = b;
  this.tid2 = c;
  this.tid3 = d;
  this.tid4 = e;
}

function ajaxWordsData(){
  $.ajax({
      type: "GET",
      url: "csv/stateTopicWords.csv",
      dataType: "text",
      async: false,
      success: function(data) { processWordData(data);}
   });
}

function processWordData(data) {
  var stateDataTemp = [];
  var allTextLines = data.split(/\r\n|\n|\r/);
  var headers = allTextLines[0].split(',');
  for (var i = 1; i < allTextLines.length; i++) {
    var stateInfo = allTextLines[i].split(',');
    var state = new State(stateInfo[0], stateInfo[1], stateInfo[2], stateInfo[3], stateInfo[4], stateInfo[5], stateInfo[6]);
    stateDataTemp.push(state);
  }
  stateData = stateDataTemp;
  console.log(stateData)
}

function getStateData(){
  return stateData;
}

//MARRIAGE INFORMATION
function MarriageAge(id, stateName, male, female, baby) {
  this.id = id;
  this.name = stateName;
  this.maleAge = male;
  this.femaleAge = female;
  this.babyAge = baby;
}

var nationalFemaleAgeMarriage = 26.85;
var nationalMaleAgeMarriage = 28.62;
var nationalFemaleBabyAge = 25;

function ajaxMarriageAgeData(){
  $.ajax({
      type: "GET",
      url: "csv/avgAgeFamily.csv",
      dataType: "text",
      async: false,
      success: function(data) { processMarriageData(data);}
   });
}

function processMarriageData(data) {
  var allTextLines = data.split(/\r\n|\n|\r/);
  var headers = allTextLines[0].split(',');
  for (var i = 1; i < allTextLines.length; i++) {
    var marriageInfo = allTextLines[i].split(',');
    var state = new MarriageAge(marriageInfo[0], marriageInfo[1], marriageInfo[2], marriageInfo[3], marriageInfo[4]);
    marriageData.push(state);
  }
}

function getMarriageData(){
  return marriageData;
}

//JOB INFORMATION
function JobObject(id, stateName, unemploymentA, unemployment, employment) {
  this.id = id;
  this.name = stateName;
  this.unemploymentAll = unemploymentA;
  this.unemploymentYoung= unemployment;
  this.employmentYoung = employment;
}

function ajaxJobData(){
  $.ajax({
      type: "GET",
      url: "csv/jobData.csv",
      dataType: "text",
      async: false,
      success: function(data) { processJobData(data);}
   });
}

function processJobData(data) {
  var allTextLines = data.split(/\r\n|\n|\r/);
  var headers = allTextLines[0].split(',');
  for (var i = 1; i < allTextLines.length; i++) {
    var jobInfo = allTextLines[i].split(',');
    var state = new JobObject(jobInfo[0], jobInfo[1], jobInfo[2], jobInfo[3], jobInfo[4]);
    jobData.push(state);
  }
}

function getJobData(){
  return jobData;
}

//SCHOOL INFORMATION
function SchoolObject(id, stateName, a, b) {
  this.id = id;
  this.name = stateName;
  this.hs = a;
  this.bachelors = b;
}

function ajaxSchoolData(){
  $.ajax({
      type: "GET",
      url: "csv/schoolGraduationData.csv",
      dataType: "text",
      async: false,
      success: function(data) { processSchoolData(data);}
   });
}

function processSchoolData(data) {
  var allTextLines = data.split(/\r\n|\n|\r/);
  var headers = allTextLines[0].split(',');
  for (var i = 1; i < allTextLines.length; i++) {
    var schoolInfo = allTextLines[i].split(',');
    var state = new SchoolObject(schoolInfo[0], schoolInfo[1], schoolInfo[2], schoolInfo[3]);
    schoolData.push(state);
  }
}

function getSchoolData(){
  return schoolData;
}




