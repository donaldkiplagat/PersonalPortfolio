$(document).ready(function(){
  $("#nav-home").click(function(){
    $("#skills").hide();
    $("#contact").hide();
    $("#projects").hide();
    $("#home").show();
  });
  $("#nav-skills").click(function(){
    $("#home").hide();
    $("#projects").hide();
    $("#contact").hide();
    $("#skills").show();
  });
  $("#nav-projects").click(function(){
    $("#home").hide();
    $("#skills").hide();
    $("#contact").hide();
    $("#projects").show();
  });
  $("#nav-contact").click(function(){
    $("#home").hide();
    $("#skills").hide();
    $("#projects").hide();
    $("#contact").show();
  });


});
