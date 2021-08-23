import frappe
import frappe.defaults
import frappe.permissions
from frappe.model.document import Document
from frappe import throw, msgprint
from frappe.utils import (cint, flt, has_gravatar, escape_html, format_datetime,
                          now_datetime, get_formatted_email, today)


@frappe.whitelist(allow_guest=True)
def owner_sign_up(email, full_name, mobile_no, gender, password):
    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": escape_html(full_name),
        "mobile_no": mobile_no,
        "gender": gender,
        "new_password": password,
        "enabled": 1,
        "user_type": "System User"
    })
    user.flags.ignore_permissions = True
    user.flags.ignore_password_policy = True
    user.insert()
    return "User Registered Successfully..!!"

    # # set default signup role as per Portal Settings
    # default_role = frappe.db.get_value("Portal Settings", None, "default_role")
    # if default_role:
    # 	user.add_roles(default_role)

    # if redirect_to:
    # 	frappe.cache().hset('redirect_after_login', user.name, redirect_to)

    # if user.flags.email_sent:
    # 	return 1, _("Please check your email for verification")
    # else:
    # 	return 2, _("Please ask your administrator to verify your sign-up")

# API For This File
# http://0.0.0.0:8005/api/method/med.med.api.owner_signup.owner_sign_up
