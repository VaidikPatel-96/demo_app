# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class demo_1(Document):
# 	pass
class demo_1(Document):
    
	def validate(self):
		frappe.msgprint("hello")
