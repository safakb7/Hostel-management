/** @odoo-module */

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToFragment } from "@web/core/utils/render";
import { registry } from "@web/core/registry";

console.log('abc')
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
        	var self = this;
        	await jsonrpc(
            	 '/latest_rooms'
        	).then((data) => {
            	this.data = data;
//            	console.log(data)
        	});

    	},
    	start: function() {
    	    console.log('data',this.data)
        	const chunks = _chunk(this.data, 4)
            console.log('chunks',chunks)

        	chunks[0].is_active = true
//        	console.log(chunks,'abc')
        	this.$el.find('#latest_rooms').html(renderToFragment('hostel_management.latest_room_carousel', {
                	chunks
            	})
        	)
    	},
	});
	publicWidget.registry.room = LatestRoom;
	return LatestRoom;
