from odoo import models, fields


class StudentWizard(models.TransientModel):
   _name = 'student.wizard'

   student_id = fields.Many2many('hostel.student', string='Student')
   room = fields.Many2one('hostel.room', string='Room')

   def action_pdf(self):
      query = ''' SELECT '''
      data = {'date': self.read()[0]}
      return self.env.ref('hostel_management.action_report_student').report_action(
         None, data=data)
