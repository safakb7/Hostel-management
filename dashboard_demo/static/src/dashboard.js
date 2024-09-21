/**@odoo-module */
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import {ListView} from "./listview";

const actionRegistry = registry.category("actions");
export class Dashboard extends Component {
    static components={ListView}

}

Dashboard.template = "dashboard_demo.Dashboard";
actionRegistry.add("dashboard", Dashboard);
