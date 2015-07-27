$("#fbirthd").slideUp();
$("#fanni").slideUp();
$("#fgwell").slideUp();
$("#fcongra").slideUp();
$("#fgrad").slideUp();
$("#fbirth").slideUp();
$("#fxmas").slideUp();
$("#fvalin").slideUp();
$("#fholi").slideUp();
$("#frand").slideUp();
$("#Home").hide();




$(function(){
  //open birthday
  $("#birthd").click(function(){
    $("#first").slideUp();
    $("#fbirthd").slideDown();
    $("#Home").slideDown();
	});

  //open anniversary
  $("#anni").click(function(){
    $("#first").slideUp();
    $("#fanni").slideDown();
    $("#Home").slideDown();
  });

  //open get well
  $("#gwell").click(function(){
    $("#first").slideUp();
    $("#fgwell").slideDown();
    $("#Home").slideDown();
  });

  //open congradulations
  $("#congra").click(function(){
    $("#first").slideUp();
    $("#fcongra").slideDown();
    $("#Home").slideDown();
  });

  //open graduation
  $("#grad").click(function(){
    $("#first").slideUp();
    $("#fgrad").slideDown();
    $("#Home").slideDown();
  });

  //open birth
  $("#birth").click(function(){
    $("#first").slideUp();
    $("#fbirth").slideDown();
    $("#Home").slideDown();
  });

  //open christmas
  $("#xmas").click(function(){
    $("#first").slideUp();
    $("#fxmas").slideDown();
    $("#Home").slideDown();
  });

  //open valintines
  $("#valin").click(function(){
    $("#first").slideUp();
    $("#fvalin").slideDown();
    $("#Home").slideDown();
  });

  //open holidays
  $("#holi").click(function(){
    $("#first").slideUp();
    $("#fholi").slideDown();
    $("#Home").slideDown();
  });

  //open random
  $("#rand").click(function(){
    $("#first").slideUp();
    $("#frand").slideDown();
    $("#Home").slideDown();
  });

  //go Home
  $("#Home").click(function(){
    $("#fbirthd").slideUp();
    $("#fanni").slideUp();
    $("#fgwell").slideUp();
    $("#fcongra").slideUp();
    $("#fgrad").slideUp();
    $("#fbirth").slideUp();
    $("#fxmas").slideUp();
    $("#fvalin").slideUp();
    $("#fholi").slideUp();
    $("#frand").slideUp();
    $("#Home").hide();
    $("#first").slideDown();
  });
});
