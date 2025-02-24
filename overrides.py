import frappe

def update_customer_group(doc, method):
    if doc.customer_group:
        customer_count = frappe.db.count("Customer", {"customer_group": doc.customer_group})
        doc.custom_customer_count_count = customer_count