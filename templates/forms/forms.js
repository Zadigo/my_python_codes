$(document).ready(function () {
    var RegistrationForm = (function() {
        var signupForm = $('#signup');
        var signupFormCheckbox = signupForm.find('p label input[type="checkbox"]');
        var signupFormButton = signupForm.find('button[type="submit"]');

        var preventCheating = function() {
            if (signupFormCheckbox.is(':checked') === false && signupFormButton.attr('disabled') === undefined) {
                signupForm.on('submit', function(e) {
                    e.preventDefault();
                })
            } else {
                // pass
            }
        }

        var buttonState = function() {
            var isChecked = $(this).is(':checked');
            if (isChecked === true) {
                signupFormButton.removeClass('disabled');
            } else {
                signupFormButton.addClass('disabled');
            }
        }

        var bindEvent = function() {
            signupFormButton.on('click', preventCheating);
            signupFormCheckbox.on('click', buttonState);
        }

        var init = function() {
            bindEvent();
        }

        return {
            init: init
        }
    })();
    RegistrationForm.init();

    var ProfileForms = (function($) {
        var bindEvent = function(form_id){
            $('#' + form_id).on('submit', function(e) {
                e.preventDefault();
                
                var data = $(this).serialize() + '&form_id=' + form_id;
                var csrf = $('.csrf input[type="hidden"]').val();
                if (csrf){
                    var data = data + '&csrfmiddlewaretoken=' + csrf;
                }
    
                $.ajax({
                    type: "POST",
                    url: window.location.pathname,
                    data: data,
                    dataType: "json",
                    success: function (response) {
                        
                    },
                    error: function (response) {
                        
                    }
                });
            })
        }
    
        var getFormId = function(form) {
            return form.attr('id');
        }
    
        var getForms = function() {
            var forms = $('form');
            forms.each(function() {
                bindEvent(getFormId($(this)));
            })
        }
    
        var init = function() {
            getForms();
        }
    
        return {
            init: init
        }
    })(jQuery);
    // ProfileForms.init();
});