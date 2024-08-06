from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LeaveRequest(models.Model):
    _name = 'leave.request'
    _description = 'Leave Request'
    _inherit = 'mail.thread'
    _rec_name = 'status'

    student_id = fields.Many2one('hostel.student', string='Student')
    leave_date = fields.Date("Leave date", required=True)
    arrival_date = fields.Date("Arrival date", required=True)
    status = fields.Selection([('new', 'New'),
                               ('approved', 'Approved')], default='new')
    room_id = fields.Many2one('hostel.room',
                              related='student_id.room_id', string="Room")
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self:
                                 self.env.user.company_id.id)

    def action_approve(self):
        for record in self:
            record.status = "approved"
            leave_requests = self.env['leave.request'].search([
                ('room_id', '=', record.room_id.id),
                ('leave_date', '=', record.leave_date),
                ('status', '=', 'approved')
            ])
            if leave_requests:
                self.env['cleaning.service'].create({
                    'room_id': record.room_id.id,
                })

    @api.constrains('arrival_date')
    def check_arrival_date(self):
        if self.arrival_date <= self.leave_date:
            raise ValidationError(
                "Arrival date cannot be before leave date")
