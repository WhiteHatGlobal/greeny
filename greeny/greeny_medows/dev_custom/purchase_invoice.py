import frappe

def landes_cost_voucher(self, event):
        frappe.errprint("aaaagggg")
        if (self.transport_type == "Own Vehicle"):
            doc=frappe.new_doc("Landed Cost Voucher")
            purchase_receipts=[{
                "receipt_document_type":"Purchase Invoice",
                "receipt_document":self.name,
                "supplier":self.supplier,
                "grand_total":self.grand_total
                
            }]
            
            table=self.items
            items=[]
            for i in range(0,len(table)):
                items.append({
                    "item_code":table[i].get("item_code"),
                    "description":table[i].get("qty"),
                    "qty":table[i].get("qty"),
                    "rate":table[i].get("rate"),
                    "amount":table[i].get("amount"),

                })


            table1=self.expence_detail_whg
            taxes=[]
            for i in range(0,len(table1)):
                taxes.append({
                    "expense_account":table1[i].get("account_head"),
                    "description":table1[i].get("remarks"),
                    "amount":table1[i].get("amount"),
                })
            


            doc.update({
                "purchase_receipts":purchase_receipts,
                "items":items,
                "taxes":taxes,
            })
            doc.save(ignore_permissions=True)
            frappe.msgprint("Purchase Invoice Against Landed Cost Voucher  Created Successfully")
