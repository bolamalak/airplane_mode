from frappe import _

def get_data():
    return {
        "fieldname": "airline",
        "transactions": [
            {
                "label": _("Airplanes"),
                "items": ["Airplane"],
            },
        ],
    }
