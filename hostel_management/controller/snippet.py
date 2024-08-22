from odoo import http


class RoomSnippet(http.Controller):

    @http.route(['/latest_rooms'], type="json", auth="public",
                website=True, methods=['POST'])
    def latest_room(self):
        Rooms = http.request.env['hostel.room'].search(
            ('state', 'in', ['empty', 'partial']),limit=4)
        return Rooms
