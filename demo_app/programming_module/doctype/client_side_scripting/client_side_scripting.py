# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import _ 

class ClientSideScripting(Document):
	def get_student_data(self):
		pass
# 		data = frappe.get_all('Student',
# 			filters={'name': 'std-0016'},
# 				fields=['enrollmentdate', 'studentname', 'id', 'bod']
# 			)
# 		frappe.msgprint("The student name is {0} and enrollment date is {1}".format(data[0].studentname,data[0].enrollmentdate))
# 		return data
	
# import frappe
# from frappe.model.document import Document

# class ClientSideScripting(Document):
#     def get_student_data(self):
#         data = frappe.get_all(
#             'Student',
#             filters={'name': 'std-0016'},  # Fetch specific student
#             fields=['enrollment_date', 'student_name', 'id', 'bod']  # Ensure these fields exist
#         )

#         if data:
#             student = data[0]  # Get first (and only) record
#             frappe.msgprint("The student name is {0} and enrollment date is {1}".format(
#                 student.get('student_name', 'N/A'),  # Use .get() to avoid KeyError
#                 student.get('enrollment_date', 'N/A')
#             ))
#         else:
#             frappe.msgprint("Student not found.")

#         return data


# 		data = frappe.get_all('Student',
# 			filters={'name': 'std-0016'},
# 				fields=['enrollmentdate', 'studentname', 'id', 'bob']
# 			)
# 		frappe.msgprint()
# 		return data

# @frappe.whitelist()
# def frappe_call(msg):
# 	import time
# 	time.sleep(5)
	# frappe.msgprint(msg)




    
                        
			
                
	
    
 
 	# frappe.msgprint("The First name is {0} and age is {1}").format(doc.firstname,doc.age)