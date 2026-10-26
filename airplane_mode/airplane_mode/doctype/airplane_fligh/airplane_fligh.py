import frappe
from frappe.model.document import Document

class AirplaneFlight(Document):
    def on_submit(self):
        self.status = "Completed"
        self.db_update()

import frappe

def update_ticket_gate_numbers(doc, method=None):
    frappe.enqueue(
        "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight.update_tickets",
        flight=doc.name,
        gate_number=doc.gate_number
    )

def update_tickets(flight, gate_number):
    tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight})
    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", gate_number)