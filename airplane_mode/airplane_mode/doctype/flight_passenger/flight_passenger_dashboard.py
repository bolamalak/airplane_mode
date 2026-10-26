from frappe import _

def get_data():
    return {
        "fieldname": "passenger",
        "transactions": [
            {
                "label": _("Tickets"),
                "items": ["Airplane Ticket"],
            },
        ],
    }
