/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {
    onLineClick(test_line) {
        var order = this.env.services.pos.get_order();
        if(test_line){
          order.removeOrderline(test_line)

        }
    }
});
