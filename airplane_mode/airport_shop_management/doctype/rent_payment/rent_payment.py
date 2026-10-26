# Copyright (c) 2026, Bola Malak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		month: DF.Data | None
		payment_date: DF.Date
		shop: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Rent Payment"
