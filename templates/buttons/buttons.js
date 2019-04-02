$(document).ready(function () {
    var Quantity = (function(){
        var increment_div = $('.increment-buttons');
        var container = $('input[name="quantity"].increment-buttons-container');
        var up_button = $('.increment-buttons .up');
        var down_button = $('.increment-buttons .down');
        var default_value = 1
        var w = window

        // var createDiv = function() {
        //     var inputButtons = $('\
        //         <div class="input-buttons">\
        //             <button class="up"><i class="material-icons">keyboard_arrow_up</i></button>\
        //             <button class="down"><i class="material-icons">keyboard_arrow_down</i></button>\
        //         </div>\
        //     ')

        //     var has_input_buttons = $('.input-buttons')
        //     if (has_input_buttons.length === 0) {
        //         $(increment_div).append(inputButtons);
        //     }

        //     var up_button = $('.input-buttons .up');
        //     var down_button = $('.input-buttons .down');

        //     bindEvents();
        // }

        var inputValue = function() {
            container.val(default_value);
            bindEvents();
        }

        var addValue = function() {
            var current_value = container.val();
            container.val(current_value * 1 + 1)
        }

        var substractValue = function() {
            var current_value = container.val();
            if (current_value <= 1) {
                container.val(default_value)
            } else {
                container.val(current_value * 1 - 1)
            }
        }

        var bindEvents = function() {
            up_button.on('click', addValue)
            down_button.on('click', substractValue)
        }

        var init = function() {
            // createDiv();
            inputValue();
        }

        return {
            init: init
        }
    })();
    Quantity.init()

    (function( $ ) {
        $.fn.quantity = function( options ) {
    
            var settings = $.extend({
                color: "#556b2f",
                backgroundColor: "white"
            }, options)
            
            return this.css({'color': settings.color, 'backgroundColor': settings.backgroundColor});
    
        };
    }( jQuery ));
});