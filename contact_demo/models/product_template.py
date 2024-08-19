from odoo import models, api, fields


class ProductTemplate(models.Model):
    _inherit = 'sale.order.line'

    product_ids = fields.Many2many('product.product',compute='_compute_product')

    product_id = fields.Many2one('product.product')



    @api.depends('order_id')
    def _compute_product(self):
        for rec in self:
            rec.product_ids = False

            if rec.order_id.partner_id.is_only_ordered:
                rec.product_ids = rec.product_id.filtered( lambda r: r.invoice_policy == 'order')
                print(rec.product_ids)
