function set_uom(frm,cdt,cdn){
	let row=locals[cdt][cdn];
	if(row.item_code){
        frappe.db.get_value("Item", {"name": row.item_code}, ["default_unit_of_measure_2"], (r) => {
            frappe.model.set_value(cdt, cdn, "uom2", r.default_unit_of_measure_2);
        });
        
   
}
}
frappe.ui.form.on('Stock Entry Detail', {
    item_code:function(frm,cdt,cdn){
    set_uom(frm,cdt,cdn);
},

})