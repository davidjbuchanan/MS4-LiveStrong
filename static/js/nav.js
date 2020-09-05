$(document).ready(function() {
    $(".navbar").mouseenter(function() {               
        this.style.setProperty( "border-bottom", "thin solid red", "important");
    });
    $(".navbar").mouseleave(function() {               
        this.style.setProperty( "border-bottom", "thin solid white", "important");
    });

    $(".jumbotron").mouseenter(function() {               
        this.style.setProperty( "border", "thin solid red", "important");
    });
    $(".jumbotron").mouseleave(function() {               
        this.style.setProperty( "border", "thin solid white", "important");
    });
    $("#alpha").mouseenter(function() {               
        $("#alpha").css("opacity", "1").css("background-color", "rgba(0,0,0,1)").css("border", "thin solid red");
        $("#one").css("background-color", "rgba(0,0,0,0.3)");
        $("#two").css("background-color", "rgba(0,0,0,0.3)");
        $("#three").css("background-color", "rgba(0,0,0,0.3)");
        $("#four").css("background-color", "rgba(0,0,0,0.3)");
    });
    $("#alpha").mouseleave(function() {
        $("#alpha").css("opacity", "0.6").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#one").css("background-color", "transparent");
        $("#two").css("background-color", "transparent");
        $("#three").css("background-color", "transparent");
        $("#four").css("background-color", "transparent");
    });
    $("#one").mouseenter(function() {
        $("#blog-options_1").css("opacity", "1");
        $("#blog-options_2").css("opacity", "1");
        $("#one").css("background-color", "rgba(0,0,0,1)").css("border", "thin solid red");
        $("#alpha").css("background-color", "rgba(0,0,0,0.3)");
        $("#two").css("background-color", "rgba(0,0,0,0.3)");
        $("#three").css("background-color", "rgba(0,0,0,0.3)");
        $("#four").css("background-color", "rgba(0,0,0,0.3)");
    });
    $("#one").mouseleave(function() {
        $("#blog-options_1").css("opacity", "0.6");
        $("#blog-options_2").css("opacity", "0.6");
        $("#one").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#alpha").css("background-color", "transparent");
        $("#two").css("background-color", "transparent");
        $("#three").css("background-color", "transparent");
        $("#four").css("background-color", "transparent");
    });
    $("#two").mouseenter(function() {
        $("#user-options_1").css("opacity", "1");
        $("#user-options_2").css("opacity", "1");
        $("#two").css("background-color", "rgba(0,0,0,1)").css("border", "thin solid red");
        $("#alpha").css("background-color", "rgba(0,0,0,0.3)");
        $("#one").css("background-color", "rgba(0,0,0,0.3)");
        $("#three").css("background-color", "rgba(0,0,0,0.3)");
        $("#four").css("background-color", "rgba(0,0,0,0.3)");
    });
    $("#two").mouseleave(function() {
        $("#user-options_1").css("opacity", "0.6");
        $("#user-options_2").css("opacity", "0.6");
        $("#two").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#alpha").css("background-color", "transparent");
        $("#one").css("background-color", "transparent");
        $("#three").css("background-color", "transparent");
        $("#four").css("background-color", "transparent");
    });
    $("#three").mouseenter(function() {
        $("#three_1").css("opacity", "1");
        $("#three_2").css("opacity", "1");
        $("#three").css("background-color", "rgba(0,0,0,1)").css("border", "thin solid red");
        $("#alpha").css("background-color", "rgba(0,0,0,0.3)");
        $("#one").css("background-color", "rgba(0,0,0,0.3)");
        $("#two").css("background-color", "rgba(0,0,0,0.3)");
        $("#four").css("background-color", "rgba(0,0,0,0.3)");
    });
    $("#three").mouseleave(function() {
        $("#three_1").css("opacity", "0.6");
        $("#three_2").css("opacity", "0.6");
        $("#three").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#alpha").css("background-color", "transparent");
        $("#one").css("background-color", "transparent");
        $("#two").css("background-color", "transparent");
        $("#four").css("background-color", "transparent");
    });
    $("#four").mouseenter(function() {
        $("#product-options_1").css("opacity", "1");
        $("#product-options_2").css("opacity", "1");
        $("#four").css("background-color", "rgba(0,0,0,1)").css("border", "thin solid red");
        $("#alpha").css("background-color", "rgba(0,0,0,0.3)");
        $("#one").css("background-color", "rgba(0,0,0,0.3)");
        $("#two").css("background-color", "rgba(0,0,0,0.3)");
        $("#three").css("background-color", "rgba(0,0,0,0.3)");
    });
    $("#four").mouseleave(function() {
        $("#product-options_1").css("opacity", "0.6");
        $("#product-options_2").css("opacity", "0.6");
        $("#four").css("background-color", "transparent").css("border", "thin solid transparent");
        $("#alpha").css("background-color", "transparent");
        $("#one").css("background-color", "transparent");
        $("#two").css("background-color", "transparent");
        $("#three").css("background-color", "transparent");
    });
    $(".btn-outline-secondary").mouseenter(function() {
        $(".fa-search").css("color", "#ff0000");
        $(".btn-outline-secondary").css("background-color", "rgba(0,0,0,1)");
        $(".btn-outline-secondary").css("border", "thin solid red");
    });
    $(".btn-outline-secondary").mouseleave(function() {
        $(".fa-search").css("color", "white");
        $(".btn-outline-secondary").css("border", "thin solid transparent");
    });
    $("#blog-options_small_su_s").on("click",function() {
        $(".dropdown-item").css("padding-top", "7px");
        $(".dropdown-item").css("padding-bottom", "7px");
        $(".dropdown-item").css("font-weight", "600");
        $("#one_prime").after($("#four_prime")).after($("#three_prime")).after($("#two_prime"));
    });
    $("#user-options_prime").on("click",function() {
        $(".dropdown-item").css("padding-top", "7px");
        $(".dropdown-item").css("padding-bottom", "7px");
        $(".dropdown-item").css("font-weight", "600");
        $("#two_prime").after($("#four_prime")).after($("#three_prime")).after($("#one_prime"));
    });
    $("#product-options_prime").on("click",function() {
        $(".dropdown-item").css("padding-top", "7px");
        $(".dropdown-item").css("padding-bottom", "7px");
        $(".dropdown-item").css("font-weight", "600");
        $("#four_prime").after($("#three_prime")).after($("#two_prime")).after($("#one_prime"));
    });
});