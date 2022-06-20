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
        ]
                }
    create_custom_fields(custom_fields)
