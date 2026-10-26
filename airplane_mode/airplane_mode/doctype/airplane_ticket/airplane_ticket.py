import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
        from frappe.types import DF

        add_ons: DF.Table[AirplaneTicketAddonItem]
        amended_from: DF.Link | None
        departure_date: DF.Date
        departure_time: DF.Time
        destination_airport: DF.Link
        destination_airport_code: DF.Data
        duration_of_flight: DF.Duration
        flight: DF.Link
        flight_price: DF.Currency
        gate_number: DF.Data | None
        passenger: DF.Link
        source_airport: DF.Link
        source_airport_code: DF.Data
        status: DF.Literal["Booked", "Checked-In", "Boarded"]
        total_amount: DF.Currency
    # end: auto-generated types

    def validate(self):
        total_add_ons = sum(item.amount for item in self.add_ons)
        self.total_amount = self.flight_price + total_add_ons
        
        seen = set()
        unique_add_ons = []
        for item in self.add_ons:
            if item.item not in seen:
                seen.add(item.item)
                unique_add_ons.append(item)
        if len(unique_add_ons) != len(self.add_ons):
            self.add_ons = unique_add_ons

        if self.flight:
            airplane_name = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
            if airplane_name:
                capacity = frappe.db.get_value("Airplane", airplane_name, "capacity")
                ticket_count = frappe.db.count("Airplane Ticket", {"flight": self.flight, "docstatus": 0})
                if ticket_count >= capacity:
                    frappe.throw(f"This flight is full! Airplane capacity is {capacity}.")

    def before_insert(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{random_number}{random_letter}"

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("You cannot submit an Airplane Ticket unless the status is 'Boarded'.")