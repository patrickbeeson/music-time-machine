$(document).ready(function() {
    console.log("Thanks for exploring my diverse musical tastes!\n\nMy all-time top five musical artists are:\n\n* The Go! Team\n* Sufjan Stevens\n* The New Pornographers\n* Cannibal Ox\n* Boards of Canada\n\n- Patrick");
   // Add event tracking to form submit
    $('#form_submit').on('mousedown', function() {
        // Build our event for GA
        ga('send', 'event', 'form-submit', 'click');
    });
});
