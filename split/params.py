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