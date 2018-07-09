$(document).ready(function() {
    // This is used to hide fields on the form
    // according to the path of the /accounts/.../ url
    // e.g. /accounts/signup/ should have all the fields
    // as opposed to /forgot-password/ which should only
    // have email
    var w = window.location.pathname;
    if (w == '/accounts/forgot-password/') {
        $('input[name="nom"], input[name="prenom"], .accept-cgu').addClass('hide');
    };
    if (w == '/accounts/login/') {
        $('input[name="nom"], input[name="prenom"], .accept-cgu').addClass('hide');
    };

    // $('#accept-cgu').click(function() {
    //     if (this.checked) {

    //     }
    // });
})