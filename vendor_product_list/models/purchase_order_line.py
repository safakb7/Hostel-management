from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_ids = fields.Many2many('product.product',
                                   compute='_compute_product')
    product_id = fields.Many2one('product.product')

    @api.depends('order_id')
    def _compute_product(self):
        for rec in self:
            rec.product_ids = False
            if rec.order_id.is_vendor_products:
                rec.product_ids = rec.product_id.search([(
                    'product_tmpl_id.seller_ids.partner_id', '=',
                    self.order_id.partner_id.id)])
                print(rec.product_ids)
            else:
                rec.product_ids = rec.product_id.search([])
