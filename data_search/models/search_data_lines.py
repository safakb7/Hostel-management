# -*- coding: utf-8 -*-
from odoo import fields, models, _


class SearchDataLines(models.Model):
    _name = 'search.data.lines'

    search_id = fields.Many2one('search.data', string='Data')
    model_id = fields.Integer(string='Model id')
    field_id = fields.Char(string='field id')
    record_id = fields.Integer(string='Record id')

    def action_view_record(self):
        self.ensure_one()
        if self.model_id and self.record_id:
            model = self.env['ir.model'].browse(self.model_id)
            record = self.env['ir.model.fields'].browse(self.record_id)
            return {
                'type': 'ir.actions.act_window',
                'res_model': model.model,
                'res_id': record.id,
                'view_mode': 'form',
            }
