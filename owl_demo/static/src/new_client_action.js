/* @odoo-module */

import {registry} from "@web/core/registry";

import {Component} from "@odoo/owl";

export class MyInputField extends Component {
    state = { text: "" };
    static template="owl_demo.new_client_action"
    submit_button(){
    console.log("rhbgfh")
    }
}
