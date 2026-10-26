import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "airline",
            "label": "Airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "fieldname": "airplane_count",
            "label": "Airplane Count",
            "fieldtype": "Int",
            "width": 150
        }
    ]

    data = frappe.db.sql("""
        SELECT 
            airline AS airline, 
            COUNT(name) AS airplane_count
        FROM 
            `tabAirplane`
        GROUP BY 
            airline
        ORDER BY 
            airplane_count DESC
    """, as_dict=1)

    return columns, data