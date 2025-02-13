# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 
from frappe.model.document import Document


class Server_side(Document):
	# pass
# class Server_side(Document):

 # 1  #####  server side events ######   
	# def validate(self):
	# 	frappe.msgprint("hello validate")
    
	# def before_save(self):
	# 	frappe.throw("hello 'before_save'event")


	# def before_insert(self):
	# 	frappe.msgprint("hello 'before_insert'event")

	# def after_insert(self):
	#  	frappe.msgprint("hello 'after_insert'event")
	# def on_update(self):
	#  	frappe.msgprint("hello 'on_update'event")

	# def before_submit(self):
	#  	frappe.throw("hello 'before_submite'event")

	# def on_submit(self):
	#  	frappe.msgprint("hello 'on_submite'event")

	# def on_cancel(self):
	#  	frappe.msgprint("hello 'on_cancel'event")

	# def on_trash(self):
	#  	frappe.msgprint("hello 'on_trash'event")

	# def after_delete(self):
	#  	frappe.msgprint("hello 'after_delete'event")


# 2   ###### value feching   ######

	# def validate(self):
	# 	frappe.msgprint(_("Hello my full name is '{0}' ").format(
	# 		self.firstname + " "+ self.middlename+" "+self.lastname))
    
	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}.The family member name is '{1}'and relation is '{2}'").format(
	# 				row.idx,row.name1,row.relation) )
    
		# def validate(self):
		# 	self.get_document()

		# def get_document(self):
		# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
		# 	frappe.msgprint(_("The First name is {0} and age is {1}").format(doc.firstname,doc.age))



    
##############frappe.get_doc(doctype, name) #######
	#Return a document object of the record identified by doctype and name

		# frappe.get_doc(doctype, name)

		# def validate(self):
		# 	self.get_document

		# def get_document(self):
		# 	doc = frappe.get_doc('Client Side Scripting', self.cllent_side_doc)
		# 	frappe.msgprint(_("The First name is {0} and age is {1}").format(doc.firstname,doc.age))


#  4   //// frappe.new_doc (doctype)////

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc=frappe.new_doc('Client Side Scripting')
	# 	doc.firstname='jake'
	# 	doc.lastname='jay'
	# 	doc.age= 15	
	# 	doc.append("family_members",{  	"name1":"vivek",
	# 						   			"relation":"bro",
	# 									"age":24
	# 						 		})
	# 	doc.insert()


 #  5 ///////delete_doc(doctype,name) //////////

# frappe.delete_doc(doctype, name)
	
	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', 'PE-0056')
		

# ///////Document Methods ////////////


	def validate(self):
		self.new_document()

	def new_document(self):
		doc = frappe.new_doc('Client Side Scripting')
		doc.firstname='bally'
		doc.age=25
		# doc.insert()
		doc.append("family_members",{  	"name1":"vivek",
							   			"relation":"bro",
										"age":24
						 			})
		doc.insert()
    
	
	
# ///////////////doc.save()//////////////////////////////////////

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.firstname='diya'
	# 	doc.age=26
	# 	doc.save()

	# 	doc.save(
	# 		ignore_permissions=True, #ingnore write permissions during insert
	# 		ignore_version=True #do not create a version recode
	# 	)
    
#///////////doc.delete()////////////////////////////////

	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting','PE-0042')
	# 	doc.delete()

#///////////doc.db_set()/////////////////////////////////

	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting','PE-0060')
	# 	doc.db_set('age',46)

	

# 7 ///////////Database API ////////////////////////////////


	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 			filters={
	# 				'enable': 1
	# 			},
	# 			fields=['firstname','age']				   
	# 			)
	# 	for d in doc:
	# 		frappe.msgprint(("The parent first name is {0} and is {1}").format(d.firstname,d.age))
    
# 8 ///////////////////////////////////////

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	firstname, age=frappe.db.get_value('Client Side Scripting','PE-0060',['firstname','age'])
	# 	frappe.msgprint(("The parent First Name is {0} and age is {1}").format(firstname,age))		


# 9 //////////////////////////////////////////////////////////

	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','PE-0060','age',80)
	# 	firstname, age=frappe.db.get_value('Client Side Scripting','PE-0031',['firstname','age'])
	# 	frappe.msgprint(_("The parent First Name is {0} and age is {1}").format(firstname,age))


# 10 ////////////////db.exists(doctype,name)/////////////////////////////////

	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','PE-00311'):
	# 		frappe.msgprint("the Document is Exists in Database")
	# 	else:
	# 		frappe.msgprint("THe document does not Exists in Database")


# 11 ///////////b.count(doctype,filters)//////////////////////////////////////////////////////

	# def validate(self):
	# 	doc_count=frappe.db.count('Client Side Scripting',{'enable': 1})
	# 	frappe.msgprint(("The enable Document Count is {0}").format(doc_count))
    

# 12 ////db.sql(query,filters,as_dict)/////////////////////////////////////////////////////////////////////////

	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data=frappe.db.sql("""
	# 				 		  SELECT
	# 				 				firstname,
	# 				 				age
	# 				 			FROM
	# 				 				`tabClient Side Scripting`
	# 				 			WHERE
	# 				 				enable = 1
	# 				 	""", as_dict=1)
	# 	for d in data:
	# 		frappe.msgprint(_("The perent Firatname is {0} and last name is {1}").format(d.firstname,d.age))	
    


# 13  ///////// Server side call ///////////////////////////////////////

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	# frappe.msgprint(msg)

	# 	self.mob_no=9924052046

		# return "Hi this message from frm_call"