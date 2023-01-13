# Copyright (c) 2022, White Hat Global and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PurchaseAdvice(Document):
	def before_submit(self):
		if (self.transport_type == "Own Vehicle"):
			if(self.qty!=self.total_loading_qty):
				frappe.throw("Total Quantity and Loading Quantity are mismatch")

	def on_submit(self):
		if (self.transport_type == "Own Vehicle"):
     
	 # Attendance Creation

			if(self.driver):
				doc=frappe.new_doc("Attendance")
				doc.update({
					"employee":self.driver,
					"attendance_date":self.date
				})
				doc.save(ignore_permissions=True)
				frappe.msgprint("Attendance Created For Driver")

	 # Expense Claim Creation

			if(self.expense_details):

				table=self.expense_details
				doc=frappe.new_doc("Expense Claim")
				item=[]
				for i in range(0,len(table)):
					
					date=table[i].get("date")
					type=table[i].get("expense_claim_type")
					amount=table[i].get("amount")
					remark=table[i].get("remarks")
					item.append({
						"expense_date":date,
						"expense_type":type,
						"amount":amount,
						"description":remark,
					})
				

				doc.update({
						"employee":self.driver,
						"purchase_advice":self.name,
						"approval_status":"Approved",
						"expenses":item,
						"payable_account":self.payable_account
					})
				doc.save(ignore_permissions=True)
				frappe.msgprint("Expense are Created Successfully")

	 # Additional Salary Creation

			if(self.loading_details_table):

					table1=self.loading_details_table
					for i in range(0,len(table1)):
						doc1=frappe.new_doc("Additional Salary")
            
						doc1.update({
							"employee":table1[i].get("employee"),
       						"purchase_advice":self.name,
							"salary_component":"Loading Salary",
							"payroll_date":table1[i].get("date"),
							"amount":table1[i].get("amount")
						})
						doc1.save(ignore_permissions=True)
					frappe.msgprint("Additional Salary Created Successfully")

 # Loading Payment Creation

			if(self.others_loading):

				table2=self.others_loading
				doc2=frappe.new_doc("Loading Payment")
				item2=[]
				for i in range(0,len(table2)):
					item2.append({
						"name1":table2[i].get("name1"),
						"qty":table2[i].get("qty"),
						"rate":table2[i].get("rate"),
						"amount":table2[i].get("amount"),
					})
				frappe.errprint(item2)
				

				doc2.update({
						"purchase_advice":self.name,
						"date":self.date,
						"supplier":self.supplier,
						"loading_payment_table":item2,
						"total_loading_qty":self.total_others,
						"total_loading_amount":self.others_loading_amount
					})
				doc2.save(ignore_permissions=True)
				frappe.msgprint("Loading Payment are Created Successfully")

# Purchase Invoice Creation

				if(self.expense_details):
					doc=frappe.new_doc("Purchase Invoice")
					tab=self.expense_details
					expence=[{
						"date":tab[i].get("date"),
						"expense_claim_type":tab[i].get("expense_claim_type"),
						"account_head":tab[i].get("account_head"),
						"amount":tab[i].get("amount"),
						"remarks":tab[i].get("remarks")
					}]
					frappe.errprint(expence)
					item=[{
						"item_code":self.item,
						"qty":self.net_weight,
						"qty2":self.qty
					}]
					doc.update({
						"supplier":self.supplier,
						"set_posting_time": "1",
						"posting_date":self.date,
						"number_of_coconant":self.qty,
						"bag_type":self.bag_type,
						"gross_weight_whg":self.weight,
						"no_of_bags":self.no_of_bags,
						"expence_detail_whg":self.expense_details,
						"items":item,
						"purchase_advice":self.name,
						"transport_type":self.transport_type,
						"vehicle":self.vehicle,
						"driver_name":self.driver_name,
						"expence_detail_whg":expence
					})
					doc.save(ignore_permissions=True)
					frappe.msgprint("Purchase Invoice are Created Successfully")
				else:
					doc=frappe.new_doc("Purchase Invoice")
					item=[{
						"item_code":self.item,
						"qty":self.net_weight,
						"qty2":self.qty
					}]
					doc.update({
						"supplier":self.supplier,
						"set_posting_time": "1",
						"posting_date":self.date,
						"number_of_coconant":self.qty,
						"bag_type":self.bag_type,
						"gross_weight_whg":self.weight,
						"no_of_bags":self.no_of_bags,
						"expence_detail_whg":self.expense_details,
						"items":item,
						"purchase_advice":self.name,
						"transport_type":self.transport_type,
						"vehicle":self.vehicle,
						"driver_name":self.driver_name
					})
					doc.save(ignore_permissions=True)
					frappe.msgprint("Purchase Invoice are Created Successfully")

# Purchase Invoice Creation for Other Vehicle (Item and Transport)

		if (self.transport_type == "Other Vehicle"):
				doc1=frappe.new_doc("Purchase Invoice")
				item1=[{
					"item_code":self.item,
					"qty":self.net_weight,
					"qty2":self.qty
				}]
				doc1.update({
					"supplier":self.supplier,
					"set_posting_time": "1",
					"posting_date":self.date,
     				"purchase_advice":self.name,
					"number_of_coconant":self.qty,
					"bag_type":self.bag_type,
					"gross_weight_whg":self.weight,
					"no_of_bags":self.no_of_bags,
					"items":item1,
					"transport_type":self.transport_type,
					"vehicle_number":self.vehicle_no,
					"driver_name":self.driver_nme
				})
				doc1.save(ignore_permissions=True)
				frappe.msgprint("Purchase Invoice are Created Successfully")

            # Purchase Invoice For Transport
				item2=[{
						"item_code":self.items,
						"qty":1,
						"rate":self.bill_amount
					}]

				doc1=frappe.new_doc("Purchase Invoice")
				doc1.update({
					"supplier":self.transport_supplier,
					"set_posting_time": "1",
					"posting_date":self.date,
     					"purchase_advice":self.name,
					"number_of_coconant":self.qty,
					"bag_type":self.bag_type,
					"gross_weight_whg":self.weight,
					"no_of_bags":self.no_of_bags,
					"items":item2,
					"transport_type":self.transport_type,
					"vehicle_number":self.vehicle_no,
					"driver_name":self.driver_nme
				})
				doc1.save(ignore_permissions=True)
				frappe.msgprint("Purchase Invoice are Created Against Transport")


@frappe.whitelist()
def account_head(expence_type):

	doc=frappe.get_doc('Expense Claim Type',expence_type)
	accounts_table=doc.accounts
	for i in range(0,len(accounts_table)):
		account=accounts_table[i].get("default_account")
	return account
		
