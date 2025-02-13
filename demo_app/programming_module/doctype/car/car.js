// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

// frappe.ui.form.on("car", {
// // 	refresh(frm) {

// // 	},



frappe.ui.form.on("car", {
    validate: function (frm) {
        if (!frm.doc.car_name) {  // Use actual child table fieldname
            frm.doc.car_name = [];
        }

        let row = frm.add_child("car_name");  // Correct child table fieldname
        row.name1 = "MG";  // Ensure "name1" exists in the Child Table Doctype

        frm.refresh_field("car_name");  // Refresh child table to reflect changes
    }
});
