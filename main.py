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

    def __init__(self, roommate):
        self.roommate = roommate

    def generate(self, roommate1, roommate2, bill):
        pass

bill = Bill(amount=130, period='August 2021')
payer1 = Roommate(first_name='John', last_name='Smith', days_in_place=14)
payer2 = Roommate(first_name='Sam', last_name='Tarly', days_in_place=25)

print(payer1.first_name, payer1.last_name, 'pays:', payer1.payment(bill=bill, roommate2=payer2))
print(payer2.first_name, payer2.last_name, 'pays:', payer2.payment(bill=bill, roommate2=payer1))
