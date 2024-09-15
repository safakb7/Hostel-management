from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)


    @api.depends('order_line.product_uom_qty', 'order_line.product_id')
    def _compute_cart_info(self):
        for order in self:
            order.cart_quantity = sum(order.mapped('website_order_line.product_uom_qty'))
            print("hgsudh", order.cart_quantity)
            order.only_services = all(l.product_id.type in ('service', 'digital') for l in order.website_order_line)
