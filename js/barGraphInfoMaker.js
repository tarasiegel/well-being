function drawMarriageGraph(femaleAge, maleAge, babyAge){
	var canvas = document.getElementById('chartContainer');
	    if (canvas.getContext) {
	      	var context = canvas.getContext('2d');
	      	context.clearRect(0,0,200,200);
	      	var f = femaleAge*3;
	      	var m = maleAge*3;
	      	var b = babyAge*3;
	      	var nationalf = 26.85*3;
			var nationalm = 28.62*3;
			var nationalb = 25*3;
	      	context.fillStyle = "rgb(113,155,217)";
			context.fillRect(10,100-f,20,f);
	      	context.fillStyle = "rgb(162,177,201)"; 
			context.fillRect(30,100-nationalf,20,nationalf);
			//female
			context.fillStyle = "rgb(221,141,228)";
			context.fillRect(60,100-m,20,m);
			context.fillStyle = "rgb(171,165,171)";
			context.fillRect(80,100-nationalm,20,nationalm);
			//baby
			context.fillStyle = "rgb(230,200,135)";
			context.fillRect(110,100-b,20,b);
			context.fillStyle = "rgb(193,190,183)";
			context.fillRect(130,100-nationalb,20,nationalb);	
	    } 
	    else {
	      alert("This page uses HTML 5 to render correctly. Other browsers may not see anything.");
	    }

	    $("#legend1").html('Average age at 1st marriage: Male')
	    $("#legend2").html('Average age at 1st marriage: Female')
	    $("#legend3").html('Average age at 1st baby')
	    $("#legend4").html('National Average')
	    $("#legendColor1").css("background","rgb(113,155,217)");
	    $("#legendColor2").css("background","rgb(221,141,228)");
	    $("#legendColor3").css("background","rgb(230,200,135)");
	    $("#legendColor4").css("background","rgb(193,190,183)");
	    $("#legendNum1").html(femaleAge+"yrs").css("color","rgb(113,155,217)");
	    $("#legendNum2").html(maleAge+"yrs").css("color","rgb(221,141,228)");
	    $("#legendNum3").html(babyAge+"yrs").css("color","rgb(230,200,135)");
  }

function drawJobGraph(allunemployment, unemployment, employment){	
	var canvas = document.getElementById('chartContainer');
	    if (canvas.getContext) {
	      var context = canvas.getContext('2d');
	      
	      context.fillStyle = "rgb(150,29,28)";
	      context.fillRect (10,10,280,280);var context = canvas.getContext('2d');
	      	context.clearRect(0,0,200,200);
	      	var a = allunemployment;
	      	var u = unemployment;
	      	var e = employment;
	      	var nationalAllUnemployment = 9.090196078;
			var nationalUnemployment = 8.592156863;
			var nationalEmployment = 75.21960784;
			
	      	context.fillStyle = "rgb(203,166,94)";
			context.fillRect(10,100-a,20,a);
	      	context.fillStyle = "rgb(193,190,183)";
			context.fillRect(30,100-nationalAllUnemployment,20,nationalAllUnemployment);
		
			context.fillStyle = "rgb(174,62,83)";
			context.fillRect(60,100-u,20,u);
			context.fillStyle = "rgb(148,133,136)";
			context.fillRect(80,100-nationalUnemployment,20,nationalUnemployment);
	
			context.fillStyle = "rgb(113,180,113)";
			context.fillRect(110,100-e,20,e);
			context.fillStyle = "rgb(166,177,166)";
			context.fillRect(130,100-nationalEmployment,20,nationalEmployment);	
	    } 
	    else {
	      // put code for browsers that don’t support canvas here
	      alert("This page uses HTML 5 to render correctly. Other browsers may not see anything.");
	    }

	    $("#legend1").html('Percent Unemployment rate: All')
	    $("#legend2").html('Percent Unemployment rate: Age 25-44')
	    $("#legend3").html('Percent Employment rate: Age 25-44')
	    $("#legend4").html('National Average')
	    $("#legendColor1").css("background","rgb(203,166,94)");
	    $("#legendColor2").css("background","rgb(174,62,83)");
	    $("#legendColor3").css("background","rgb(113,180,113)");
	    $("#legendColor4").css("background","rgb(193,190,183)");
	    $("#legendNum1").html(allunemployment+"%").css("color","rgb(203,166,94)");
	    $("#legendNum2").html(unemployment+"%").css("color","rgb(174,62,83)");
	    $("#legendNum3").html(employment+"%").css("color","rgb(113,180,113)");
  }

  function drawSchoolGraph(highSchool, bachelors){	
	var canvas = document.getElementById('chartContainer');
	    if (canvas.getContext) {
	      var context = canvas.getContext('2d');
	      
	      context.fillStyle = "rgb(150,29,28)";
	      context.fillRect (10,10,280,280);var context = canvas.getContext('2d');
	      	context.clearRect(0,0,200,200);
	      	var hs = highSchool;
	      	var ba = bachelors;
	      	var nationalHS = 88.01176471;
	      	var nationalBA = 28.9254902;
			
	      	context.fillStyle = "rgb(108,185,180)";
			context.fillRect(10,100-hs,20,hs);
	      	context.fillStyle = "rgb(177,189,188)";
			context.fillRect(30,100-nationalHS,20,nationalHS);
		
			context.fillStyle = "rgb(144,96,231)";
			context.fillRect(60,100-ba,20,ba);
			context.fillStyle = "rgb(168,164,176)";
			context.fillRect(80,100-nationalBA,20,nationalBA);

	    } 
	    else {
	      // put code for browsers that don’t support canvas here
	      alert("This page uses HTML 5 to render correctly. Other browsers may not see anything.");
	    }

	    $("#legend1").html("Percent High School Graduate")
	    $("#legend2").html("Percent Bachelor's Degree or higher")
	    $("#legend3").html('National Average')
	    $("#legend4").html("(Hover over a state to see its stats)")
	    $("#legendColor1").css("background","rgb(108,185,180)");
	    $("#legendColor2").css("background","rgb(144,96,231)");
	    $("#legendColor3").css("background","rgb(168,164,176)");
	    $("#legendColor4").css("background","#fff");
	    $("#legendNum1").html(highSchool+"%").css("color","rgb(108,185,180)");
	    $("#legendNum2").html(bachelors+"%").css("color","rgb(144,96,231)");
	    $("#legendNum3").html("");
  }