from form import BillForm
from split import params

from flask import Flask, render_template, request
from flask.views import MethodView


class FormPage(MethodView):
    def get(self):
        bill_form = BillForm()

        return render_template('form.html', form=bill_form)


    def post(self):
        form_data = BillForm(request.form)

        bill = params.Bill\
            (form_data.bill_total.data,
             form_data.date_posted.data)
        payer1 = params.Roommate\
            (form_data.user_firstname.data,
             form_data.user_last_name.data,
             form_data.user_days_spent.data)
        payer2 = params.Roommate\
            (form_data.roommate_fn.data,
             form_data.roommate_ln.data,
             form_data.roommate_days_spent.data)


        if form_data.date_posted.data is None:
            date = f'No date provided'
        else:
            date = form_data.date_posted.data

        return render_template\
            ('form.html', form=form_data,
             calculated = True,

             payer1_firstname = payer1.first_name.capitalize(),
             payer1_lastname = payer1.last_name.capitalize(),
             payer1_total = round(payer1.payment(bill, payer2), 2),

             payer2_firstname = payer2.first_name.capitalize(),
             payer2_lastname = payer2.last_name.capitalize(),
             payer2_total = round(payer2.payment(bill, payer1), 2),

             total = form_data.bill_total.data,
             date = date,
             email_options = form_data.email_options.data)