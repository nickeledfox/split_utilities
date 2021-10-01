from wtforms import Form, StringField, SubmitField, FloatField, RadioField
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import DataRequired, Email


class BillForm(Form):
    user_firstname = StringField\
        ("First Name", validators=[DataRequired()],
         default="John")
    user_last_name = StringField\
        ("Last Name", validators=[DataRequired()],
         default="Doe")
    user_email = EmailField\
        ("Email Address", validators=[Email()],
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
        ("First Name", validators=[DataRequired()],
         default="James")
    roommate_ln = StringField\
        ("Last Name", validators=[DataRequired()],
         default="Smith")
    roommate_email = EmailField\
        ("Email Address", validators=[Email()],
         default="gmail@test.com")
    roommate_days_spent = FloatField\
        ("Days roommate spent at home",
         render_kw={"placeholder":
                        "(during the billing period)"},
         default="12")

    email_options = RadioField\
        ('Label',
         choices=[('don\'t-send', 'Don\'t send'),
                  ('to-roommate', 'To my roommate'),
                  ('to-both-us', 'To both us'),
                  ('send-to-me', 'Send to me')],
                  default="don't-send")


    submit_button = SubmitField("Calculate")