from odoo import models, fields


class StudentWizard(models.TransientModel):
    _name = 'student.wizard'

    student_ids = fields.Many2many('hostel.student',
                                   string='Student')
    room_ids = fields.Many2many('hostel.room', string='Room')

    def action_pdf(self):
        query = '''select st.id,st.name,st.state,
        rm.room_number,rm.pending_amount from hostel_student st
        join hostel_room rm ON
        rm.id = st.room_id'''
        param = []
        if self.student_ids:
            query += ' where st.id in %s'
            param.append(tuple(self.student_ids.ids))
        if self.student_ids and self.room_ids:
            query += ' and rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        if not self.student_ids and self.room_ids:
            query += ' where rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        self.env.cr.execute(query, tuple(param))
        result = self.env.cr.dictfetchall()
        print(result)
        data = {'date': self.read()[0], 'report': result}
        return self.env.ref(
            'hostel_management.action_report_student').report_action(
            None, data=data)
