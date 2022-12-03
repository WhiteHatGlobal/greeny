from . import __version__ as app_version

app_name = "greeny"
app_title = "Greeny Medows"
app_publisher = "White Hat Global"
app_description = "Greeny Medows Custom app"
app_email = "rk@whitehatglobal.org"
app_license = "MIT"

# Includes in <head>
# ------------------
# import Stock function & custom function for customisation
override_doctype_class = {
    "Stock Ledger Entry": "greeny.overrides.stock_ledger_entry.CustomStockLedgerEntry"
}
# include js, css files in header of desk.html
# app_include_css = "/assets/greeny/css/greeny.css"
# app_include_js = "/assets/greeny/js/greeny.js"

# include js, css files in header of web template
# web_include_css = "/assets/greeny/css/greeny.css"
# web_include_js = "/assets/greeny/js/greeny.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "greeny/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
# include js in doctype views

doctype_js = {"Purchase Receipt" : "/greeny_medows/dev_custom/purchase_receipt.js",
              "Purchase Invoice" : "/greeny_medows/dev_custom/purchase_invoice.js",
			  "Sales Invoice" : "/greeny_medows/dev_custom/sales_invoice.js",
			  "Stock Entry" : "/greeny_medows/dev_custom/stock_entry.js",
			  "Purchase Loading":"/greeny_medows/dev_custom/purchase_loading.js",
			  "Sales Loading":"/greeny_medows/dev_custom/sales_loading.js",
			  "Purchase Transport":"/greeny_medows/dev_custom/purchase_transport.js",
			  }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "greeny.utils.jinja_methods",
#	"filters": "greeny.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "greeny.install.before_install"
# after_install = "greeny.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "greeny.uninstall.before_uninstall"
# after_uninstall = "greeny.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "greeny.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
	"Purchase Transport": {
		"on_submit": "greeny.greeny_medows.dev_custom.purchase_sales.purchase_transport",
		
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"greeny.tasks.all"
#	],
#	"daily": [
#		"greeny.tasks.daily"
#	],
#	"hourly": [
#		"greeny.tasks.hourly"
#	],
#	"weekly": [
#		"greeny.tasks.weekly"
#	],
#	"monthly": [
#		"greeny.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "greeny.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "greeny.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "greeny.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"greeny.auth.validate"
# ]
fixtures = [
	 "Custom Field",
	 "Client Script",
	 "Property Setter"
]