$(document).ready(function(){
    $('.content-author').on('mouseenter', function(){
        $('.author-details').addClass('show');
    }).on('mouseleave', function(){
        $('.author-details').removeClass('show');
    })
})