# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SearchData(models.Model):
    _name = 'search.data'
    _description = 'Search Data Model'
    _rec_name = 'search_text'

    search_text = fields.Char(string='Search Text')
    model_id = fields.Many2one('ir.model', string='Model')
    field_id = fields.Many2one('ir.model.fields', string='Field')

    # record_ids = fields.One2many('search.data.lines', 'search_id',
    #                              string='Data Lines')

    @api.onchange('model_id')
    def _onchange_model_id(self):
        if self.model_id:
            fields = self.env['ir.model.fields'].search(
                [('model_id', '=', self.model_id.id)])
            print(fields)
            return {'domain': {'field_id': [('id', 'in', fields.ids)]}}
        else:
            return {'domain': {'field_id': []}}

    def action_search(self):
        print('vhd')

        if self.model_id and self.field_id and self.search_text:
            model = self.env[self.model_id.model]
            domain = [(self.field_id.name, 'ilike', self.search_text)]
            records = model.search(domain)


            # for record in records:
            #     self.record_ids.create({
            #         'record_data': str(record)
            #     })
