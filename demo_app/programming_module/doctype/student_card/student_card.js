// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student card", {
	// refresh(frm) {
    before_save: function(frm) {
        frm.doc.subject_details.forEach(studentCardDetails => {
            let marks = studentCardDetails.marks || 0;
            let max_marks = studentCardDetails.max_marks || 0;
            let percentage = (marks / max_marks) * 100;
            studentCardDetails.percentage = percentage;
        });

	},
});
