
frappe.ui.form.on('Purchase Transport', {
    
    validate: function(frm, cdt, cdn){
        if(cur_frm.doc.transport_type =="Own Vehicle"){
       let weight=cur_frm.doc.weight
       let rate=cur_frm.doc.rate
       let total=weight*rate
        cur_frm.set_value("transport_charges", total);
        // refresh_field("total_greeny");
        }
        if(cur_frm.doc.transport_type =="Other Vehicle"){
            console.log("aaa")
           let weight=cur_frm.doc.weight
           let rate=cur_frm.doc.rate
            let total=weight*rate
            cur_frm.set_value("bill_amount", total);
        }  

},
})
