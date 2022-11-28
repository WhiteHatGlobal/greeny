import frappe

@frappe.whitelist()
def purchase_loading(name, date, supplier, coconant):
    
    doc=frappe.new_doc("Purchase Loading")
    doc.update({
        "purchase_invoice":name,
        "date":date,
        "supplier":supplier,
        "coconut_qty":coconant
    })
    doc.save(ignore_permissions=True)
    return purchase_tranport(name)

def purchase_tranport(name):
    frappe.errprint(name)
    doc=frappe.new_doc("Purchase Transport")
    doc.update({
        "purchase_invoice":name,
        # "date":date,
        # "supplier":supplier,
        # "coconut_qty":coconant
    })
    doc.save(ignore_permissions=True)