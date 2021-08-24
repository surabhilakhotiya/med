import frappe
import frappe.defaults
import frappe.permissions
from frappe.model.document import Document
from frappe import throw, msgprint
from frappe.utils import (cint, flt, has_gravatar, escape_html, format_datetime,
                          now_datetime, get_formatted_email, today)


@frappe.whitelist(allow_guest=True)
def owner_sign_up(email,full_name,mobile_no,gender,password,role_profile,mod_pro,bs_name,bs_addr,lat,long,b_info,bank,ac,branch,ifsc,mon,tue,wed,thu,fri,sat,sun,kwh,amount):
    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": escape_html(full_name),
        "mobile_no": mobile_no,
        "gender": gender,
        "new_password": password,
        "enabled": 1,
        "role_profile_name": role_profile,
        "module_profile": mod_pro,
        "owner_business_name":bs_name,
        "business_address":bs_addr,
        "lattitude":lat,
        "longitude":long,
        "business_information":b_info,
        "bank_name":bank,
        "account_number":ac,
        "branch":branch,
        "ifsc_code":ifsc,
        "monday":mon,
        "tuesday":tue,
        "wednesday":wed,
        "thursday":thu,
        "friday":fri,
        "saturday":sat,
        "sunday":sun,
        "kwh":kwh,
        "amount":amount
    })
    user.flags.ignore_permissions = True
    user.flags.ignore_password_policy = True
    user.insert()
    return "Sign-Up Successfully"

# API For This File
# http://0.0.0.0:8005/api/method/med.med.api.owner_signup.owner_sign_up
