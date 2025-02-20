import frappe

def before_insert(doc, method):
    if doc.customer_group:
        count = frappe.db.count('Customer1', {'customer_group': doc.customer_group})
        doc.customer_group_count = count
