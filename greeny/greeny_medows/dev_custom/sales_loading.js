
frappe.ui.form.on('Sales Loading', {

    validate: function(frm, cdt, cdn){
        var d = locals[cdt][cdn];
        var qty = 0;
        frm.doc.loading_details.forEach(function (d) { qty += d.qty; });
        cur_frm.set_value("total_greeny", qty);
        refresh_field("total_greeny");

        var other_qty = 0;
        frm.doc.others_loading.forEach(function (d) { other_qty += d.qty; });
        cur_frm.set_value("total_others", other_qty);
        refresh_field("total_others");

        var total = 0;
        total=cur_frm.doc.total_greeny + cur_frm.doc.total_others
        cur_frm.set_value("total_loading_qty", total);

        var lo_amount = 0;
        frm.doc.loading_details.forEach(function (d) { lo_amount += d.amount; });
        cur_frm.set_value("greeny_loading_amount", lo_amount);
        refresh_field("greeny_loading_amount");


        var other_amount = 0;
        frm.doc.others_loading.forEach(function (d) { other_amount += d.amount; });
        cur_frm.set_value("others_loading_amount", other_amount);
        refresh_field("others_loading_amount");


        var total_amount = 0;
        total_amount=cur_frm.doc.greeny_loading_amount + cur_frm.doc.others_loading_amount
        cur_frm.set_value("total_loading_amount", total_amount);

        

},
after_save: function(frm){

    if(cur_frm.doc.coconut_qty > cur_frm.doc.total_loading_qty){
        msgprint("Loading Coconat is less then Total Coconant")
    }
    if(cur_frm.doc.coconut_qty < cur_frm.doc.total_loading_qty){
        msgprint("Loading Coconat is higher then Total Coconant")

    }
   
}
})


function amount(frm,cdt,cdn){
	let row=locals[cdt][cdn];
    let tot_amount=row.qty * row.rate
            frappe.model.set_value(cdt, cdn, "amount", tot_amount);
    
}

frappe.ui.form.on('Loading Details', {
    qty:function(frm,cdt,cdn){
    amount(frm,cdt,cdn);
},
rate:function(frm,cdt,cdn){
    amount(frm,cdt,cdn);
},
})


function ot_amount(frm,cdt,cdn){
	let row=locals[cdt][cdn];
    let tot_amount=row.qty * row.rate
            frappe.model.set_value(cdt, cdn, "amount", tot_amount);
    
}


frappe.ui.form.on('Loading Others', {
    qty:function(frm,cdt,cdn){
    ot_amount(frm,cdt,cdn);
},
rate:function(frm,cdt,cdn){
    ot_amount(frm,cdt,cdn);
},
})