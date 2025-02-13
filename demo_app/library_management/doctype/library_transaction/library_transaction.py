# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class LibraryTransaction(Document):
# 	pass
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        book=frappe.get_doc("Library Book",self.book)
        if book.status != "Available":
            frappe.throw("Book is not available")
            book.status="Issued"
            book.save()
        else:
            frappe.throw("Book is not available")
        
