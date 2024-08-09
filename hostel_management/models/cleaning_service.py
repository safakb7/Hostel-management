from odoo import models, fields


class CleaningService(models.Model):
    _name = "cleaning.service"
    _description = "Cleaning Service"
    _inherit = 'mail.thread'
    _rec_name = 'staff_id'

    room_id = fields.Many2one('hostel.room', 'Room')
    start_time = fields.Datetime("Time")

    staff_id = fields.Many2one('res.users', readonly=True)
    state = fields.Selection([('new', 'New'),
                              ('assigned', 'Assigned'),
                              ('done', 'Done')], default='new')

    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self:
                                 self.env.user.company_id.id)

    def action_assign(self):
        """ assigning the current user """
        self.staff_id = self.env.user

    def action_complete(self):
        """ generating when the room state is cleaning  """
        if self.room_id.state == 'cleaning':
            self.state = 'done'
            self.room_id.state = 'empty'
