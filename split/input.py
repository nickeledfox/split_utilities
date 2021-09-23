user_firstname = input\
    ('Enter your first name, please ')
user_lastname = input\
    ('Enter your lastname, please ')
billing_period = input\
    ('What is the billing date? ')
total_amount = float\
    (input('Enter the total amount of the bill: '))
total_days_user = int(
    input
    ('How many days have you spent at home during the billing period:'
     '\n'+billing_period+'?'))

roommate_firstname = input\
    ('Enter your roommate first name, please ')
roommate_lastname = input\
    ('Enter your roommate lastname, please ')
total_days_roommate = int(
    input(f'How many days '
          f'{roommate_firstname+" "+roommate_lastname}'
          f' spent at home during the billing period:'
          f'\n'+billing_period+'?'))