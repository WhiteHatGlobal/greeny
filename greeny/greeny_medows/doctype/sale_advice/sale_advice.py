# Copyright (c) 2022, White Hat Global and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SaleAdvice(Document):

	def before_submit(self):
		if (self.transport_type == "Own Vehicle"):
			if(self.qty!=self.total_loading_qty):
				frappe.throw("Total Quantity and Loading Quantity are mismatch")
	def on_submit(self):
		if (self.transport_type == "Own Vehicle"):
			
# Sales Loading Creation
			if(self.create_sales_loading == 1):
				doc=frappe.new_doc("Sales Loading")

				tab1=self.loading_details_table
				loading_emp=[]
				for i in range(0,len(tab1)):
					loading_emp.append({
						"date":tab1[i].get("date"),
						"employee":tab1[i].get("employee"),
						"qty":tab1[i].get("qty"),
						"rate":tab1[i].get("rate"),
						"amount":tab1[i].get("amount"),
					})

				tab2=self.others_loading
				loading_others=[]
				for i in range(0,len(tab2)):
					loading_others.append({
						"date":tab2[i].get("date"),
						"name1":tab2[i].get("name1"),
						"qty":tab2[i].get("qty"),
						"rate":tab2[i].get("rate"),
						"amount":tab2[i].get("amount"),
					})
					
				doc.update({
					    "date":self.date,
						"loading_details":loading_emp,
						"others_loading":loading_others,
					})
				doc.save(ignore_permissions=True)
				frappe.msgprint("Sales Loading are Created Successfully")


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
						"sale_advice":self.name,
						"approval_status":"Approved",
						"expenses":item,
						"payable_account":"Creditors - WHG"
					})
				doc.save(ignore_permissions=True)
				frappe.msgprint("Expense are Created Successfully")

# Additional Salary Creation

			if(self.loading_details_table):

					total_dict={}
					for row in self.loading_details_table:
						if row.get('employee') not in total_dict:
							total_dict[row.get('employee')]=[]
						total_dict[row.get('employee')].append({"date":row.date,"employee":row.employee,"qty":row.qty,"rate":row.rate,"amount":row.amount})
					frappe.errprint(list(total_dict.values()))
					for i in list(total_dict.values()):
						frappe.errprint(i[0].get("employee"))
						doc1=frappe.new_doc("Additional Salary")
						
						doc1.update({
							"employee":i[0].get("employee"),
							"loading_details":i,
							"salary_component":"Loading Salary",
							"payroll_date":self.date,
							"amount":0,
							
						})
						doc1.save(ignore_permissions=True)
						frappe.msgprint("Additional Salary are Created Successfully")

# Trasport Payment Creation
			
			if(self.others_loading):

				table2=self.others_loading
				doc2=frappe.new_doc("Trasport Payment")
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
						"sale_advice":self.name,
						"date":self.date,
						"customer":self.customer,
						"loading_payment_table":item2,
						"total_loading_qty":self.total_others,
						"total_loading_amount":self.others_loading_amount
					})
				doc2.save(ignore_permissions=True)
				frappe.msgprint("Transport Payment are Created Successfully")

# Sales Invoice Creation

			doc=frappe.new_doc("Sales Invoice")
			item=[{
                "item_code":self.item,
				"qty":self.net_weight,
				"qty2":self.qty
            }]
			doc.update({
                "customer":self.customer,
                "sale_advice":self.name,
				"number_of_coconant":self.qty,
				"bag_type":self.bag_type,
				"gross_weight_whg":self.weight,
				"no_of_bags":self.no_of_bags,
                "items":item,
                "transport_type_whg":self.transport_type,
                "vehicle_whg2":self.vehicle,
            })
			doc.save(ignore_permissions=True)
			frappe.msgprint("Sales Invoice are Created Successfully")

# Other Vehicle

		if (self.transport_type == "Other Vehicle"):
				doc1=frappe.new_doc("Sales Invoice")
				item=[{
					"item_code":"Transport Item",
					"qty":1,
					"rate":self.bill_amount
				}]
				doc1.update({
					"customer":self.customer,
     				"sale_advice":self.name,
					"number_of_coconant":self.qty,
					"bag_type":self.bag_type,
					"gross_weight_whg":self.weight,
					"no_of_bags":self.no_of_bags,
					"items":item,
					"transport_type_whg":self.transport_type,
					"vehicle_number_whg2":self.vehicle_no,
					# "driver_name":self.driver_nme
				})
				doc1.save(ignore_permissions=True)
				frappe.msgprint("Sales Invoice are Created Successfully")

@frappe.whitelist()
def account_head(expence_type):

	doc=frappe.get_doc('Expense Claim Type',expence_type)
	accounts_table=doc.accounts
	for i in range(0,len(accounts_table)):
		account=accounts_table[i].get("default_account")
	return account
		