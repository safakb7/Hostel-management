/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

export class DeleteOrderLines extends Component {
    static template = "pos_remove_order_lines.ClearAllButton";
    setup() {
        this.pos = usePos();
    }
     onClick() {
        var order = this.pos.get_order();
        var lines = order.get_orderlines();
        if(lines.length) {
            lines.filter(line => line.get_product())
            .forEach(line => order.removeOrderline(line));
        }
    }
    }
ProductScreen.addControlButton({ component: DeleteOrderLines });

