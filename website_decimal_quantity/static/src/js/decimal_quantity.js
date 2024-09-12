/** @odoo-module */

console.log("log")
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { patch } from "@web/core/utils/patch";

PublicWidget.registry.WebsiteSale.extends({
    onClickAddCartJSON: function (ev) {
    ev.preventDefault();
        var $parent = $(ev.target).closest('.js_product');
        var product_id = this._getProductId($parent);
      var quantity = ($link.has(".fa-minus").length ? -0.1 : 0.1) + previousQty;
      }
      });

//onChangeAddQuantity: function (ev) {
//        var $parent;
//
//        if ($(ev.currentTarget).closest('.oe_advanced_configurator_modal').length > 0){
//            $parent = $(ev.currentTarget).closest('.oe_advanced_configurator_modal');
//        } else if ($(ev.currentTarget).closest('form').length > 0){
//            $parent = $(ev.currentTarget).closest('form');
//        }  else {
//            $parent = $(ev.currentTarget).closest('.o_product_configurator');
//        }
//
//        this.triggerVariantChange($parent);
//    },
//
