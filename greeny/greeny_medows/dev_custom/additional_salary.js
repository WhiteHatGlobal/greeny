frappe.ui.form.on('Additional Salary',{
    after_save: function(frm, cdt, cdn){
        var d = locals[cdt][cdn];
        let amount =0
        frm.doc.loading_details.forEach(function(d){amount +=d.amount});
        cur_frm.set_value("amount",amount);
        refresh_field(amount)
    }
})