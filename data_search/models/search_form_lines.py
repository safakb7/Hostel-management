from odoo import models, fields


class SearchFormLines(models.Model):
    _name = "search.form.lines"
    _description = "search form"

    search_id = fields.Many2one('search.form',string="search")
    model_id = fields.Many2one('ir.model',string="model")
    field_id = fields.Many2one('ir.model.fields',string="fields")
