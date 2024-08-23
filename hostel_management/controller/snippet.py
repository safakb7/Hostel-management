from odoo import http


class RoomSnippet(http.Controller):

    @http.route(['/latest_rooms'], type="json", auth="public",
                website=True, methods=['POST'])
    def latest_room(self):
        room = http.request.env['hostel.room'].search_read([],
         ['room_number', 'image', 'id'], limit=4)
        print(room)
        return room
