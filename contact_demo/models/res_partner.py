from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'res.partner'

    is_only_ordered = fields.Boolean(string="Is only ordered")




