/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";

patch(Orderline.prototype,{
        getDisplayData() {

            return{
            ...super.getDisplayData(),
            spanish_name: this.get_spanishname()
            };
        },
            get_spanishname()
            {
            return this.product.spanish_name
            }
})
