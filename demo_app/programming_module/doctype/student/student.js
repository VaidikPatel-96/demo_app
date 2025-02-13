// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
//     validate: function(frm) {
//         frm.doc.Subject_Details.forEach(row => {
//             if (row.marks < 0) {
//                 frappe.msgprint({
//                     title: __('Validation Error'),
//                     message: __('Marks cannot be negative for {0}', [row.subjects]),
//                     indicator: 'red'
//                 });
//                 frappe.validated = false;
//             }
//         });
//     }

// });
frappe.ui.form.on("Student", {
    validate: function(frm) {
        frm.doc.subjects.forEach(row => {
            if (row.marks < 0) {
                frappe.throw(__('Marks cannot be negative for {0}', [row.subjects]));
            }
        });
    }
});
