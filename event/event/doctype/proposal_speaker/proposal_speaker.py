# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProposalSpeaker(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		first_name: DF.Data | None
		last_name: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types
	pass
