from odoo import models, fields


class SearchForm(models.Model):
    _name = "search.form"
    _description = "search form"

    search_text = fields.Char(string="Search ")

    def action_search(self):
        result = self.env['ir.model'].search([('transient','=',False)])
        print(result)
        record = self.env['ir.model.fields'].search([])

        for res in result:
            var = self.env[res.model].search([()])
            print(var)
