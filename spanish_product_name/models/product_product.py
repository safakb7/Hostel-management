from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    spanish_name = fields.Char(string='Spanish Name')
