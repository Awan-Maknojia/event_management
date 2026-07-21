# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventBookingAttendee(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        add_on_total: DF.Currency
        add_ons: DF.Link | None
        amount: DF.Currency
        currency: DF.Link
        email: DF.Data | None
        full_name: DF.Data | None
        number_of_add_ons: DF.Int
        parent: DF.Data
        parentfield: DF.Data
        parenttype: DF.Data
        ticket_type: DF.Link | None
    # end: auto-generated types
    
    # def before_save(self):
    #     self.add_on_total = self.get_add_on_total()


    def get_add_on_total(self):
        if not self.add_ons:
            return 0

        add_ons = frappe.get_cached_doc("Attendee Ticket Add-on",self.add_ons).add_ons
        return sum(row.price for row in add_ons)
    
    def get_number_of_add_on(self):
       	return len(frappe.get_cached_doc("Attendee Ticket Add-on",self.add_ons).add_ons)