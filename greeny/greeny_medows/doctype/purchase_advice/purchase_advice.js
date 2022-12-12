// Copyright (c) 2022, White Hat Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Advice', {
	validate: function(frm, cdt, cdn){
		if(cur_frm.doc.transport_type=="Own Vehicle"){

        var d = locals[cdt][cdn];
        var qty = 0;
        frm.doc.loading_details_table.forEach(function (d) { qty += d.qty; });
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
        frm.doc.loading_details_table.forEach(function (d) { lo_amount += d.amount; });
        cur_frm.set_value("greeny_loading_amount", lo_amount);
        refresh_field("greeny_loading_amount");


        var other_amount = 0;
        frm.doc.others_loading.forEach(function (d) { other_amount += d.amount; });
        cur_frm.set_value("others_loading_amount", other_amount);
        refresh_field("others_loading_amount");


        var total_amount = 0;
        total_amount=cur_frm.doc.greeny_loading_amount + cur_frm.doc.others_loading_amount
        cur_frm.set_value("total_loading_amount", total_amount);
        if(cur_frm.doc.ending_km){
            total=cur_frm.doc.ending_km - cur_frm.doc.starting_km
            cur_frm.set_value("total_km", total);
        }

        if(cur_frm.doc.weight){
            total=cur_frm.doc.weight * cur_frm.doc.transport_rate
            cur_frm.set_value("transport_charges", total);
        }

	}

    if(cur_frm.doc.bag_type=="No bag"){
           

        let co_count = cur_frm.doc.weight-(cur_frm.doc.no_of_bags*cur_frm.doc.weight_without_bag)
        let net_weight = co_count -((co_count/100)*3)
        cur_frm.set_value("net_weight", net_weight);
    }
    else if(cur_frm.doc.bag_type == "Domestic"){

        let co_count = cur_frm.doc.weight-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_domestic)
        let net_weight = co_count -((co_count/100)*3)
        cur_frm.set_value("net_weight", net_weight);
      
    }
     else {
        

        let co_count = cur_frm.doc.weight-(cur_frm.doc.no_of_bags*cur_frm.doc.bag_weight_international)
        let net_weight = co_count -((co_count/100)*3)
        cur_frm.set_value("net_weight", net_weight);
       
    }

}

});


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







function account_head(frm,cdt,cdn){
	let row=locals[cdt][cdn];
    console.log("vvvvvvv")
    frappe.call({
        method:"greeny.greeny_medows.doctype.purchase_advice.purchase_advice.account_head",
        args: {
            "expence_type":row.expense_claim_type
        },
        callback(r){
            frappe.model.set_value(cdt, cdn, "account_head", r.message);
        }
    })
    
}


frappe.ui.form.on('Expense Details', {
    expense_claim_type:function(frm,cdt,cdn){
    account_head(frm,cdt,cdn);
},

})


