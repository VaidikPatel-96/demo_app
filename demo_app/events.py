
# import frappe

# def validate_student(doc, method):
#     """
#     Calculates the percentage from child table marks and updates the student's status.
#     """
#     total_marks = 0
#     max_marks = 0

#     # Iterate through subjects and ensure marks are converted to integers
#     for subject in doc.subjects:
#         marks_obtained = int(subject.marks) if subject.marks else 0
#         max_possible_marks = int(subject.maxmarks) if subject.maxmarks else 0

#         total_marks += marks_obtained
#         max_marks += max_possible_marks

#     # Compute percentage
#     doc.percentage = (total_marks / max_marks * 100) if max_marks else 0

#     # Update status based on percentage
#     if doc.percentage < 33:
#         doc.status = "Failed"
#     elif 33 <= doc.percentage <= 50:
#         doc.status = "Pass"
#     else:
#         doc.status = "Excellent"
