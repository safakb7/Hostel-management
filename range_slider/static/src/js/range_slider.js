/** @odoo-module */

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useState, onWillUpdateProps, Component } from "@odoo/owl";

console.log("hello")

export class RangeField extends Component {
console.log("hi")

 static template = "range_slider.RangeField";
    static props = {
        standardFieldProps,
    };
    setup() {
        return this.props.value || '';
//       console.log("props",this)
    }
    }
  export const rangeField = {
    component: RangeField,
    supportedTypes: ["integer"],
   };
registry.category("fields").add("range", rangeField);
