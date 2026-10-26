import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "width": 150}
    ]

    airlines = frappe.get_all("Airline", fields=["name"])
    data = []
    total_revenue = 0

    for airline in airlines:
        flights = frappe.get_all("Airplane Flight", filters={"airplane": ["like", f"%{airline.name}%"]}, fields=["name"])
        flight_names = [f.name for f in flights]
        
        revenue = 0
        if flight_names:
            tickets = frappe.get_all("Airplane Ticket", 
                filters={"flight": ["in", flight_names], "docstatus": 1}, 
                fields=["sum(total_amount) as total"]
            )
            if tickets and tickets[0].total:
                revenue = tickets[0].total
        
        data.append({"airline": airline.name, "revenue": revenue})
        total_revenue += revenue

    report_summary = [{"value": total_revenue, "label": "Total Revenue", "datatype": "Currency", "indicator": "Green"}]
    
    chart = {
        "data": {
            "labels": [d["airline"] for d in data if d["revenue"] > 0],
            "datasets": [{"values": [d["revenue"] for d in data if d["revenue"] > 0]}]
        },
        "type": "donut"
    }

    return columns, data, None, chart, report_summary