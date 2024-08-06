from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_vendor_products = fields.Boolean(string="Is Vendor Products")
