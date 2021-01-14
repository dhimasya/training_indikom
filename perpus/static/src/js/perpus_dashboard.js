odoo.define('perpus.perpus_dashboard', function (require) {
    "use strict";

    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');

    var perpus_dashboard = AbstractAction.extend({
        template: 'perpus_dashboard',
        events: {
            'click .search': 'search_click',
        },
        start: function () {
            this.get_buku();
            return this._super.apply(this, arguments);
        },
        search_click: function() {
            var judul = this.$el.find('#search_judul').val();
            this.get_buku(judul);
        },
        get_buku: function(judul) {
            var self = this;
            $.ajax({
                type: 'POST',
                url: '/perpus/list_buku',
                headers: {
                    'Content-Type': 'text/plain',
                },
                data: JSON.stringify({judul: judul}),
                success: function(list) {
                    self.$el.find('.content').html(list)
                }
            })
        }
    });

    core.action_registry.add('widget_perpus_dashboard', perpus_dashboard);

    return perpus_dashboard;
});
