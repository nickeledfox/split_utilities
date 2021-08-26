from flask import Flask
from flask.views import MethodView
from wtforms import Form

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return 'Hi home page!'    


class BillFormPage(MethodView):

    def get(self):
        return 'Some String'

class AmountPage(MethodView):
    pass

class BillForm(Form):
    pass

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run()