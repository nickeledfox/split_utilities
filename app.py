from flask import Flask, render_template, request
from flask.views import MethodView

from form import BillForm
from split import params

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class FormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('form.html', form=bill_form)

class FormProcessing(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = billform.bill_total.data
        period = billform.date_posted.data

        bill = params.Bill(float(amount), period)
        payer1 = params.Roommate(billform.user_firstname.data,billform.user_last_name.data, days_in_place=float(billform.user_days_spent.data))
        payer2 = params.Roommate(billform.roommate_fn.data, billform.roommate_ln.data, days_in_place=float(billform.roommate_days_spent.data))

        return f'{payer1.first_name} pays {payer1.payment(bill, payer2)}'


@app.route('/', methods =["GET", "POST"])

def index():
    return render_template('index.html')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form',
                 view_func=FormPage.as_view('form'))
app.add_url_rule('/processed',
                 view_func=FormProcessing.as_view('processed'))

app.run(debug=True)