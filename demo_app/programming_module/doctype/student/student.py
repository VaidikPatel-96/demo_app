# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        self.calculate_percentage()
        # self.set_status()
        self.set_grade()

    def calculate_percentage(self):
        if self.subjects:
            total_marks = sum([subject.marks for subject in self.subjects])
            self.percentage = total_marks / len(self.subjects) if len(self.subjects) > 0 else 0
        else:
            self.percentage = 0

    # def set_status(self):
    #     if self.percentage >= 35:
    #         self.status = "Pass"
    #     else:
    #         self.status = "Fail"
    
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


