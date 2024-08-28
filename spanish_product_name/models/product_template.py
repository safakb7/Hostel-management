# In your custom module's models/product.py
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name_es = fields.Char(string='Spanish Name')
