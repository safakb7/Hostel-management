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

    def query_generate(self):
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
        # print(result)
        data = {'date': self.read()[0], 'report': result}
        if not result:
            raise ValidationError("No data available")
        return data

    def action_pdf(self):
        data = self.query_generate()
        # print(data, "data")
        return self.env.ref(
            'hostel_management.action_report_student').report_action(
            None, data=data)

    def print_student_xlsx_report(self):
        # print("xl button")
        data = self.query_generate()
        # print(data, "printdata")
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
        students = data.get('report', [])
        student_names = list(set(record['name'] for record in students))
        room_number = list(set(record['room_number'] for record in students))
        print("room", room_number)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()

        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center', 'bold': True})
        head_format = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '15px'})
        text_format = workbook.add_format(
            {'font_size': '10px', 'align': 'center'})

        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 25)
        sheet.set_column('C:C', 25)
        sheet.set_column('D:D', 25)
        sheet.set_column('E:E', 25)

        sheet.merge_range('B2:I3', 'STUDENT REPORT', head_format)

        if len(student_names) == 1 and len(room_number) == 1:
            student_name = student_names[0]
            room = room_number[0]
            sheet.merge_range('A4:B4', f'STUDENT: {student_name}', head_format)
            sheet.merge_range('A5:B5', f'ROOM: {room}', head_format)

            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Pending Amount', cell_format)
            sheet.write("C6", 'Invoice Status', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('pending_amount'), text_format)
                sheet.write(row, 2, rec.get('state'), text_format)
                row += 1
                index += 1

        elif len(student_names) > 1 and len(room_number) == 1:
            room = room_number[0]
            sheet.merge_range('A5:B5', f'ROOM: {room}', head_format)

            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Name', cell_format)
            sheet.write("C6", 'Pending Amount', cell_format)
            sheet.write("D6", 'Invoice Status', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('name'), text_format)
                sheet.write(row, 2, rec.get('pending_amount'), text_format)
                sheet.write(row, 3, rec.get('state'), text_format)
                row += 1
                index += 1

        else:
            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Name', cell_format)
            sheet.write("C6", 'Room', cell_format)
            sheet.write("D6", 'Pending Amount', cell_format)
            sheet.write("E6", 'Invoice Status', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('name'), text_format)
                sheet.write(row, 2, rec.get('room_number'), text_format)
                sheet.write(row, 3, rec.get('pending_amount'), text_format)
                sheet.write(row, 4, rec.get('state'), text_format)
                row += 1
                index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
