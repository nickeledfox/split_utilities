from wtforms import Form, StringField, SubmitField, FloatField
from wtforms.fields.html5 import DateField


class BillForm(Form):

    user_firstname = StringField\
        ("First Name",
         default="John")
    user_last_name = StringField\
        ("Last Name",
         default="Doe")
    user_email = StringField\
        ("Email Address",
         default="email@test.com")


    date_posted = DateField\
        ("Billing date")


    user_days_spent = FloatField\
        ("Days spent at home",
         render_kw={"placeholder":
                        "(during the billing period)"},
         default="20")

    bill_total = FloatField\
        ("Total amount",
         render_kw={"placeholder":
                        "Bill total amount"},
         default="100")
         

    roommate_fn = StringField\
        ("First Name",
         default="James")
    roommate_ln = StringField\
        ("Last Name",
         default="Smith")
    roommate_email = StringField\
        ("Email Address",
         default="gmail@test.com")
    roommate_days_spent = FloatField\
        ("Days roommate spent at home",
         render_kw={"placeholder":
                        "(during the billing period)"},
         default="12")

    submit_button = SubmitField("Calculate")