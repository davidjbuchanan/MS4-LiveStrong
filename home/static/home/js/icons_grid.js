$(document).ready(function() {
    $("#overlay_1").mouseenter(function() {               
        $("#overlay_1a").css("background-color", "rgba(0,0,0,0.7)").css("border", "thin solid red");
        $("#overlay_1b").css("opacity", "1");
        $("#overlay_1c").css("opacity", "1");
    });
    $("#overlay_1").mouseleave(function() {
        $("#overlay_1a").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#overlay_1b").css("opacity", "0.6");
        $("#overlay_1c").css("opacity", "0.6");
    });
    $("#overlay_2").mouseenter(function() {               
        $("#overlay_2a").css("background-color", "rgba(0,0,0,0.7)").css("border", "thin solid red");
        $("#overlay_2b").css("opacity", "1");
        $("#overlay_2c").css("opacity", "1");
    });
    $("#overlay_2").mouseleave(function() {
        $("#overlay_2a").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#overlay_2b").css("opacity", "0.6");
        $("#overlay_2c").css("opacity", "0.6");
    });
    $("#overlay_3").mouseenter(function() {               
        $("#overlay_3a").css("background-color", "rgba(0,0,0,0.7)").css("border", "thin solid red");
        $("#overlay_3b").css("opacity", "1");
        $("#overlay_3c").css("opacity", "1");
    });
    $("#overlay_3").mouseleave(function() {
        $("#overlay_3a").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#overlay_3b").css("opacity", "0.6");
        $("#overlay_3c").css("opacity", "0.6");
    });
});