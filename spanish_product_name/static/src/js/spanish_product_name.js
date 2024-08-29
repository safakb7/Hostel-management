/** @odoo-module */

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";

patch(ProductCard.prototype, {
    getDisplayData() {
        return {
            ...super.getDisplayData(),
            spanish_name: this.get_product().spanish_name,
        };
    },
});
