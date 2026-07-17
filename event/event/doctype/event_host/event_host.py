# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EventHost(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from event.event.doctype.social_media_link.social_media_link import SocialMediaLink
		from frappe.types import DF

		about: DF.TextEditor | None
		address: DF.SmallText | None
		country: DF.Link | None
		data_pqge: DF.Data | None
		logo: DF.AttachImage | None
		social_media_links: DF.Table[SocialMediaLink]
	# end: auto-generated types
	pass
