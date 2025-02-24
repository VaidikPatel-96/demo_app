# from frappe.model.document import Document
# from frappe.model.docstatus import DocStatus

# import frappe


# class LibraryMembership(Document):
#     # check before submitting this document
#     def before_submit(self):
#         exists = frappe.db.exists(
#             "Library Membership",
#             {
#                 "library_member": self.library_member,
#                 "docstatus": DocStatus.submitted(),
#                 # check if the membership's end date is later than this membership's start date
#                 "to_date": (">", self.from_date),
#             },
#         )
#         if exists:
#             frappe.throw("There is an active membership for this member")

#         # get loan period and compute to_date by adding loan_period to from_date
#         loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
#         self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
    def before_submit(self):
        if not self.from_date or not self.to_date:
            frappe.throw("Membership must have a valid From Date and To Date.")

        # Check if the member already has an active membership
        existing_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "to_date": (">=", self.from_date)
            }
        )
        if existing_membership:
            frappe.throw("Member already has an active membership!")
# import frappe
# from frappe.model.document import Document

# class LibraryMembership(Document):  # Example: Fetch Student data inside LibraryMembership
#     def show_student_data(self, student_id='std-0016'):
#         student = frappe.db.get_list(
#             'Student',
#             filters={'name': student_id},  # Get specific student
#             fields=['studentname', 'enrollmentdate', 'status']
#         )

#         if student:
#             student_data = student[0]
#             msg = f"Student Name: {student_data['studentname']} \nEnrollment Date: {student_data['enrollmentdate']} \nStatus: {student_data['status']}"
#             frappe.msgprint(msg)
#         else:
#             frappe.msgprint(f"Student {student_id} not found.")
