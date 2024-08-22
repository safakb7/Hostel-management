/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";
export function _chunk(array, size) {
    const result = [];

    }
    return result;
}
var TopLatestRoom = PublicWidget.Widget.extend({
        selector: '.latest_rooms',
        willStart: async function () {
            const data = await jsonrpc('/latest_rooms', {})
            const [website_id] = data
            Object.assign(this, {
                website_id
            })
        },
        start: function () {
            const refEl = this.$el.find("#courosel")
            const { current_website_id } = this
            refEl.html(renderToElement(hostel_management.latest_room', {
                current_website_id,
                chunkData
            }))
        }
    });
PublicWidget.registry.top_latest_room_snippet = TopLatestRoom;
return TopLatestRoom;
