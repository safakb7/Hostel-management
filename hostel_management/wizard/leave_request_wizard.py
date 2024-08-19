import io
import xlsxwriter
from odoo import models, fields
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
from odoo.tools.safe_eval import json


class LeaveRequestWizard(models.TransientModel):
    _name = 'leave.request.wizard'

    student_ids = fields.Many2many('hostel.student',
                                   string='Student')
    room_ids = fields.Many2many('hostel.room', string='Room')
    start_date = fields.Date('Start Date')
    arrival_date = fields.Date('Arrival Date')

    def query_generate(self):
        query = '''select st.id, st.student_id,st.leave_date,st.arrival_date,
                       st.duration,lr.room_number from leave_request st 
                       join hostel_student rm ON rm.id = st.student_id 
                       join hostel_room  lr ON lr.id = st.id where 1=1'''
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
        if self.start_date and not self.arrival_date:
            query += ' and %s >= st.leave_date'
            param.append(self.start_date)
        if self.arrival_date and not self.start_date:
            query += ' and %s <= st.arrival_date '
            param.append(self.arrival_date)
        if self.start_date and self.arrival_date:
            query += 'and %s >= st.leave_date and  %s <= st.arrival_date'
            param.append(self.start_date)
            param.append(self.arrival_date)
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
            'hostel_management.action_report_leave_request').report_action(
            None, data=data)

    def print_leave_request_xlsx_report(self):
        # print("xl button")
        data = self.query_generate()
        # print(data, "printdata")
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'leave.request.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Request Report',

                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        students = data.get('report')
        student_names = list(set(record['student_id'] for record in students))
        room_number = list(set(record['room_number'] for record in students))

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
        sheet.set_column('F:F', 25)

        sheet.merge_range('B2:I3', 'LEAVE  REQUEST REPORT', head_format)

        if len(student_names) == 1 and len(room_number) == 1:
            student_name = student_names[0]
            room = room_number[0]
            sheet.merge_range('A4:B4', f'STUDENT: {student_name}', head_format)
            sheet.merge_range('A5:B5', f'ROOM: {room}', head_format)

            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Start date', cell_format)
            sheet.write("C6", 'End date', cell_format)
            sheet.write("D6", 'Duration', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('leave_date'), text_format)
                sheet.write(row, 2, rec.get('arrival_date'), text_format)
                sheet.write(row, 3, rec.get('duration'), text_format)
                row += 1
                index += 1

        elif len(student_names) > 1 and len(room_number) == 1:
            room = room_number[0]
            sheet.merge_range('A5:B5', f'ROOM: {room}', head_format)
            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Name', cell_format)
            sheet.write("C6", 'Start Date', cell_format)
            sheet.write("D6", 'End Date', cell_format)
            sheet.write("E6", 'Duration', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('student_id'), text_format)
                sheet.write(row, 2, rec.get('leave_date'), text_format)
                sheet.write(row, 3, rec.get('arrival_date'), text_format)
                sheet.write(row, 4, rec.get('duration'), text_format)
                row += 1
                index += 1

        else:
            sheet.write("A6", 'Sl No:', cell_format)
            sheet.write("B6", 'Name', cell_format)
            sheet.write("C6", 'Room', cell_format)
            sheet.write("D6", 'Start Date', cell_format)
            sheet.write("E6", 'End Date', cell_format)
            sheet.write("F6", 'Duration', cell_format)

            row = 6
            index = 1
            for rec in students:
                sheet.write(row, 0, index, text_format)
                sheet.write(row, 1, rec.get('student_id'), text_format)
                sheet.write(row, 2, rec.get('room_number'), text_format)
                sheet.write(row, 3, rec.get('leave_date'), text_format)
                sheet.write(row, 4, rec.get('arrival_date'), text_format)
                sheet.write(row, 5, rec.get('duration'), text_format)
                row += 1
                index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
