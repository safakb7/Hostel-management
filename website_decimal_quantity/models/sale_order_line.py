from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'

    product_uom_qty = fields.Float(
        string="Quantity",
        compute='_compute_product_qty', default=1.0)

    @api.depends('order_line.product_uom_qty', 'order_line.product_id')
    def _compute_product_qty(self):
        for order in self:
            order.cart_quantity = sum(order.mapped('website_order_line.product_uom_qty'))
