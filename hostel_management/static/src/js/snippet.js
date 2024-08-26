/** @odoo-module */

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToFragment } from "@web/core/utils/render";

export function _chunk(array, size) {
   const result = [];
    for (let i = 0; i < array.length; i += size) {
      result.push(array.slice(i, i + size));
    }
    return result;
}

var LatestRoom = publicWidget.Widget.extend({
       selector: '.latest_room_snippets',

    willStart: async function() {
        await jsonrpc(
     	           	 '/latest_rooms'
       	).then((data) => {
           	this.data = data;
           	});
   	},
   	start: function() {
   	     var unique_id = new Date()
   	     var millisecond = unique_id.getMilliseconds();
   	     console.log(millisecond)
   	     var chunks = _chunk(this.data, 4)
   	     chunks[0].is_active = true
   	     this.$el.find('#latest_rooms').html(renderToFragment
      	('hostel_management.latest_room_carousel', {
      	        millisecond,
              	chunks
       	})
   	)
  	},
	});
	publicWidget.registry.room = LatestRoom;
	return LatestRoom;
