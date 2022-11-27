
frappe.ui.form.on('Purchase Invoice', {

    on_submit: function(){
        frappe.call({
			method:"greeny.greeny_medows.dev_custom.purchase_sales.purchase_loading",
			args: {
                
                "name":cur_frm.doc.name,
                "date":cur_frm.doc.due_date,
                "supplier":cur_frm.doc.supplier,
                "coconant":cur_frm.doc.number_of_coconant,
            },
            callback(r){
				console.log("fdgdg")
			}
		})
}




})
function set_uom(frm,cdt,cdn){
	let row=locals[cdt][cdn];
	if(row.item_code){

        frappe.db.get_value("Item", {"name": row.item_code}, ["default_unit_of_measure_2"], (r) => {
            frappe.model.set_value(cdt, cdn, "uom_2", r.default_unit_of_measure_2);
        });
        if(cur_frm.doc.bag_type=="No bag"){
           

            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.weight_without_bag)
            let net_weight = co_count -((co_count/100)*3)
            cur_frm.set_value("net_weight", net_weight);
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }
        else if(cur_frm.doc.bag_type == "Domestic"){

            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_domestic)
            let net_weight = co_count -((co_count/100)*3)
            cur_frm.set_value("net_weight", net_weight);
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }
         else {
            

            let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_international)
            let net_weight = co_count -((co_count/100)*3)
            cur_frm.set_value("net_weight", net_weight);
            frappe.model.set_value(cdt, cdn, "qty", net_weight);
            frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        }

        // let co_count = cur_frm.doc.gross_weight_whg-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_domestic)

        // let net_weight = co_count -((co_count/100)*3)
        // frappe.model.set_value(cdt, cdn, "qty", net_weight);
        // frappe.model.set_value(cdt, cdn, "qty2", cur_frm.doc.number_of_coconant);
        
}
}
frappe.ui.form.on('Purchase Invoice Item', {
    item_code:function(frm,cdt,cdn){
    set_uom(frm,cdt,cdn);
},

})













// frappe.ui.form.on('My Custom Settings', {

//     onload: function() {
    
//             frappe.model.with_doctype('Purchase Invoice', () => {
//             const meta = frappe.get_meta('Purchase Invoice');
    
//             const naming_series = meta.fields.find(df => df.fieldname === 'naming_series');
    
//             frm.set_df_property('my_custom_settings_selectio_field', 'options', naming_series.options);
//         });
    
//     },
    
//     });