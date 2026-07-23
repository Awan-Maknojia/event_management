// Copyright (c) 2026, Awan Maknojia and contributors
// For license information, please see license.txt

frappe.ui.form.on("AX Event", {
    refresh(frm) {
        frappe.call("frappe.geo.country_info.get_country_timezone_info").then(({ message }) => {
            frm.fields_dict.time_zone.set_data(message.all_timezones);
        });
        frm.add_custom_button(__("Start Check In"), () => {

            frappe.prompt({
                label: 'Track',
                fieldname: 'track',
                fieldtype: 'Link',
                options: 'Event Track'
            }, (values) => {
                const track = values.track;
                new frappe.ui.Scanner({
                    dialog: true,
                    multiple: false,
                    on_scan(data) {
                        const ticket_id = data.decodedText;
                        frm.call("check_in", { ticket_id, track }).then(() => {
                            frappe.show_alert(__("Check In Complete!"))
                            frm.refresh();
                        }).catch(() => {
                            frappe.utils.play_sound("error")
                        })
                    }
                });
            })

        })
        const button_label = frm.doc.published ? __("Unpublish") : __("Publish");
        frm.add_custom_button(__(button_label), function () {
            frm.set_value("published", !frm.doc.published);
            frm.save();
        },);
    },
});