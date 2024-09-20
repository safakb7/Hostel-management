from odoo import models, fields, api


class SearchForm(models.Model):
    _name = "search.form"
    _description = "search form"
    _rec_name = 'search_text'

    search_text = fields.Char(string="Search ")
    model_id = fields.Many2one('ir.model', string='model')
    field_id = fields.Many2one('ir.model.fields', string='field')
    record_ids = fields.One2many('search.form.lines',
                                 'search_id', string='record')

    @api.onchange('model_id')
    def _onchange(self):
        if self.model_id:
            domain = [('model_id', '=', self.model_id.id)]
        else:
            domain = []
        return {'domain': {'field_id': domain}}


    def action_search(self):
        if self.model_id and self.field_id and self.search_text:
            model = self.env['ir.model'].search([('transient', '=', False)])


        for res in model:
            var = self.env[res.model].search(['model'])
            print(var)
            return var


            # for rec in model:
            #     self.update({
            #         'record_ids': [(fields.Command.create({
            #             'model_id': model.id,
            #             'record_id': rec.id,
            #         }))
            #         ]
            #     })

        # result = self.env['ir.model'].search([('transient','=',False)])
        # print(result)
