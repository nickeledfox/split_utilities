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
        pdf.set_font('Times', 'B', 16)
        pdf.cell(20, 65, 'Period:',)
        pdf.cell(-20, 65, bill.period.capitalize())
        pdf.set_font('Times', '', 16)

        # payers info/ billing cycle amount
        pdf.cell(7, 85, payer1.first_name[0].capitalize() + '.', )
        pdf.cell(70, 85, payer1.last_name.capitalize()+' '+'payment due is:')
        pdf.cell(-77, 85, payer1_bill)

        pdf.cell(7, 100, payer2.first_name[0].capitalize() + '.', )
        pdf.cell(70, 100, payer2.last_name.capitalize() + ' '+'payment due is:')
        pdf.cell(-1, 100, payer2_bill)

        pdf.output(self.filename)


# hello = input('Hello! I\'ll walk you through the bill splitting process.\nPress "Enter" to move forward ')
user_firstname = input('Enter your first name, please ')
user_lastname = input('Enter your lastname, please ')
billing_period = input('What is the billing date? ')
total_amount = float(input('Enter the total amount of the bill: '))
total_days_user = int(input('How many days have you spent at home during the billing period:\n'+billing_period+'?'))

roommate_firstname = input('Enter your roommate first name, please ')
roommate_lastname = input('Enter your roommate lastname, please ')
total_days_roommate = int(input(f'How many days {roommate_firstname+""+roommate_lastname} spent at home during the billing period:\n'+billing_period+'?'))

print('The total for', billing_period, 'is:', total_amount)


pay_amount = Bill(total_amount, billing_period)
payer1 = Roommate(user_firstname, user_lastname, total_days_user)
payer2 = Roommate(roommate_firstname, roommate_lastname, total_days_roommate)

print(payer1.first_name, payer1.last_name, payer1.payment(pay_amount, payer2))
print(payer2.first_name, payer2.last_name, payer2.payment(pay_amount, payer1))

pdf_report = PDFReport(filename='report.pdf')
pdf_report.generate(roommate1=payer1, roommate2=payer2, bill=pay_amount)
