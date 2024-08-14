from odoo import models, api, fields


class ProductTemplate(models.Model):
    _inherit = 'sale.order.line'

    product_id = fields.Many2one('product.template')

    # @api.depends('order_id')
    # def _compute_product(self):
    #     for rec in self:
    #         rec.product_id = False
    #         if rec.order_id.is_only_ordered:
