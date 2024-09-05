import { patch } from "@web/core/utils/patch";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";

console.log('jj')

patch(ReceiptScreen.prototype, {
    printReceipt(){
    console.log("hi")
    }
});
