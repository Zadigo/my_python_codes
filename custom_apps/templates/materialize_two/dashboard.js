$(document).ready(function() {
    // Script for changing the items
    // in the user profile cards menu
    $('#profile-details, #skills-details, #contact-details').on('click', function() {
        var w = $(this).data('menu');
        if (w == 'details') {
            $('#about-me').removeClass('hide');
            $('#skills').addClass('hide');
            $('#contact').addClass('hide');
        };
        if (w == 'skills') {
            $('#about-me').addClass('hide');
            $('#skills').removeClass('hide');
            $('#contact').addClass('hide');
        };
        if (w == 'contact') {
            $('#about-me').addClass('hide');
            $('#skills').addClass('hide');
            $('#contact').removeClass('hide');
        };
    });
});