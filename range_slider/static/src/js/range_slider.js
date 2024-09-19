/** @odoo-module */

import {  Component} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RangeField extends Component {

 static template = "range_slider.RangeField";

 static props = {
        ...standardFieldProps,

    };
    setup() {
         console.log(this)
         return this.props.name || '';
        }
    }
  export const rangeField = {
    component: RangeField,
    supportedTypes: ["integer"],

   };
registry.category("fields").add("range", rangeField);
