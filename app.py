from flask import Flask, render_template, request
from flask.views import MethodView

from form_page import FormPage

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


@app.route('/', methods =["GET", "POST"])

def index():
    return render_template('index.html')


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form',
                 view_func=FormPage.as_view('form_page'))


app.run(debug=True)