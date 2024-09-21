/* @odoo-module */

import {registry} from "@web/core/registry";

import {Component,useState,onWillStart} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";



export class ListView extends Component {
    static template="dashboard_demo.listview"

     setup() {
            super.setup();
            this.state = useState({
                   data: [],
        });
             this.orm = useService("orm")
             onWillStart(async () => await this.fetchData())
        }
        async fetchData() {
                this.state.data = await this.orm.searchRead(this.props.model,
                ['partner_id','date_order'])

        }
}
