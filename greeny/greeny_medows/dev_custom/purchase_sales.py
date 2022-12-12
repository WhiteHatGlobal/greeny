import frappe


# @frappe.whitelist()
# def purchase_loading(name, date, supplier, coconant, trans_type, vehicle, driver):
#     frappe.errprint("vgh")    
#     doc=frappe.new_doc("Purchase Loading")
#     doc.update({
#         "purchase_invoice":name,
#         "date":date,
#         "supplier":supplier,
#         "coconut_qty":coconant
#     })
#     doc.save(ignore_permissions=True)
    
#     return purchase_tranport(name,  trans_type, vehicle, driver, supplier)

# def purchase_tranport(name, trans_type, vehicle, driver, supplier):
#     frappe.errprint("hvghhhhhh")

#     if(trans_type == "Own Vehicle"):
#         frappe.errprint("fdvgdf")
#         doc=frappe.new_doc("Purchase Transport")
#         doc.update({
#             "purchase_invoice":name,
#             "transport_type":trans_type,
#             "vehicle":vehicle,
#             "driver_whg":driver,
#         })
#         doc.save(ignore_permissions=True)
#         frappe.msgprint("Purchase Transport and Purchase Loading are Created Successfully")
       
#     else:
#         doc=frappe.new_doc("Purchase Transport")
#         doc.update({
#             "purchase_invoice":name,
#             "transport_type":trans_type,
#             "vehicle_number":vehicle,
#             "driver_whg":driver,
#             "transport_supplier": supplier,
#             # "bill_amount":rounded_total,

#         })
#         doc.save(ignore_permissions=True)
#         frappe.msgprint("Purchase Transport and Purchase Loading are Created Successfully")

def purchase_transport(self, event):

        if (self.transport_type == "Other Vehicle"):
            doc=frappe.new_doc("Purchase Invoice")
            item=[{
                "item_code":"Transport Item",
                "qty":1,
                "rate":self.bill_amount
                
            }]
            doc.update({
                "supplier":self.supplier,
                "items":item,
                "transport_type":self.transport_type,
                "vehicle_number":self.vehicle_number,
                "driver_name":self.driver_whg
            })
            doc.save(ignore_permissions=True)
            frappe.msgprint("Purchase Invoice are Created Successfully")
        else:
            doc=frappe.new_doc("Purchase Invoice")
            item=[{
                "item_code":"Transport Item",
                "qty":1,
                "rate":self.transport_charges
                
            }]
            doc.update({
                "supplier":self.supplier,
                "items":item,
                "transport_type":self.transport_type,
                "vehicle":self.vehicle_number,
                "driver_name":self.driver_whg
            })
            doc.save(ignore_permissions=True)
            frappe.msgprint("Purchase Invoice are Created Successfully")

        

@frappe.whitelist()
def sales_loading(name, date, customer, coconant, trans_type, vehicle, vehicle2, driver):
    frappe.errprint("vgh")    
    doc=frappe.new_doc("Sales Loading")
    doc.update({
        "sales_invoice":name,
        "date":date,
        "customer":customer,
        "coconut_qty":coconant
    })
    doc.save(ignore_permissions=True)
    return sales_tranport(name, date, coconant, trans_type, vehicle, vehicle2, driver, customer)



def sales_tranport(name, date, coconant, trans_type, vehicle, vehicle2, driver, customer):
    frappe.errprint("hvghhhhhh")

    if(trans_type == "Own Vehicle"):
        frappe.errprint("fdvgdf")
        doc=frappe.new_doc("Sales Transport")
        doc.update({
            "sales_invoice":name,
            "transport_type":trans_type,
            "date":date,
            "coconut_qty":coconant,
            "vehicle":vehicle,
            "driver_whg":driver,
            "customer":customer
        })
        doc.save(ignore_permissions=True)
    else:
        doc=frappe.new_doc("Sales Transport")
        doc.update({
            "sales_invoice":name,
            "transport_type":trans_type,
            "date":date,
            "coconut_qty":coconant,
            "vehicle":vehicle2,
            "driver_whg":driver,
            "customer":customer
        })
        doc.save(ignore_permissions=True)