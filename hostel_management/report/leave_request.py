from odoo import models, api


class StudentReport(models.AbstractModel):
    _name = 'report.hostel_management.report_leave_request'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("data", data)
        print("docids", docids)

        docs = self.env['leave.request'].browse([rec.get('id')
                                                 for rec in data['report']])
        print("docs", docs)

        return {
            'doc_ids': docids,
            'doc_model': 'leave.request',
            'docs': docs,
            'data': data,
        }
