$(document).ready(function() {
    console.log("document is ready!")
    // AJAX GET
    $('.get-more').click(function(){

        $.ajax({
            type: "GET",
            url: "/",
            success: function(data) {
            for(i = 0; i < data.length; i++){
                $('ul').append('<li>'+data[i]+'</li>');
            }
        }
        });

    });

});