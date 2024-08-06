from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student"
    _inherit = 'mail.thread'
    _rec_name = 'name'

    student_id = fields.Char("Student Id", readonly=True)
    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 ondelete='cascade', readonly=True)
    date_of_birth = fields.Date("DOB")
    age = fields.Char('Age', store=True)
    room_id = fields.Many2one('hostel.room', 'Room',
                              readonly=True)
    email = fields.Char(string='Email', required=True)
    image = fields.Binary(help="Select image here")
    receive_mail = fields.Char("Receive mail")
    street = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self:
                                 self.env.user.company_id.id)
    leave_requests = fields.One2many('leave.request',
                                     'student_id')

    invoice_ids = fields.One2many('account.move',
                                  'student_id')
    invoice_count = fields.Integer(compute='_compute_count', string="Invoices")

    active = fields.Boolean(string='Active', default=True)
    monthly_amount = fields.Float("Monthly amount")
    state = fields.Selection([('pending', 'Pending'), ('done', 'Done')]
                             , default='pending', compute='_compute_state')
    user_id = fields.Many2one('res.users')

    def action_allocate_room(self):
        partial = (self.env['hostel.room'].search
                   ([('state', '=', 'partial')], limit=1))

        if partial:
            print(self.room_id, 'partial', partial)
            self.room_id = partial[0]
            partial.remaining_rooms += 1
        else:
            empty = self.env['hostel.room'].search(
                [('state', '=', 'empty')], limit=1)
            if empty:
                self.room_id = empty
                empty.remaining_rooms += 1
            else:
                raise UserError("No rooms available for allocation")

        if self.room_id.remaining_rooms == self.room_id.number_of_beds:
            self.room_id.state = 'full'
        elif self.room_id.remaining_rooms > 0:
            self.room_id.state = 'partial'
        else:
            self.room_id.state = 'empty'

    @api.onchange('date_of_birth')
    def _compute_age(self):
        for record in self:
            if (record.date_of_birth and
                    record.date_of_birth <= fields.Date.today()):
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.date_of_birth)).years
            else:
                record.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_id', _('New')) == _('New'):
                vals['student_id'] = self.env['ir.sequence'].next_by_code(
                    'student_sequence')
            new_partner = {
                'name': vals.get('name'),
                'email': vals.get('email'),
                'street': vals.get('street'),
                'phone': vals.get('phone'),
                'mobile': vals.get('mobile')
            }
            print(self, vals)
            partner = self.env['res.partner'].create(new_partner)
            vals['partner_id'] = partner.id
            return super(HostelStudent, self).create(vals)

    def action_vacate_room(self):
        for student in self:
            if student.room_id:
                room = student.room_id
                room.student_ids -= student
                if not room.student_ids:
                    self.env['cleaning.service'].create({
                        'room_id': room.id,
                    })
                    room.state = 'cleaning'
                if student.leave_requests:
                    student.leave_requests.unlink()
                student.active = False

    def _compute_count(self):
        for record in self:
            record.invoice_count = len(record.invoice_ids)

    def get_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'invoice',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('student_id', '=', self.id)],
            'context': "{'create': False}"
        }

    @api.depends('invoice_ids')
    def _compute_state(self):
        for student in self:
            invoice = (self.env['account.move'].search([
                ('payment_state', '=', 'not_paid'),
                ('student_id', '=', self.id)]))
            if invoice:
                student.state = 'pending'
            else:
                student.state = 'done'

    def create_student_user(self):
        if self.name:
            user_rec = {
                'name': self.name,
                'login': self.email,
                'password': 'abc'
            }
            user = self.env['res.users'].create(user_rec)
            self.user_id = user
