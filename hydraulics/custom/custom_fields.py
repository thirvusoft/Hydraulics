from optparse import Option
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def customize():
    custom_fields = {
        "Sales Order": [
            dict(fieldname='abbr', label='Abbr',
                fieldtype='Data', insert_after='column_break1', read_only=0),
            dict(fieldname='additional_notes', label='Additional Notes',
                fieldtype='Section Break', insert_after='items', read_only=0),
            dict(fieldname='add_notes', label='Additional Notes',
                fieldtype='Small Text', insert_after='items', read_only=0),
        ],
        "Sales Invoice":[
            dict(fieldname='vehicle', label='Vehicle',
                fieldtype='Data', insert_after='customer', read_only=0),
            dict(fieldname='section_break_228', fieldtype='Section Break',insert_after='vehicle_no'),
            dict(fieldname='additional_notes', label='Additional Notes',
                fieldtype='Section Break', insert_after='section_break_228', read_only=0,collapsible=1),
            dict(fieldname='add_notes', label='Additional Notes',
                fieldtype='Small Text', insert_after='additional_notes', read_only=0),
            dict(fieldname='column_break_invoice', label='',
                fieldtype='Column Break', insert_after='add_notes', read_only=0),
            dict(fieldname='delivery_date', label='Delivery Date',
                fieldtype='Date', insert_after='column_break_invoice', read_only=0),
            dict(fieldname='distance_km', label='Distance(in km)',
                fieldtype='Float', insert_after='delivery_date', read_only=0),
            dict(fieldname='dname', label='Driver',
                fieldtype='Data', insert_after='distance_km', read_only=0),               
            dict(fieldname='drivername', label='Driver Name',
                fieldtype='Data', insert_after='dname', read_only=0),
            dict(fieldname='section_break_229', fieldtype='Section Break',insert_after='redeem_loyalty_points'),
            dict(fieldname='delivery', label='Delivery',
                fieldtype='Section Break', insert_after='section_break_229', read_only=0,collapsible=1),
            dict(fieldname='deliverymode', label='Delivery Mode',
                fieldtype='Select', insert_after='delivery',options='\n Delivery Pickup \n Courier Bus  \n  Delivery',read_only=0),
            dict(fieldname='contact_person_for_delivery', label='Contact Person For Delivery',
                fieldtype='Data', insert_after='deliverymode', read_only=0),
        ]

    }
    create_custom_fields(custom_fields)
