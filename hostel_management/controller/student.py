from odoo.http import request, route, Controller


class StudentFormController(Controller):

    @route('/student/form', auth='public', website=True ,type='http')
    def student_form(self, **kwargs):
        return request.render('hostel_management.student_register_template')

    @route('/student/form/available_rooms', type='http', auth="public",
           website=True)
    def available_rooms(self, **kw):
        available_rooms = request.env['hostel.room'].search([
            '|', ('state', '=', 'empty'), ('state', '=', 'partial')
        ])
        return request.render('hostel_management.available_rooms', {
            'rooms': available_rooms
        })

    @route('/student/form/submit', type='http', auth='public', website=True
          )
    def student_form_submit(self, **post):
        request.env['hostel.student'].sudo().create({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                    'street': post.get('street'),

        })
        return request.render('hostel_management.thankyou_message')
