from odoo import models, api


class StudentReport(models.AbstractModel):
    _name = 'report.hostel_management.report_student'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("data123", data)
        print("docidshj", docids)

        docs = self.env['hostel.student'].browse(
            [rec.get('id') for rec in data['report']])
        print("docs", docs)

        return {
            'doc_ids': docids,
            'doc_model': 'hostel.student',
            'docs': docs,
            'data': data,
        }
