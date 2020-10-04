$(document).ready(function() {
    $(".btn-black").mouseenter(function() {
        this.style.setProperty("border", "thin solid red");
        this.style.setProperty("color", "red");
    });
    $(".btn-black").mouseleave(function() {
        this.style.setProperty( "border", "thin solid transparent");
        this.style.setProperty("color", "white");
    });
    $("#submit_code").on("click",function() {
        $("#submit_code").hide();
        $("#coupon_form").show();
    });
    $("#cancel").on("click",function() {
        $("#coupon_form").hide();
        $("#submit_code").show();
    });
    $(".update-link").click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });
});