# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customerdemo(Document):
	pass
# import frappe

# def update_customer_group_count(doc, method):
#     if doc.customer_group:
#         # Count the number of customers in the same group
#         customer_count = frappe.db.count("Customerdemo", filters={"customer_group": doc.customer_group})
#         doc.customer_group_count = customer_count  # Update the custom field
