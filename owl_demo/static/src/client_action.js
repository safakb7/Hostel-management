/* @odoo-module */

import {registry} from "@web/core/registry";

import {Component} from "@odoo/owl";
import {MyInputField} from "./new_client_action";

export class MyClientAction extends Component {
    static components={MyInputField}

}
MyClientAction.template ="owl_demo.my_client_action";

registry.category("actions").add("owl_demo.MyClientAction",MyClientAction)
