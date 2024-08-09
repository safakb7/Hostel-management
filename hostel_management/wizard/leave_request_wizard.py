from odoo import models, fields


class LeaveRequestWizard(models.TransientModel):
   _name = 'leave.request.wizard'

   student_id = fields.Many2one('hostel.student', string='Student')
   room = fields.Many2one('hostel.room', string='Room')
   start_date = fields.Date('Start Date')
   arrival_date = fields.Date('Arrival Date')
