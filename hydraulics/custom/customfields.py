
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def creation():
    custom_fields = {
        "Customer": [
           	
           
            dict(fieldname='contact_name', label='Contact Name',
                fieldtype='Data', insert_after='company_name', read_only=0),
            dict(fieldname='contact_name', label='Contact Name',
                fieldtype='Data', insert_after='company_name', read_only=0),
          
        ],
     
    }
    create_custom_fields(custom_fields)
    print('finished')

   