from odoo import models, api


class StudentReport(models.AbstractModel):
    _name = 'report.hostel_management.report_student'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hostel.student'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hostel.student',
            'docs': docs,
            'data': data,
        }
