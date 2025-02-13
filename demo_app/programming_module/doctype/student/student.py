# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class Student(Document):
# 	pass

# @frappe.whitelist()
# def calculate_percentage(doc, method):
#     total_marks = sum([row.marks for row in doc.subjects])
#     total_subjects = len(doc.subjects)
#     doc.percentage = (total_marks / (total_subjects * 100)) * 100 if total_subjects > 0 else 0

# import frappe
# from frappe.model.document import Document

# class Student(Document):
#     def validate(self):
#         """Ensure validation and auto-calculate percentage before saving."""
#         self.calculate_percentage()

#     def calculate_percentage(self):
#         """Calculate the percentage based on marks."""
#         total_marks = 0
#         subject_count = len(self.subjects)

#         if subject_count > 0:
#             for subject in self.subjects:
#                 total_marks += subject.marks

#             self.percentage = total_marks / subject_count
#         else:
#             self.percentage = 0

# import frappe
# from frappe.model.document import Document

# class Student(Document):
#     def validate(self):
#         self.calculate_percentage()
#         self.set_status()

#     def calculate_percentage(self):
#         if self.subjects:
#             total_marks = sum(subject.marks for subject in self.subjects)
#             self.percentage = total_marks / len(self.subjects) if len(self.subjects) > 0 else 0
#         else:
#             self.percentage = 0

#     def set_status(self):
#         self.status = "Pass" if self.percentage >= 40 else "Fail"

# class Subject(Document):
#     pass


# import frappe
# from frappe.model.document import Document

# class Student(Document):
#     def before_save(self):
#         self.calculate_percentage()
#         self.calculate_status()

#     def calculate_percentage(self):
#         if self.subjects:
#             total_marks = sum(subject.marks for subject in self.subjects)
#             subject_count = len(self.subjects)
#             self.percentage = (total_marks / (subject_count * 100)) * 100 if subject_count else 0

#     def calculate_status(self):
#         if self.subjects:
#             all_passed = all(subject.marks >= 35 for subject in self.subjects)
#             self.status = "Pass" if all_passed else "Fail"

import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        self.calculate_percentage()
        self.set_status()
        self.set_grade()

    def calculate_percentage(self):
        if self.subjects:
            total_marks = sum([subject.marks for subject in self.subjects])
            self.percentage = total_marks / len(self.subjects) if len(self.subjects) > 0 else 0
        else:
            self.percentage = 0

    def set_status(self):
        if self.percentage >= 35:
            self.status = "Pass"
        else:
            self.status = "Fail"
    
    def set_grade(self):
        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 80:
            self.grade = "B"
        elif self.percentage >= 70:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"


