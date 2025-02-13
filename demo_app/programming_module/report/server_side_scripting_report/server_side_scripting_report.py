# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# import frappe
# from datetime import datetime, date

# def execute(filters=None):
#     columns = get_columns()
#     data = get_data(filters)
#     chart = get_chart_data(data)
    
#     return columns, data, None, chart

# def get_columns():
#     return [
#         {"fieldname": "name", "label": "Name", "fieldtype": "Link", "options": "Server_side", "width": 150},
#         {"fieldname": "dob", "label": "Date of Birth", "fieldtype": "Date", "width": 120},
#         {"fieldname": "age", "label": "Age", "fieldtype": "Int", "width": 80}
#     ]

# def get_data(filters):
#     conditions = []
#     values = {}

#     if filters.get("name"):
#         conditions.append("name = %(name)s")
#         values["name"] = filters["name"]

#     if filters.get("dob"):
#         conditions.append("dob = %(dob)s")
#         values["dob"] = filters["dob"]

#     condition_str = " AND ".join(conditions) if conditions else "1=1"

#     results = frappe.db.sql(f"""
#         SELECT name, dob, age
#         FROM tabServer_side
#         WHERE {condition_str}
#     """, values, as_dict=True)

#     return results

# def get_chart_data(data):
#     age_groups = {}

#     for row in data:
#         age = row.get("age")
#         if age is not None:
#             age_groups[age] = age_groups.get(age, 0) + 1  # Counting occurrences of each age

#     return {
#         "data": {
#             "labels": list(age_groups.keys()),  # X-axis (Ages)
#             "datasets": [{"name": "Number of Students", "values": list(age_groups.values())}]  # Y-axis (Count)
#         },
#         "type": "pie"  # Chart Type (Bar Chart)
# }

import frappe
from datetime import datetime, date

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart_data(data)
    
    return columns, data, None, chart

def get_columns():
    return [
        {"fieldname": "name", "label": "Name", "fieldtype": "Link", "options": "Server_side", "width": 150},
        {"fieldname": "dob", "label": "Date of Birth", "fieldtype": "Date", "width": 120},
        {"fieldname": "age", "label": "Age", "fieldtype": "Int", "width": 80}
    ]

def get_data(filters):
    conditions = []
    values = {}

    if filters.get("name"):
        conditions.append("name = %(name)s")
        values["name"] = filters["name"]

    if filters.get("dob"):
        conditions.append("dob = %(dob)s")
        values["dob"] = filters["dob"]

    condition_str = " AND ".join(conditions) if conditions else "1=1"

    results = frappe.db.sql(f"""
        SELECT name, dob, age
        FROM tabServer_side
        WHERE {condition_str}
    """, values, as_dict=True)

    return results

def get_chart_data(data):
    age_groups = {"≤ 45": 0, "> 45": 0}

    for row in data:
        age = row.get("age")
        if age is not None:
            if age <= 45:
                age_groups["≤ 45"] += 1
            else:
                age_groups["> 45"] += 1

    return {
        "data": {
            "labels": list(age_groups.keys()),  # "≤ 45" and "> 45"
            "datasets": [{"name": "Number of Students", "values": list(age_groups.values())}]
        },
        "type": "pie"  # Chart Type (Pie Chart)
    }
