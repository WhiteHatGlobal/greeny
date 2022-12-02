import frappe

@frappe.whitelist()
def purchase_loading(name, date, supplier, coconant, trans_type, vehicle, driver):
    # frappe.errprint(rounded_total)
    
    doc=frappe.new_doc("Purchase Loading")
    doc.update({
        "purchase_invoice":name,
        "date":date,
        "supplier":supplier,
        "coconut_qty":coconant
    })
    doc.save(ignore_permissions=True)
    return purchase_tranport(name,  trans_type, vehicle, driver, supplier)

def purchase_tranport(name, trans_type, vehicle, driver, supplier):
    frappe.errprint("hvghhhhhh")
    # frappe.errprint(rounded_total)


    if(trans_type == "Own Vehicle"):
        frappe.errprint("fdvgdf")
        doc=frappe.new_doc("Purchase Transport")
        doc.update({
            "purchase_invoice":name,
            "transport_type":trans_type,
            "vehicle":vehicle,
            "driver_whg":driver
        })
        doc.save(ignore_permissions=True)
    else:
        doc=frappe.new_doc("Purchase Transport")
        doc.update({
            "purchase_invoice":name,
            "transport_type":trans_type,
            "vehicle_number":vehicle,
            "driver_whg":driver,
            "transport_supplier": supplier,
            # "bill_amount":rounded_total,

        })
        doc.save(ignore_permissions=True)

def purchase_transport(self, event):

        if (self.transport_type == "Other Vehicle"):
            doc=frappe.new_doc("Purchase Invoice")
            item=[{
                "item_code":"Transport Item",
                "qty":self.coconut_qty,
                
            }]
            doc.update({
                "supplier":self.supplier,
                "items":item,
                "transport_type":self.transport_type,
                "vehicle_number":self.vehicle_number,
                "driver_name":self.driver_whg
            })
            doc.save(ignore_permissions=True)
        else:
            doc=frappe.new_doc("Purchase Invoice")
            item=[{
                "item_code":"Transport Item",
                "qty":self.coconut_qty,
                
            }]
            doc.update({
                "supplier":self.supplier,
                "items":item,
                "transport_type":self.transport_type,
                "vehicle":self.vehicle_number,
                "driver_name":self.driver_whg
            })
            doc.save(ignore_permissions=True)
        