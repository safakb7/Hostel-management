# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SearchData(models.Model):
    _name = 'search.data'

    model_id = fields.Many2one('ir.model', string='Models')
    field_id = fields.Many2one('ir.model.fields',
                               string='Applied Fields')
    search_text = fields.Char(string='Search')
    record_ids = (fields.One2many('search.data.lines',
                                  'search_id', string='Record'))

    @api.onchange('model_id')
    def _onchange(self):
        self.field_id = False

    def action_view_record(self):
        if self.model_id and self.field_id and self.search_text:
            records = self.env[self.model_id.model].search([(self.field_id.name, 'ilike', self.search_text)])
            for record in records:
                self.update({
                    'record_ids': [(fields.Command.create({
                        'model_id': self.model_id.id,
                        'field_id': self.field_id.id,
                        'record_id': record.id,
                    }))
                    ]
                })
