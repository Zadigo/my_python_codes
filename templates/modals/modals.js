$(document).ready(function(){
    var Modal = (function(){
        var trigger = $('.modal-pictures-trigger');
        var modals = selectObjects('.modal');
        var modals_closers = selectObjects('.modal-close');
        var w = window;
        var isOpen = false;

        function selectObjects(obj_name) {
            return document.querySelectorAll(obj_name);
        }    

        var getModalId = function(event) {
            event.preventDefault();
            var self = this;
            var modalId = self.dataset.modal;
        };

        var bindActions = function() {
            for (var i = 0; i < len; i++) {
                trigger[i].addEventListener('click', getModalId, false)
            }
        };

        var init = function() {
            bindActions();
        };

        return {
            init: init
        };
    }());
    
    Modal.init()
})