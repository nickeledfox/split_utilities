from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')    


class BillFormPage(MethodView):

    def get(self):
        # bill_form = BillForm()
        return render_template('form.html')

class AmountPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        return amount
        

class BillForm(Form):
    pass

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       user_first_name = request.form.get("user_firstname")
       user_last_name = request.form.get("user_firstname")
       user_email = request.form.get("user_email")
       bill_total = request.form.get("bill_total")
       user_days_spent = request.form.get("user_days_spent")
       roommate_fn = request.form.get("roommate_fn")
       roommate_ln = request.form.get("roommate_ln")
       roommate_email = request.form.get("roommate_email")
       roommate_days_spent = request.form.get("roommate_days_spent")
       return render_template('calculated.html')
    return render_template("form.html")

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=BillFormPage.as_view('form'))

app.run(debug=True)