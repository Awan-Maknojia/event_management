# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventBooking(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from event.ticketing.doctype.event_booking_attendee.event_booking_attendee import EventBookingAttendee
        from frappe.types import DF

        amended_from: DF.Link | None
        attendee: DF.Table[EventBookingAttendee]
        currency: DF.Link | None
        event: DF.Link
        total_amount: DF.Currency
        user: DF.Link
    # end: auto-generated types

    def validate(self):
        self.set_total()
        self.set_currency()

    def set_total(self):
        self.total_amount = 0

        for attendee in self.attendee:
            self.total_amount += attendee.amount

    def set_currency(self):
        self.currency = self.attendee[0].currency
        
    def on_submit(self):
        self.generate_tickets()
        
    def generate_tickets(self):
        for attendee in self.attendee:
            ticket = frappe.new_doc("Event Ticket")
            ticket.event = self.event
            ticket.booking = self.name
            ticket.ticket_type = attendee.ticket_type
            ticket.attendee_name = attendee.full_name
            ticket.insert()
    
    # def on_cancel(self):
    #     self.cancel_tickets()
