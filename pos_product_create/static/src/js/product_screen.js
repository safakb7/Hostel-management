/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

export class CreateProduct extends Component {
    static template = "pos_create_button.CreateButton";

    setup() {
     this.pos = usePos()
    }

      onClick() {
            var product = this.pos.get_product_list(); var list = new ProductListModal();
        }
 }
ProductScreen.addControlButton({ component: CreateProduct });
