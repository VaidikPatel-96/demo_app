# # # Copyright (c) 2025, D-codE and contributors
# # # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class Student(Document):
#     def validate(self):
#         self.calculate_percentage()
#         # self.set_status()
#         self.set_grade()

#     def calculate_percentage(self):
#         if self.subjects:
#             total_marks = sum([subject.marks for subject in self.subjects])
#             self.percentage = total_marks / len(self.subjects) if len(self.subjects) > 0 else 0
#         else:
#             self.percentage = 0

#     # def set_status(self):
#     #     if self.percentage >= 35:
#     #         self.status = "Pass"
#     #     else:
#     #         self.status = "Fail"
    
#     def set_grade(self):
#         if self.percentage >= 90:
#             self.grade = "A"
#         elif self.percentage >= 80:
#             self.grade = "B"
#         elif self.percentage >= 70:
#             self.grade = "C"
#         elif self.percentage >= 50:
#             self.grade = "D"
#         else:
#             self.grade = "F"

# Copyright (c) 2025, Sigzen and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Student(Document):
    def before_save(self):
        total_marks = 0
        total_subjects = len(self.subjects)

        for subject in self.subjects:
            # Corrected: Check 'marks' instead of 'subject_mark'
            if subject.marks < 0:
                frappe.throw(f"Marks for {subject.subjectname} cannot be negative.")
            if subject.marks > 100:
                frappe.throw(f"Marks for {subject.subjectname} cannot be more than 100.")

            total_marks += subject.marks  # Corrected field

        # Calculate percentage
        self.percentage = (total_marks / (total_subjects * 100)) * 100 if total_subjects else 0

        # Assign grade based on percentage
        if self.percentage > 90:
            self.grade = "A"
        elif self.percentage > 80:
            self.grade = "B"
        elif self.percentage >= 70:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"
