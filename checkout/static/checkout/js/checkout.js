$(document).ready(function() {
    $(".btn-black").mouseenter(function() {               
        this.style.setProperty("border", "thin solid red");
        this.style.setProperty("color", "red");
    });
    $(".btn-black").mouseleave(function() {               
        this.style.setProperty( "border", "thin solid transparent");
        this.style.setProperty("color", "white");
    });
});

