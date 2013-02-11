var App = window.App || {};

App.settings = {
    alert_delay: 10000
};

var MESSAGE_TEMPLATE = '<div class="alert error fade in alert-<%= type %>">' +
	'<a class="close" href="#" data-dismiss="alert">&times;</a>' +
	'<strong><%= title %></strong> <%= message %>' +
	'</div>';

(function ($) {
    "use strict";

    App.ChromeView = Backbone.View.extend({

    	el: "body",

        initialize: function () {
            _.bindAll(this, "showAlert", "showModal");
            this.$("#messages-area .alert").delay(App.settings.alert_delay).fadeOut("slow", $.remove);
        },

        showAlert: function (message, type, title) {
            var template = _.template(
                MESSAGE_TEMPLATE,
                {message: message, type: type || "success", title: title || ""}
            );
            var $alert = $(template);
            this.$("#messages-area").append($alert);
            this.$("#messages-area .alert").delay(App.settings.alert_delay).fadeOut("slow", $.remove);
        },

        showModal: function(e, id){
            var $modal = this.$(id);
            if($modal.size()){
                e.preventDefault();
                $modal.on("shown", function () {
                    $(this).find("input:text:first").focus();
                }).modal({remote: false});
            }
        }
    });
})(jQuery);
