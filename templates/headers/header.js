$(document).ready(function(){
    $('.header-navigation-wrapper li').on('click', function(){
        $('.header-navigation-wrapper li').each(function(e){
            $(this).removeClass('active');
        });
        $(this).addClass('active');
    })

    $('.test').on('click', function(){
        $('.header-title').slideToggle();
    })
})