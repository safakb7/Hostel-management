/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

export class CreateProduct extends Component {
    static template = "pos_create_button.CreateButton";
    static props = {
        class: { type: Object, optional: true },
        line: {
            type: Object,
            shape: {
                productName: String,
                price: String,
                qty: String,

                unit: { type: String, optional: true },
                unitPrice: String,

                "*": true,
            },
        },
    };
    static defaultProps = {
        class: {},

    };
    setup() {
     this.pos = usePos()
    }

     onClick() {
        var product = this.pos.getProductInfo(product,1)
        console.log(this)
        }
        }
ProductScreen.addControlButton({ component: CreateProduct });
