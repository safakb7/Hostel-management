/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

PublicWidget.registry.cart = PublicWidget.Widget.extend
({
    selector: '.oe_website_sale',
    events: {
        'click #clear_cart_button':'_onButtonClick',
    },
    _onButtonClick: async function(ev){
        await jsonrpc('/shop/clear_cart')
       location.reload();
    },
})
