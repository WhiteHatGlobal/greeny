

function set_uom(frm,cdt,cdn){
	let row=locals[cdt][cdn];
	if(row.item_code){
        frappe.db.get_value("Item", {"name": row.item_code}, ["default_unit_of_measure_2"], (r) => {
            frappe.model.set_value(cdt, cdn, "uom_2", r.default_unit_of_measure_2);
        });
        if(cur_frm.doc.bag_type=="No bag"){
           
            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.weight_without_bag)
            let net_weight = co_count -((co_count/100)*3)
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }
        else if(cur_frm.doc.bag_type == "Domestic"){

            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_domestic)
            let net_weight = co_count -((co_count/100)*3)
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }
         else {
          

            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_international)
            let net_weight = co_count -((co_count/100)*3)
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }
   
}
}
frappe.ui.form.on('Sales Invoice Item', {
    item_code:function(frm,cdt,cdn){
    set_uom(frm,cdt,cdn);
},

})