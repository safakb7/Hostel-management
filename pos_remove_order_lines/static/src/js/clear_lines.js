/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {
    onLineClick(line) {

        var order = this.env.services.pos.get_order();
        console.log(this.props.test_line)
        if(line){
          order.removeOrderline(this.props.test_line)
        }
    }
});