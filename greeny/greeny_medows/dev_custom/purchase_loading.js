
frappe.ui.form.on('Purchase Loading', {

    validate: function(frm, cdt, cdn){
        console.log("gfdguhiu")
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
        frm.doc.loading_details_table.forEach(function (d) { lo_amount += d.rate; });
        cur_frm.set_value("greeny_loading_amount", lo_amount);
        refresh_field("greeny_loading_amount");


        var other_amount = 0;
        frm.doc.others_loading.forEach(function (d) { other_amount += d.rate; });
        cur_frm.set_value("others_loading_amount", other_amount);
        refresh_field("others_loading_amount");


        var total_amount = 0;
        total_amount=cur_frm.doc.greeny_loading_amount + cur_frm.doc.others_loading_amount
        cur_frm.set_value("total_loading_amount", total_amount);

        

},
after_save: function(frm){
    console.log("aaadsds")

    if(cur_frm.doc.coconut_qty > cur_frm.doc.total_loading_qty){
        console.log("aaa")
        msgprint("Loading Coconat is less then Total Coconant")
    }
    if(cur_frm.doc.coconut_qty < cur_frm.doc.total_loading_qty){
        msgprint("Loading Coconat is higher then Total Coconant")
        console.log("aaaddd")

    }
   

}


})