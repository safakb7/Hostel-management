# -*- coding: utf-8 -*-
from odoo import fields, models, _


class SearchDataLine(models.Model):
    _name = 'search.data.line'
    _description = 'Search Data Line'

    search_id = fields.Many2one('search.data', string='Search Data')
    record_data = fields.Text(string='Record Data')



