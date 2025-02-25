# # Copyright (c) 2025, D-codE and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Studentcard(Document):
	
	# # pass

	# def validate(self, method=None):
		
	# 	student = frappe.get_doc("Student", self.id)
		
	# 	if not student:
	# 		raise frappe.ValidationError(f"Student with name {self.studentname} not found!")

	# 	self.studentname = student.studentname
		
	# 	for subject in student.subjects:

	# 		self.append("subjects", {
	# 			"subjectname": subject.subjectname,
	# 			"marks": subject.marks
	# 		})
        


    def validate(self, method=None):
        student = frappe.get_doc("Student", self.id)

        if not student:
            raise frappe.ValidationError(f"Student with name {self.studentname} not found!")

        self.studentname = student.studentname

        max_marks = 100 
        total_marks_obtained = 0
        total_max_marks = 0
        self.subjects = []

        for subject in student.subjects:
            percentage = (subject.marks / max_marks) * 100 if max_marks > 0 else 0

            self.append("subjects", {
                "subjectname": subject.subjectname,
                "marks": subject.marks,
                "percentage": percentage
            })

            total_marks_obtained += subject.marks
            total_max_marks += max_marks
        self.percentage = (total_marks_obtained / total_max_marks) * 100 if total_max_marks > 0 else 0

