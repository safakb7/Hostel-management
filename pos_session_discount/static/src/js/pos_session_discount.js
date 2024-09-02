/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import {ErrorPopup} from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
import { ORM } from "@web/core/orm_service";

patch(Order.prototype, {
    async pay() {
       console.log(this)
       const total_discount = this.get_total_discount()
       const data = await this.env.services.orm.call('pos.session','get_discount',
       [this.pos_session_id])

       if(data+total_discount > this.pos.config.discount_limit)
       {

        this.pos.env.services.popup.add(ErrorPopup, {
                    title: _t("Error"),
                    body: _t("The session discount limit has been exceeded."),
                });
        }
       else
       {
         return super.pay(...arguments);
              }
       }
       });
