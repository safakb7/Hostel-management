from odoo.http import request, Controller, route

class StudentFormController(Controller):
    @route('/studentform', auth='public', website=True)

    def student_form(self, **kwargs):
        return request.render('hostel_management.student_register_template')


    @route('/studentform/submit', type='http', auth='public', website=True,
           methods=['POST'])

    def student_form_submit(self, **post):
        print('gvtufe')
        request.env['student.register'].sudo().create({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                })
        return request.redirect('hostel_management.tmp_student_form_success')
