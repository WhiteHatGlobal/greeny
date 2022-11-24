
frappe.ui.form.on('Purchase Receipt', {

        validate: function(frm, cdt, cdn){
            var d = locals[cdt][cdn];
            var total = 0;
            frm.doc.employee_work_details.forEach(function (d) { total += d.coconat_loading_count; });
            cur_frm.set_value("total_coconat_count", total);
            refresh_field("total_coconat_count");
    },

    total_coconat_count: function(frm){
        let  total_coconat= cur_frm.doc.total_qty
        let load_coconat = cur_frm.doc.total_coconat_count
        if (total_coconat >load_coconat)
            alert("Coconat Missing")
        if (total_coconat < load_coconat)
           alert("Load Coconat is High")

    }
    

})
