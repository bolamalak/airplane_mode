# Copyright (c) 2026, Bola Malak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Shop(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		area: DF.Float
		contract_expiry: DF.Date
		is_occupied: DF.Check
		rent_amount: DF.Currency
		shop_name: DF.Data
		shop_number: DF.Data
		shop_type: DF.Link
		tenant: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Shop"
