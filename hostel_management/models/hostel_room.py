from datetime import date
from odoo import models, fields, api, _


class HostelRoom(models.Model):
    _name = "hostel.room"
    _description = "Hostel Room"
    _inherit = 'mail.thread'
    _rec_name = 'room_number'

    room_number = fields.Char("Room number")
    room_type = fields.Selection(selection=[
        ('single', 'Single'),
        ('double', 'Double'),
    ])
    number_of_beds = fields.Integer("Number Of Beds")
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self:
                                 self.env.user.company_id.id)
    currency_id = fields.Many2one(
        'res.currency', string="currency",
        related='company_id.currency_id',
        default=lambda self: self.env.user.company_id.currency_id.id)
    rent = fields.Float("Rent", currency_field="currency_id")
    state = fields.Selection([('empty', 'Empty'),
                              ('partial', 'Partial'),
                              ('full', 'Full'), ('cleaning', 'Cleaning')],
                             default='empty')
    remaining_rooms = fields.Integer(default=0)
    facility_ids = fields.Many2many('hostel.facility',
                                    string="Facilities")
    student_ids = fields.One2many('hostel.student',
                                  "room_id")

    total_rent = fields.Float('Total rent', compute='_compute_total_rent',
                              readonly=True)
    pending_amount = fields.Float('Pending Amount',
                                  compute='_compute_pending_amount')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('', _('New')) == _('New'):
                vals['room_number'] = self.env['ir.sequence'].next_by_code(
                    'room_sequence_code')
        return super().create(vals_list)

    @api.depends('rent', 'facility_ids.charge')
    def _compute_total_rent(self):
        for room in self:
            facility_charges = sum(room.facility_ids.mapped('charge'))
            room.total_rent = room.rent + facility_charges

    def create_monthly_invoice(self):
        for student in self.student_ids:
            self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': student.partner_id.id,
                'student_id': student.id,
                'invoice_line_ids': [(0, 0, {
                    'product_id': self.env.ref('hostel_management.product_rent').id,
                    'price_unit': self.total_rent
                })]
            })

    def _cron_check_invoice(self):
        print("abc")
        template = (self.env.ref
                    ('hostel_management.email_student_template'))
        print(template)
        today = date.today()
        if today.day == 1:
            for student in self.student_ids:
                invoice = self.env['account.move'].create({
                    'move_type': 'out_invoice',
                    'partner_id': student.partner_id.id,
                    'invoice_date': today,
                    'student_id': student.id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': self.env.ref
                        ('hostel_management.product_rent').id,
                        'price_unit': self.total_rent
                    })]
                })
                template.send_mail(invoice.id, force_send=True)

    @api.depends('student_ids.invoice_ids')
    def _compute_pending_amount(self):
        self.pending_amount = 0
        for room in self:
            total_amount = sum(room.student_ids.mapped('invoice_ids').filtered(
                lambda x: x.payment_state == 'not_paid').mapped
                               ('amount_untaxed_signed'))
            room.pending_amount = total_amount
