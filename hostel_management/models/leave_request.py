from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


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
    duration = fields.Char('Duration')

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

    @api.onchange('leave_date', 'arrival_date', 'duration')
    def calculate_date(self):
        if self.leave_date and self.arrival_date:
            d1 = datetime.strptime(str(self.leave_date), '%Y-%m-%d')
            d2 = datetime.strptime(str(self.arrival_date), '%Y-%m-%d')
            d3 = d2 - d1
            self.duration = str(d3.days)
