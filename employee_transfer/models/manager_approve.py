from odoo import fields, models


class ManagerApprove(models.Model):
    _name = 'manager.approve'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company',
                                 'Transfer company')

    def action_approve(self):
        self.env['company.transfer'].search([
            ('employee_id', '=', self.employee_id.id)
            ]).write({'state': 'approved'})
        self.employee_id.company_id = self.company_id
