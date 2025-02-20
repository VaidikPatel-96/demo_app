// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Membership", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Library Membership', {
    validate: function(frm) {
        if (!frm.doc.from_date || !frm.doc.to_date) {
            frappe.msgprint(__('Please enter a valid From Date and To Date.'));
            frappe.validated = false;
        }
    }
});
