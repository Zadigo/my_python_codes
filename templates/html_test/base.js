$(document).ready(function () {
    var Google = (function(){
        var c = $('#button_id')
        var init = function(){
            bindEvents();
        }

        var getValue = function(){
            alert('this');
        }

        var bindEvents = function(){
            c.on('click', getValue);
        }

        return {
            init: init
        }
    })();
    Google.init();

    var Forms = (function(){
        var f = $('form');
        var url = window.location.href;
        var len = f.length;

        var getId = function(event){
            event.preventDefault();

            var data = $(this).serialize();
            var form_id = '&form_id=' + this.id;

            $.ajax({
                type: 'POST',
                url: url,
                data: data + form_id,
                dataType: 'json',
                success: function (response) {
                    $('#test').html('Success!');
                },
                error: function(response) {
                    $('#test').html('Error!');
                }
            });
        }

        var bindEvents = function(){
            for (var i = 0; i < len; i++) {
                f[i].addEventListener('submit', getId);
            }
        }

        var init = function(){
            bindEvents();
        }

        return {
            init: init
        }
    })();
    Forms.init();

    (function( $ ) {
        $.fn.greenify = function( options ) {
    
            var settings = $.extend({
                color: "#556b2f",
                backgroundColor: "white"
            }, options)
            
            return this.css({'color': settings.color, 'backgroundColor': settings.backgroundColor});
    
        };
    }( jQuery ));
});