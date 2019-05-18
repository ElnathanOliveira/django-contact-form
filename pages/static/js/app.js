
$(document).ready(function($) {
    $('.clickable-row').click(function() {
        window.location = $(this).data("href");
    });
});

$(document).ready(function() {
    $('#example').DataTable();
} );

$(document).ready(function(){
    $("#id_register").mask("999.999.999-99");
});

$(document).ready(function(){
    $("#id_age").mask("99/99/9999");
});


