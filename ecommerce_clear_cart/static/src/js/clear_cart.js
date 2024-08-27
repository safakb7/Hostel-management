/** @odoo-module */

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

var button = publicWidget.widget.extends
{
        selector:'.oe_website_sale'
}
      $(oe_website_sale).on("click", "#clear_cart_button",
      function () {

        await.jsonrpc("/shop/clear_cart").then(function()
        {
           location.reload();
         })
        })

publicWidget.registry.demo = button;
	return button;
})
