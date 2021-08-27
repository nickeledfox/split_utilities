from flask import Flask, render_template
from flask.views import MethodView
from wtforms import Form

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')    


class BillFormPage(MethodView):

    def get(self):
        return render_template('form.html')

class AmountPage(MethodView):
    pass

class BillForm(Form):
    pass

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form', view_func=BillFormPage.as_view('form'))

app.run(debug=True)