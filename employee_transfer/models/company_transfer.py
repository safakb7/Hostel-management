from odoo import fields, models


class CompanyTransfer(models.Model):
    _name = 'company.transfer'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one("hr.employee", 'Employee',
                                  required=True)
    current_company = fields.Many2one(related="employee_id.company_id")
    date = fields.Date("Date")
    transfer_company_id = fields.Many2one('res.company',
                                          string="Transfer Company")

    state = fields.Selection([('new', 'New'),
                              ('requested', 'Requested'),
                              ('approved', 'Approved')],
                             default='new')

    def action_transfer_request(self):
        self.state = "requested"
        self.env['manager.approve'].create({
            'employee_id': self.employee_id.id,
            'company_id': self.transfer_company_id.id,
        })
