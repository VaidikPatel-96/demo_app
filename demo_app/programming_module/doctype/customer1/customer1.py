# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customer1(Document):
	pass
import frappe

def before_insert(doc, method):
    if doc.customer_group:
        count = frappe.db.count('Customer1', {'customer_group': doc.customer_group})
        doc.customer_group_count = count
