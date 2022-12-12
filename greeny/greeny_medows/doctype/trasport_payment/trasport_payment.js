// Copyright (c) 2022, White Hat Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Trasport Payment', {
	validate: function(frm, cdt, cdn){
        var d = locals[cdt][cdn];
        var paid = 0;
        frm.doc.loading_payment_table.forEach(function (d) { paid += d.paid; });
        cur_frm.set_value("paid", paid);
        refresh_field("paid");

		var outstanding = 0;
        frm.doc.loading_payment_table.forEach(function (d) { outstanding += d.outstanding; });
        cur_frm.set_value("outstanding", outstanding);
        refresh_field("outstanding");

		if(cur_frm.doc.paid){
			if(cur_frm.doc.paid==cur_frm.doc.total_loading_amount){
				cur_frm.set_value("status", "Paid");
			}
			if(cur_frm.doc.paid<cur_frm.doc.total_loading_amount){
				cur_frm.set_value("status", "Partially Paid");
               
			}
		}
	}
});


function out_amount(frm,cdt,cdn){
	let row=locals[cdt][cdn];
    let outstanding_amount=row.amount - row.paid
            frappe.model.set_value(cdt, cdn, "outstanding", outstanding_amount);
    
}


frappe.ui.form.on('Loading Payment Table', {
    amount:function(frm,cdt,cdn){
    out_amount(frm,cdt,cdn);
},
paid:function(frm,cdt,cdn){
    out_amount(frm,cdt,cdn);
},
})