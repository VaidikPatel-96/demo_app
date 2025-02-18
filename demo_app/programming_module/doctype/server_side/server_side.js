// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Server_side", {
// 	enable: function(frm){
//         frm.call({
//             doc:frm.doc,
//             method:'frm_call',
//             args:{
//                 msg: "HELLO"
//             },
//             freeze: true,
//             freeze_message:('Calling frm_call Method'),
//             callback:function(r){
//                 frappe.msgprint(r.message)
//                 // frappe.msgprint("Server side calling compleated")
//                 // frm.refresh_field('medication_orders');
//             }

//         })
//     }
// });


// frappe.ui.form.on("Server_side", {
// 	enable: function(frm){
//         frappe.call({
//             method: "demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.frappe_call",

//             args:{
//                 msg: "HELLO"
//             },
//             freeze: true,
//             freeze_message:__('Calling frappe_call Method'),
//             callback:function(r){
//                 frappe.msgprint(r.message)
//                 // frappe.msgprint("Server side calling compleated")
//                 // frm.refresh_field('medication_orders');
//             }

//         })
//     }
// });