// In your custom module's static/src/js/pos_es_name.js
odoo.define('your_module_name.PosSpanishName', function (require) {
    'use strict';

    const PosBaseWidget = require('point_of_sale.BaseWidget');
    const PosModel = require('point_of_sale.Model');
    const core = require('web.core');
    const _t = core._t;

    const ProductScreenWidget = require('point_of_sale.ProductScreenWidget');

    ProductScreenWidget.include({
        _renderProduct: function (product) {
            this._super(product);
            const $product = this.el.querySelector(`.product[data-product-id="${product.id}"]`);
            const spanishName = product.name_es || '';
            if ($product) {
                $product.querySelector('.product-name').textContent += ` (${spanishName})`;
            }
        }
    });
});
