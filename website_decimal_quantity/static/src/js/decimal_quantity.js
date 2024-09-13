/** @odoo-module */

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.WebsiteSale.include({
    onClickAddCartJSON: function (ev) {
        ev.preventDefault();
        var $link = $(ev.currentTarget);
        var $input = $link.closest('.input-group').find("input");
        var min = parseFloat($input.data("min") || 0);
        var max = parseFloat($input.data("max") || Infinity);
        var previousQty = parseFloat($input.val() || 0, 10);
        var quantity = ($link.has(".fa-minus").length ? -0.1 : 0.1) + previousQty;
        var newQty = quantity > min ? (quantity < max ? quantity : max) : min;

        if (newQty !== previousQty) {
            $input.val(newQty).trigger('change');
        }
        return false;
    },
//    onChangeAddQuantity: function (ev) {
//    var $input = $(ev.currentTarget);
//    if ($input.data('update_change'))
//    {
//    return;
//    }
//    }
    changeProductQty(product, newQty) {
        const productNewQty = Math.max(0, newQty);
        const qtyChanged = productNewQty !== product.qty;
        product.qty = productNewQty;
        this.render(true);
        if (!qtyChanged) {
            return;
        }
    }
});
