from fpdf import FPDF

from input import *
from params import Bill, Roommate

# Create pdf file
class PDFReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        # Payment amount
        payer1_bill = str\
            (round(payer1.payment(bill, roommate2), 2))
        payer2_bill = str\
            (round(payer2.payment(bill, roommate1), 2))

        pdf = FPDF('P', 'pt', 'A4')
        pdf.add_page()

        pdf = FPDF()
        pdf.add_page()

        # File params
        pdf.set_font('Times', 'B', 24)
        pdf.cell(60, 0, '')

        # Image/logo
        pdf.image('img/house.png', x=95, y=5, w=15, h=15)

        # Title
        pdf.set_text_color(105, 105, 105)
        pdf.cell(-60, 35, 'Split Utilities Bill', 'C')

        # Bill date and total
        pdf.set_font('Times', 'B', 16)
        pdf.cell(1, 60, 'Period: '+bill.period.capitalize())

        pdf.set_font('Times', '', 16)
        pdf.cell(5, 75, 'Payers: '
                 +payer1.first_name.capitalize()+" "
                 +payer1.last_name.capitalize()+' and '
                 +payer2.first_name.capitalize()+" "
                 +payer2.last_name.capitalize())
        pdf.cell(1, 90, 'Total:'+" "+str(total_amount))

        # Payers info/ billing cycle amount
        pdf.cell(5, 115, payer1.first_name[0].capitalize() + '.'+' ')
        pdf.cell(60, 115, payer1.last_name.capitalize()+' '+'payment due is: ')
        pdf.cell(-65, 115, payer1_bill)

        pdf.cell(5, 130, payer2.first_name[0].capitalize() + '.'+' ')
        pdf.cell(60, 130, payer2.last_name.capitalize() + ' '+'payment due is: ')
        pdf.cell(-1, 130, payer2_bill)

        pdf.output(f'pdf/{self.filename}')


pay_amount = Bill(total_amount, billing_period)
payer1 = Roommate\
    (user_firstname,
     user_lastname,
     total_days_user)
payer2 = Roommate\
    (roommate_firstname,
     roommate_lastname,
     total_days_roommate)

print(payer1.first_name,
      payer1.last_name,
      payer1.payment(pay_amount, payer2))
print(payer2.first_name,
      payer2.last_name,
      payer2.payment(pay_amount, payer1))

pdf_report = PDFReport(filename='report.pdf')
pdf_report.generate(roommate1=payer1, roommate2=payer2, bill=pay_amount)

