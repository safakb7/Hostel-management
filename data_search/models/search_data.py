# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SearchData(models.Model):
    _name = 'search.data'
    _description = "search data"
    _rec_name = "model_id"

    model_id = fields.Many2one('ir.model', string='Model')
    field_id = fields.Many2one('ir.model.fields',
                               string='Field')
    search_text = fields.Char(string='Search text')
    record_ids = fields.One2many('search.data.lines',
                                 'search_id', string='Record')

    @api.onchange('model_id')
    def _onchange(self):
        self.field_id = False

    def action_search(self):
        record_ids = []

        self.record_ids.unlink()
        if self.model_id and self.field_id and self.search_text:

            records = self.env[self.model_id.model].search([(self.field_id.name,
                                                             'ilike',
                                                             self.search_text)])
            print('records',records)
            for record in records:
                self.update({
                    'record_ids': [(fields.Command.create({
                        'model_id': self.model_id.id,
                        'field_id': self.field_id.id,
                        'record_id': record.id,
                    }))
                    ]
                })
        # if not self.field_id:
        #     searchable_fields = self.env[self.model_id.model]._fields.items()
        #     print(searchable_fields)
        #     domain = []
        #     print(domain)
        #     for field_name, field in searchable_fields:
        #        if field.type in ['char', 'text']:
        #            domain.append((field_name, 'ilike', self.search_text))
        #            print("domain",domain)
        #     for i in range(len(domain) - 1):
        #        domain.insert(0, '|')
        #
        #     records = self.env[self.model_id.model].search(domain)
        #     print(records)
        #     for record in records:
        #        record_ids.append(fields.Command.create({
        #            'model_id': self.model_id.id,
        #            'field_id': self.field_id.id,
        #            'record_id': record.id,
        #        }))
        #     self.update({
        #        'record_ids': record_ids
        #    })
