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



$(function(){
  //open birthday
  $("#birthd").click(function(){
    $("#first").slideUp();
    $("#fbirthd").slideDown();
	});

  //open anniversary
  $("#anni").click(function(){
    $("#first").slideUp();
    $("#fanni").slideDown();
  });

  //open get well
  $("#gwell").click(function(){
    $("#first").slideUp();
    $("#fgwell").slideDown();
  });

  //open congradulations
  $("#congra").click(function(){
    $("#first").slideUp();
    $("#fcongra").slideDown();
  });

  //open graduation
  $("#grad").click(function(){
    $("#first").slideUp();
    $("#fgrad").slideDown();
  });

  //open birth
  $("#birth").click(function(){
    $("#first").slideUp();
    $("#fbirth").slideDown();
  });

  //open christmas
  $("#xmas").click(function(){
    $("#first").slideUp();
    $("#fxmas").slideDown();
  });

  //open valintines
  $("#valin").click(function(){
    $("#first").slideUp();
    $("#fvalin").slideDown();
  });

  //open holidays
  $("#holi").click(function(){
    $("#first").slideUp();
    $("#fholi").slideDown();
  });

  //open random
  $("#rand").click(function(){
    $("#first").slideUp();
    $("#frand").slideDown();
  });
});
