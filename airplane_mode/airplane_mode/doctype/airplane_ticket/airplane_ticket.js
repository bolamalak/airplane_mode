frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            frappe.prompt([
                {
                    fieldname: 'seat',
                    label: 'Seat Number',
                    fieldtype: 'Data',
                    reqd: 1
                }
            ], function(values) {
                frm.set_value('seat', values.seat);
            }, __('Select Seat'), __('Assign'));
        });
    }
});