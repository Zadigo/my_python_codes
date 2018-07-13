$(document).ready(function() {
    // Dynamically masking the fields of
    // the form given the path in the
    // current url. This is to use with
    // the complete form template
    var p = window.location.pathname;
    if (p === '/book/') {
        var fld = $('input[name="nom"]');
        fld.parent().addClass('hide');
        fld.removeAttr('required');
        fld.attr('novalidate', 'novalidate');
    };
    if (p === '/books/') {
        $('input').each(function(element) {
            if (this['name'] === 'nom' || this['name'] === 'prenom') {
                $(this).parent().addClass('hide');
                $(this).removeAttr('required');
                $(this).attr('novalidate', 'novalidate');
            }
        });
    };
})
