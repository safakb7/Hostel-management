import io
import xlsxwriter
from odoo import models, fields
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
from odoo.tools.safe_eval import json


class StudentWizard(models.TransientModel):
    _name = 'student.wizard'

    student_ids = fields.Many2many('hostel.student',
                                   string='Student')
    room_ids = fields.Many2many('hostel.room', string='Room')

    def action_pdf(self):
        query = '''select st.id,st.name,st.state,
        rm.room_number,rm.pending_amount from hostel_student st
        join hostel_room rm ON
        rm.id = st.room_id where 1=1'''
        param = []
        if self.student_ids:
            query += ' and st.id in %s'
            param.append(tuple(self.student_ids.ids))
        if self.student_ids and self.room_ids:
            query += ' and rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        if not self.student_ids and self.room_ids:
            query += ' and rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        self.env.cr.execute(query, tuple(param))
        result = self.env.cr.dictfetchall()
        print(result)
        data = {'date': self.read()[0], 'report': result}
        if not result:
            raise ValidationError("No data available")

        return self.env.ref(
            'hostel_management.action_report_student').report_action(
            None, data=data)

    def print_student_xlsx_report(self):
        print("xl button")

        query = '''select st.id,st.name,st.state,
               rm.room_number,rm.pending_amount from hostel_student st
               join hostel_room rm ON
               rm.id = st.room_id where 1=1'''
        param = []
        if self.student_ids:
            query += ' and st.id in %s'
            param.append(tuple(self.student_ids.ids))
        if self.student_ids and self.room_ids:
            query += ' and rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        if not self.student_ids and self.room_ids:
            query += ' and rm.id in %s'
            param.append(tuple(self.room_ids.ids))
        self.env.cr.execute(query, tuple(param))
        result = self.env.cr.dictfetchall()
        print(result,"result")
        data = {'report': result}
        print(data,"data")
        if not result:
            raise ValidationError("No data available")

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'student.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Student Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        a = 1
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('B2:I3', 'STUDENT REPORT', head)
        sheet.merge_range('A4:B4', 'Sl No:', cell_format)
        # sheet.merge_range('A5:B5', data[''], txt)
        sheet.merge_range('C4:D4', 'Name', cell_format)
        sheet.merge_range('C5:D5', data.get('name'), txt)
        sheet.merge_range('E4:F4', 'Room', cell_format)
        sheet.merge_range('E5:F5', data.get('room_number'), txt)
        sheet.merge_range('G4:H4', 'Pending Amount', cell_format)
        sheet.merge_range('G5:H5', data.get('pending_amount'), txt)
        sheet.merge_range('I4:J4', 'Invoice status', cell_format)
        sheet.merge_range('I5:J5', data.get('state'), txt)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
