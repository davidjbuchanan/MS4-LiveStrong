$(document).ready(function() {
    $("input[type=submit]").mouseenter(function() {               
        this.style.setProperty("border", "thin solid red");
        this.style.setProperty("color", "red");
    });
    $("input[type=submit").mouseleave(function() {               
        this.style.setProperty( "border", "thin solid transparent");
        this.style.setProperty("color", "white");
    });
});