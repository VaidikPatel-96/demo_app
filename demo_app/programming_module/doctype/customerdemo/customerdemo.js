// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Customerdemo", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Customerdemo", {
    refresh: function(frm) {
        frm.page.remove_action_button(__('Action')); // Hides the action button
    }
});
