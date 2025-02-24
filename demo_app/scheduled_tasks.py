import frappe
from frappe.utils import nowdate, add_days
from datetime import datetime

def mark_expired_memberships():
    """Mark expired library memberships as inactive"""
    today = nowdate()
    expired_members = frappe.get_all(
        "Library Membership",
        filters={"to_date": ["<", today], "status": "Active"},
        fields=["name"]
    )

    for member in expired_members:
        frappe.db.set_value("Library Membership", member.name, "status", "Expired")
    
    frappe.db.commit()
    frappe.logger().info("Expired memberships have been marked.")

def auto_return_overdue_books():
    """Automatically return books that are overdue"""
    today = nowdate()
    overdue_books = frappe.get_all(
        "Library Transaction",
        filters={"due_date": ["<", today], "transaction_type": "Issue"},
        fields=["name", "library_member"]
    )

    for transaction in overdue_books:
        frappe.db.set_value("Library Transaction", transaction.name, "transaction_type", "Return")
    
    frappe.db.commit()
    frappe.logger().info("Overdue books have been returned.")

def generate_monthly_report():
    """Generate and send a monthly report"""
    total_members = frappe.db.count("Library Membership")
    total_books_issued = frappe.db.count("Library Transaction", {"transaction_type": "Issue"})
    
    report = f"""
    Monthly Library Report ({datetime.today().strftime('%B %Y')}):
    - Total Members: {total_members}
    - Total Books Issued: {total_books_issued}
    """
    
    frappe.sendmail(
        recipients=["admin@library.com"],  # Change to actual recipients
        subject="Monthly Library Report",
        message=report
    )

    frappe.logger().info("Monthly report generated and sent via email.")
