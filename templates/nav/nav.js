$(document).ready(function(){
    $('nav').css({
        'transition':'all 0.2s ease'
    })
    $(window).on('scroll', function(){
        if ($(window).scrollTop()){
            $('nav').removeClass('transparent');
        }else{
            $('nav').addClass('transparent');
        }
    })
})