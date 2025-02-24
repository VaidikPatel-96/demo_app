# import frappe

# def validate_student(doc, method):
#     total_marks = 0
#     max_marks = 0

#     # Ensure subjects exist in the child table
#     if doc.subjects:
#         for subject in doc.subjects:
#             total_marks += int(subject.marks)  # Convert to int to avoid TypeError
#             max_marks += int(subject.maxmarks)

#         # Calculate percentage
#         doc.percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0

#         # Set status based on percentage
#         if doc.percentage < 33:
#             doc.status = "Failed"
#         elif 33 <= doc.percentage <= 50:
#             doc.status = "Pass"
#         else:
#             doc.status = "Excellent"

import frappe

def validate_student(doc, method):
    """Calculate percentage and update status in Student Doctype."""
    
    if not doc.subjects:
        doc.percentage = 0
        doc.status = "Failed"
        return

    total_marks = 0
    max_marks = len(doc.subjects) * 100  

    for subject in doc.subjects:
        if hasattr(subject, "marks"):
            if subject.marks < 0:
                frappe.throw(f"Marks for {subject.subjectname} cannot be negative.")
            if subject.marks > 100:
                frappe.throw(f"Marks for {subject.subjectname} cannot be more than 100.")
            total_marks += subject.marks  
        else:
            frappe.throw("Missing 'marks' field in Subject Details Doctype.")

    doc.percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0

    if doc.percentage < 33:
        doc.status = "Failed"
    elif 33 <= doc.percentage <= 50:
        doc.status = "Pass"
    else:
        doc.status = "Excellent"

    frappe.msgprint(f"Percentage calculated: {doc.percentage:.2f}%. Status updated to {doc.status}")
