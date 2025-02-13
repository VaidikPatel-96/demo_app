import frappe
from frappe.utils import today

def check_overdue_books():
    overdue_books = frappe.get_all(
        "Library Transaction",
        filters={ "date": ("<", today())},
        fields=["name", "library_member", "date"],
    )

    for transaction in overdue_books:
        frappe.sendmail(
            recipients=frappe.get_value(
                "Library Member",
                transaction.library_member,
                "email",
            ),
            subject="Overdue Book",
            message=f"Book {transaction.name} was due on {transaction.date}.",

        )