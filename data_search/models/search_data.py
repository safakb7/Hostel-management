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
        if not self.field_id:
            field = self.env['ir.model.fields'].search(
                [('model_id', "=", self.model_id.id), ('ttype', '=', 'char')])
            print(field)

            for rec in field:
                print("rec", rec.name)
                print("search_text", self.search_text)
                records = self.env[self.model_id.model].search(
                    [(rec.name, 'ilike', self.search_text), ()])
                print(records)
                for record in records:
                    self.update({
                        'record_ids': [(fields.Command.create({
                            'model_id': self.model_id.id,
                            'field_id': self.field_id.id,
                            'record_id': record.id,
                        }))
                        ]
                    })










