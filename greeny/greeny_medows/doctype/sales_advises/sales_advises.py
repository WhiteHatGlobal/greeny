# Copyright (c) 2022, White Hat Global and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PurchaseAdvice(Document):
	pass
	# def on_submit(self):
	# 	if (self.transport_type == "Own Vehicle"):
	# 		if(self.expense_details):

	# 			table=self.expense_details
	# 			doc=frappe.new_doc("Expense Claim")
	# 			item=[]
	# 			for i in range(0,len(table)):
					
	# 				date=table[i].get("date")
	# 				type=table[i].get("expense_claim_type")
	# 				amount=table[i].get("amount")
	# 				remark=table[i].get("remarks")
	# 				item.append({
	# 					"expense_date":date,
	# 					"expense_type":type,
	# 					"amount":amount,
	# 					"description":remark,
	# 				})
				

	# 			doc.update({
	# 					"employee":self.driver,
	# 					"expense_approver":'rk@whg.org',
	# 					"approval_status":"Approved",
	# 					"expenses":item,
	# 					"payable_account":"Creditors - WHG"
	# 				})
	# 			doc.save(ignore_permissions=True)
	# 			frappe.msgprint("Expense are Created Successfully")


	# 		if(self.loading_details_table):

	# 				table1=self.loading_details_table
	# 				for i in range(0,len(table1)):
	# 					doc1=frappe.new_doc("Additional Salary")
            
	# 					doc1.update({
	# 						"employee":table1[i].get("employee"),
	# 						"salary_component":"Loading Salary",
	# 						"payroll_date":table1[i].get("date"),
	# 						"amount":table1[i].get("amount")
	# 					})
	# 					doc1.save(ignore_permissions=True)
	# 				frappe.msgprint("Additional Salaryare Created Successfully")

			
			# if(self.others_loading):

			# 	table2=self.others_loading
			# 	frappe.errprint("taaaa")
			# 	doc2=frappe.new_doc("Loading Payment")
			# 	item2=[]
			# 	for i in range(0,len(table2)):
			# 		item2.append({
			# 			"name1":table2[i].get("name1"),
			# 			"qty":table2[i].get("qty"),
			# 			"rate":table2[i].get("rate"),
			# 			"amount":table2[i].get("amount"),
			# 		})
				

			# 	doc2.update({
			# 			"purchase_advice_whg":self.name,
			# 			"date":self.date,
			# 			"supplier":self.supplier,
			# 			"loading_payment_table":item2,
			# 			"total_loading_qty":self.total_others,
			# 			"total_loading_amount":self.others_loading_amount
			# 		})
			# 	doc2.save(ignore_permissions=True)
			# 	frappe.msgprint("Loading Payment are Created Successfully")


			# doc=frappe.new_doc("Purchase Invoice")
			# item=[{
            #     "item_code":"Coconut",
			# 	"qty":self.qty
            # }]
			# doc.update({
            #     "supplier":self.supplier,
			# 	"number_of_coconant":self.qty,
			# 	"bag_type":self.bag_type,
			# 	"gross_weight_whg":self.weight,
			# 	"no_of_bags":self.no_of_bags,
            #     "items":item,
            #     "transport_type":self.transport_type,
            #     "vehicle":self.vehicle,
            #     "driver_name":self.driver_name
            # })
			# doc.save(ignore_permissions=True)
			# frappe.msgprint("Purchase Invoice are Created Successfully")

		# if (self.transport_type == "Other Vehicle"):
		# 		doc1=frappe.new_doc("Purchase Invoice")
		# 		item=[{
		# 			"item_code":"Coconut",
		# 			"qty":self.qty
		# 		}]
		# 		doc1.update({
		# 			"supplier":self.supplier,
		# 			"number_of_coconant":self.qty,
		# 			"bag_type":self.bag_type,
		# 			"gross_weight_whg":self.weight,
		# 			"no_of_bags":self.no_of_bags,
		# 			"items":item,
		# 			"transport_type":self.transport_type,
		# 			"vehicle_number":self.vehicle_no,
		# 			"driver_name":self.driver_nme
		# 		})
		# 		doc1.save(ignore_permissions=True)
		# 		frappe.msgprint("Purchase Invoice are Created Successfully")