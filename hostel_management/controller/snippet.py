from odoo import http
from odoo.http import request


class RoomSnippet(http.Controller):

    @http.route(['/latest_rooms'], type="json", auth="public",
                website=True, methods=['POST'])
    def latest_room(self):
        room = http.request.env['hostel.room'].search_read([],
                        ['room_number','image', 'id'],order="create_date desc")
        print(room)
        return room

    @http.route(['/room/<int:id>'], type='http', auth='user', website=True)
    def get_room_data(self, **post):
        room = (request.env['hostel.room'].
                browse(post.get('id')))
        return request.render('hostel_management.room_data_snippet',
                              {'room': room})
