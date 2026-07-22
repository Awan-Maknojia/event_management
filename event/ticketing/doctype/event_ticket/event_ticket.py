# Copyright (c) 2026, Awan Maknojia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventTicket(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from event.ticketing.doctype.ticket_add_on_value.ticket_add_on_value import TicketAddonValue
        from frappe.types import DF

        add_ons: DF.Table[TicketAddonValue]
        amended_from: DF.Link | None
        attendee_name: DF.Data | None
        booking: DF.Link | None
        event: DF.Link
        qr_code: DF.AttachImage | None
        ticket_type: DF.Link | None
    # end: auto-generated types
    

    def before_submit(self):
        self.generate_qr_code()

    def generate_qr_code(self):
        # frappe.throw("HI")
       qr_data =make_qr_with_data(f"{self.name}")
       qr_code_file =frappe.get_doc({
            "doctype":"File",
            "content":qr_data,
            "attached_to_doctype": "Event Ticket",
            "attached_to_name":self.name,
            "attached_to_field": "qrcode",
            "file_name": f"ticket-qr-code-{self.name}.png"
            }).save()
       self.qr_code = qr_code_file.file_url
        
        
def make_qr_with_data(data: str) -> bytes:
            import io
            import qrcode
            from qrcode.image.styledpil import StyledPilImage
            from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
            qr = qrcode.QRCode(
                     version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(image_factory=StyledPilImage ,module_drawer=HorizontalBarsDrawer())
            output = io.BytesIO()
            img.save(output, format="PNG")
            return output.getvalue()