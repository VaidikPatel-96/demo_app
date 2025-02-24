# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _ 

class ClientSideScripting(Document):
	def validate(self):
		frappe.msgprint(
			self.student)
		linked_student = frappe.get_doc("Student", self.student)
		print("8888888888",linked_student)
		frappe.msgprint(
			linked_student.studentname)
		print("8888888888",linked_student.studentname)
		frappe.msgprint(
			"The student name is {0} and enrollment date is {1}".format(linked_student.studentname, linked_student.enrollmentdate)
		)
		print("8888888888",linked_student.enrollmentdate)
		frappe.msgprint(
			linked_student.grade)
		print("8888888888",linked_student.grade)

		frappe.msgprint(
			linked_student.status)
		print("8888888888",linked_student.status)

		for return_subject in linked_student.subjects:
			frappe.msgprint(return_subject.subjectname)
			print("8888888888",linked_student.subjects)

		
		# for role in self.get("subjects"):
		# 	frappe.msgprint(
		# 		role.subjectname)
		# print("7777777777",self.get("subjects"))
		# for linked_student in get("student"):
		# 	frappe.msgprint(
		# 		linked_student.subjectname)
			
	
	

		
	
		

		# pass
	# 	data = frappe.get_list('Student',
	# 		filters={'name': 'std-0016'},
	# 			fields=['enrollmentdate', 'studentname', 'id', 'bod']
	# 		)
	# 	print("______________",data)
	# 	frappe.msgprint("The student name is {0} and enrollment date is {1}".format(data[0].studentname,data[0].enrollmentdate))
	# 	return data
	
	# def validate(self):

	


# @frappe.whitelist()
# def frappe_call(msg):
# 	import time
# 	time.sleep(5)
	# frappe.msgprint(msg)

# class ClientSideScripting(Document):
# 	def validate(self):
# 		# pass
# 		data = frappe.get_list('Student',
# 			filters={'name': 'std-0016'},
# 				fields=['enrollmentdate', 'studentname', 'id', 'bod']
# 			)
# 		print("______________",data)
# 		frappe.msgprint("The student name is {0} and enrollment date is {1}".format(data[0].studentname,data[0].enrollmentdate))
# 		return data
	


    
                        
			
                
	
    
 
 	# frappe.msgprint("The First name is {0} and age is {1}").format(doc.firstname,doc.age)