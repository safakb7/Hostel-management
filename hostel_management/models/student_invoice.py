from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    student_id = fields.Many2one('hostel.student', string="Student")

    @api.constrains('state')
    def change_state(self):
        if self.state == 'posted':
            template = self.env.ref('hostel_management.email_student_template')
            template.send_mail(self.id, force_send=True)
