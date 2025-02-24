# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class Demo2(Document):
# 	def validate(self):
# 		student_id = "std-0016"
# 		student = frappe.get_list("Student", filters={"student_id": student_id}, fields=["student_id"])
# 		if student:
# 			subjects = frappe.get_list("Subjects", filters={"parent": student[0].name}, fields=["subjectname", "marks"])
# 			for subject in subjects:
# 				subjectname = subject.subjectname
# 				marks = subject.marks
# 				frappe.msgprint(f"Subject Name: {subjectname}, Marks: {marks}")

import frappe
from frappe.model.document import Document

class Demo2(Document):
    def validate(self):
        frappe.msgprint("\n".join([f"Subject Name: {s['subjectname']}, Marks: {s['marks']}" for s in frappe.get_list("Subjects", filters={"parent": frappe.get_value("Student", {"student_id": "std-0016"}, "name")}, fields=["subjectname", "marks"])]) or "No subjects found")

		

