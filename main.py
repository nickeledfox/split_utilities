from fpdf import FPDF

class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:

    def __init__(self, first_name, last_name, days_in_place):
        self.first_name = first_name
        self.last_name = last_name
        self.days_in_place = days_in_place

    def payment(self, bill, roommate2):
        weight = self.days_in_place / (self.days_in_place + roommate2.days_in_place)
        pay = bill.amount * weight
        return pay

# creates pdf file that contains data such as names/each bill amount
class PDFReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        # payment amount
        payer1_bill = str(round(payer1.payment(bill, roommate2), 2))
        payer2_bill = str(round(payer2.payment(bill, roommate1), 2))

        pdf = FPDF('P', 'pt', 'A4')
        pdf.add_page()

        pdf = FPDF()
        pdf.add_page()

        # file params
        pdf.set_font('Times', 'B', 24)
        pdf.cell(60, 0, '')

        # image/logo
        pdf.image('house.png', x=95, y=5, w=15, h=15)

        # title
        pdf.cell(-60, 35, 'Split Utilities Bill', 'B')

        # bill date
        pdf.set_font('Times', 'B', 16,)
        pdf.cell(20, 65, 'Period:',)
        pdf.cell(-20, 65, bill.period,)

        pdf.set_font('Times', '', 16,)

        # payers info/ billing cycle amount
        pdf.cell(7, 85, payer1.first_name[0]+'.')
        pdf.cell(70, 85, payer1.last_name+' '+'payment due:')
        pdf.cell(-77, 85, payer1_bill)

        pdf.cell(7, 100, payer2.first_name[0] + '.', )
        pdf.cell(70, 100, payer2.last_name + ' '+'payment due:')
        pdf.cell(-1, 100, payer2_bill)

        pdf.output(self.filename)

pay_amount = Bill(amount=130, period='July 2021')
payer1 = Roommate(first_name='John', last_name='Smith', days_in_place=14)
payer2 = Roommate(first_name='Sam', last_name='Tarly', days_in_place=25)

print(payer1.first_name, payer1.last_name, payer1.payment(bill=pay_amount, roommate2=payer2))
print(payer2.first_name, payer2.last_name, payer2.payment(bill=pay_amount, roommate2=payer1))

pdf_report = PDFReport(filename='report.pdf')
pdf_report.generate(roommate1=payer1, roommate2=payer2, bill=pay_amount)
