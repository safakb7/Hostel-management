import io

import xlsxwriter

from odoo import models, fields
from odoo.exceptions import ValidationError


class LeaveRequestWizard(models.TransientModel):
    _name = 'leave.request.wizard'

    student_ids = fields.Many2many('hostel.student',
                                   string='Student')
    room_ids = fields.Many2many('hostel.room', string='Room')
    start_date = fields.Date('Start Date')
    arrival_date = fields.Date('Arrival Date')

    def action_pdf(self):
        query = '''select st.id, st.student_id,st.leave_date,st.arrival_date,
        st.duration,lr.room_number from leave_request st 
        join hostel_student rm ON rm.id = st.student_id 
        join hostel_room  lr ON lr.id = st.id '''
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
        if self.start_date and not self.arrival_date:
            query += ' where %s >= st.leave_date'
            param.append(self.start_date)
        if self.arrival_date and not self.start_date:
            query += ' where %s <= st.arrival_date '
            param.append(self.arrival_date)
        if self.start_date and self.arrival_date:
            query += 'where %s >= st.leave_date and  %s <= st.arrival_date'
            param.append(self.start_date)
            param.append(self.arrival_date)
        self.env.cr.execute(query, tuple(param))
        result = self.env.cr.dictfetchall()
        print(result)
        data = {'date': self.read()[0], 'report': result}
        if not result:
            raise ValidationError("No data available")

        return self.env.ref(
            'hostel_management.action_report_leave_request').report_action(
            None, data=data)


    def print_leave_request_xlsx_report(self):
        print("xl button")

        query = '''select st.id, st.student_id,st.leave_date,st.arrival_date,
              st.duration,lr.room_number from leave_request st 
              join hostel_student rm ON rm.id = st.student_id 
              join hostel_room  lr ON lr.id = st.id '''
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
        if self.start_date and not self.arrival_date:
            query += ' where %s >= st.leave_date'
            param.append(self.start_date)
        if self.arrival_date and not self.start_date:
            query += ' where %s <= st.arrival_date '
            param.append(self.arrival_date)
        if self.start_date and self.arrival_date:
            query += 'where %s >= st.leave_date and  %s <= st.arrival_date'
            param.append(self.start_date)
            param.append(self.arrival_date)
        self.env.cr.execute(query, tuple(param))
        result = self.env.cr.dictfetchall()
        print(result)
        data = {'date': self.read()[0], 'report': result}
        if not result:
            raise ValidationError("No data available")

        return self.env.ref(
            'hostel_management.action_report_leave_request').report_action(
            None, data=data)

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
