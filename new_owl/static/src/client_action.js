/* @odoo-module */

import {registry} from "@web/core/registry";

import {Component, useState} from "@odoo/owl";

class Counter extends Component {
    static template = "new_owl.Counter";

    setup() {
        this.state = useState({ value: 0 });
    }

    increment() {
        this.state.value++;
    }
}
registry.category("actions").add("new_owl.Counter",Counter)
