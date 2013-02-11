$(document).ready(function ($) {
    "use strict";
    $("a[rel=tooltip], span[rel=tooltip]").tooltip({ delay: { show: 500, hide: 100 }, html: false });
    App.chromeView = new App.ChromeView();
});
