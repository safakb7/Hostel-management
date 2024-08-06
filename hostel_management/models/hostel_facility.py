from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HostelFacilities(models.Model):
    _name = "hostel.facility"
    _description = "Hostel Facility"
    _inherit = 'mail.thread'

    name = fields.Char("Name", required=True)
    charge = fields.Float("Charge")
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self:
                                 self.env.user.company_id.id)

    @api.constrains('charge')
    def check_charge(self):
        """ generate error when charge is lesser than zero  """
        if self.charge <= 0:
            raise ValidationError("Charge should be greater than zero")

