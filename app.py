from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('form.html', form=bill_form)

class AmountPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        return amount
        

class BillForm(Form):
    user_firstname = StringField("First Name",)
    user_last_name = StringField("Last Name",)
    user_email = StringField("Email Address",)
    billing_period = StringField("Billing date",)
    user_days_spent = StringField\
        ("Days spent at home",
         render_kw={"placeholder":
                        "(during the billing period)"})

    bill_total = StringField\
        ("Total amount",
         render_kw={"placeholder":
                        "Bill total amount"})

    roommate_fn = StringField("First Name",)
    roommate_ln = StringField("Last Name",)
    roommate_email = StringField("Email Address")
    roommate_days_spent = StringField\
        ("Days roommate spent at home",
         render_kw={"placeholder":
                        "(during the billing period)"})
    

@app.route('/', methods =["GET", "POST"])
def index():
    return render_template('index.html')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=BillFormPage.as_view('form'))

app.run(debug=True)