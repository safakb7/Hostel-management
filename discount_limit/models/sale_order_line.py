from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float('Discount Amount',
                                   compute='_compute_discount_amount')

    @api.depends('product_uom_qty', 'price_unit', 'price_subtotal')
    def _compute_discount_amount(self):
        for record in self:
            record.discount_amount=(record.product_uom_qty *
                                    record.price_unit-record.price_subtotal)
