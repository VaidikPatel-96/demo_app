import frappe
from frappe.utils import nowdate, add_days
from frappe.core.doctype.communication.email import make

def mark_expired_memberships():
    """Marks library memberships as expired if their to_date has passed"""
    expired_memberships = frappe.get_all(
        "Library Membership",
        filters={"to_date": ("<", nowdate()), "docstatus": 1},
        fields=["name"]
    )

    for membership in expired_memberships:
        doc = frappe.get_doc("Library Membership", membership.name)
        doc.status = "Expired"
        doc.save()

    frappe.msgprint(f"{len(expired_memberships)} memberships marked as expired.")

def notify_due_books():
    """Send notifications to members with books due within 2 days"""
    due_books = frappe.get_all("Library Transaction",
        filters={"type": "Issue", "due_date": ("<=", add_days(nowdate(), 2))},
        fields=["library_member", "article", "due_date"]
    )

    for book in due_books:
        member = frappe.get_doc("Library Member", book.library_member)
        make(
            recipients=member.email,
            subject="Book Due Reminder",
            content=f"Dear {member.full_name}, the book '{book.article}' is due on {book.due_date}. Please return it on time.",
            send_email=True
        )

    frappe.msgprint(f"{len(due_books)} members notified of due books.")

def auto_return_overdue_books():
    """Automatically marks overdue books as returned"""
    overdue_books = frappe.get_all("Library Transaction",
        filters={"type": "Issue", "due_date": ("<", add_days(nowdate(), -7))},
        fields=["name", "article"]
    )

    for transaction in overdue_books:
        doc = frappe.get_doc("Library Transaction", transaction.name)
        doc.type = "Return"
        doc.save()
    
    frappe.msgprint(f"{len(overdue_books)} overdue books auto-returned.")

def generate_monthly_report():
    """Generates a monthly summary of issued and returned books"""
    issued_count = frappe.db.count("Library Transaction", {"type": "Issue"})
    returned_count = frappe.db.count("Library Transaction", {"type": "Return"})

    report = f"Library Report:\nIssued Books: {issued_count}\nReturned Books: {returned_count}"

    frappe.log_error(report, "Monthly Library Report")
