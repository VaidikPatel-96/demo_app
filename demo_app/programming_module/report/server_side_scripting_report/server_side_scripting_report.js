// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

frappe.query_reports["Server side scripting Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Server side scripting"),
			"fieldtype": "Link",
			"options": "Server_side"
		},
		{
			"fieldname": "dob",
			"label": __("DOB"),
			"fieldtype": "Date",
			
		},
		{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Int",
			
		}
	]
};
