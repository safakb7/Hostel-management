/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {
    onLineClick(line) {
        console.log(line, "line")
        var order = this.env.services.pos.get_order();
        var selectedLine = order.get_selected_orderline();
        console.log(selectedLine, "selectedLine")
        if(line){
          order.removeOrderline(line)
        }
    }
});