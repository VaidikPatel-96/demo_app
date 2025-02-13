# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class Newserver_side(Document):
# 	pass
class ServerSideScripting(Document):
    
	def validate(self):
		frappe.msgprint("hello")