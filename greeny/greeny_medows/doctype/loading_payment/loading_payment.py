# Copyright (c) 2022, White Hat Global and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate, today
from frappe.model.document import Document

class LoadingPayment(Document):
	# pass
	def on_submit(self):
		if (self.status == "Paid"):
		
			doc=frappe.new_doc("Journal Entry")
			items=[{'account': 'Cash - WHG', 'debit_in_account_currency': self.paid, 'credit_in_account_currency': 0}, {'account': 'Others Expenses - WHG', 'debit_in_account_currency': 0, 'credit_in_account_currency': self.paid}]
				
			frappe.errprint(frappe.utils.nowdate())
			doc.update({
				"posting_date":frappe.utils.nowdate(),
				"accounts":items,
				
			})
			doc.save(ignore_permissions=True)
			frappe.msgprint("Journal Entry are Created Successfully")