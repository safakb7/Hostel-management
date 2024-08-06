from odoo import models, fields, api


class Hospital_OP(models.Model):

    _name = "hospital.op"

    sequence = fields.Char("Sequence")
    date = fields.Datetime("Date")

    patient_id = fields.Many2one("res.partner")
    age = fields.Integer(related="patient_id.age")
    blood_group = fields.Selection(related="patient_id.blood_group")
    doctor_id = fields.Many2one("hr.employee")
    token_number = fields.Integer("Token Number")
    currency_id = fields.Many2one('res.currency')
    fees = fields.Monetary(related="doctor_id.hourly_cost", string='Fee', currency_field="currency_id")
    stage = fields.Selection([('new','New'),('inprogress','Inprogress'),('done','done')],default='new')
    responsible_id = fields.Many2one("res.users",default=lambda self: self.env.user and self.env.user.id or False,string="responsible")

@api.model

def create(self, vals):
    vals['sequence'] = self.env['ir.sequence'].next_by_code('my_sequence_code')
    return super(Hospital_OP, self).create(vals)
