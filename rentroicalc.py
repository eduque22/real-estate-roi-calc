import time
class Roi():
    def __init__(self):
        self.home_value = 0
        self.monthly_rent_income = 0
        self.total_monthly_expenses = 0
        self.cash_flow = 0
        self.acf = 0
        self.total_investment = 0
        self.coc_roi = 0

    def price(self):
        print('\nWhat type of property are you looking to purchase?(Single-Family Home, Duplex, Triplex, etc.)')
        casita = input('Enter here: ')
        print(f'\nGreat, what is the current value of that {casita}?(Please enter digits only Ex. $40,000 = 40000)')
        home_value = int(input('Current Value: '))
        self.home_value = home_value
        print(f'Perfect, a {casita} valued at {home_value} will hopefully bring you some great returns, let\'s move on to the next step.')
        # hle_home['Home Value'] = home_value

    def monthly_rev(self):
        print('\nLet\'s take a look at monthly income. Please enter your expected income.(Please enter digits only)')
        monthly_rent_income = int(input('Expected Monthly Income: '))
        self.monthly_rent_income = monthly_rent_income
        print('Nice! Do you have any other incomes you would like to add, before moving on?(y/n)')
        extra = input('Extra Income: ')
        if extra.lower() == 'n':
            print(f'Okay then, let\'s continue with your total monthly income of ${monthly_rent_income}.')
            #hle_home['Monthly Rental Income'] = monthly_rent_income
        if extra.lower() == 'y':
            print('Okay, please add the extra income you would like us to account for.(Please enter digits only)')
            plus_monthly_rental = int(input('Added Monthly Income: $'))
            monthly_rent_income += plus_monthly_rental
            self.monthly_rent_income = monthly_rent_income
            #hle_home['Monthly Rental Income'] = monthly_rent_income
            print(f'Okay, your new total monthly income is ${monthly_rent_income}, let\'s continue.')

    def monthly_exp(self):
        print('\nNext, we\'ll go over some expenses.')
        print('What is the property tax you\'ll be paying for the home?(Provide property tax in %)')
        p_tax = float(input('Property Tax: '))
        prop_tax = (self.home_value * p_tax) / 360
        new_prop_tax = '%.2f' % prop_tax
        print(f'Estimated property tax: ${new_prop_tax}.')
        self.total_monthly_expenses += prop_tax
        print('How much do you expect to pay a month for property insurance? (Enter dollar amount)')
        prop_ins = int(input('Expected Property Insurance: $'))
        self.total_monthly_expenses += prop_ins
        print(f'Great, we\'ve added {prop_ins} to your total!')
        util = input('Will you be paying utilities?(y/n)')
        if util.lower() == 'n':
            print('Okay, let\'s continue.')
        if util.lower() == 'y':
            print('How much will you be paying for utilities a month?')
            monthly_util = int(input('Enter amount: $'))
            self.total_monthly_expenses += monthly_util
            print('Great, we got that added.')
        print('Will you be paying monthly HOA fees?(y/n)')
        hoa = input('HOA: ')
        if hoa.lower() == 'n':
            print('Great, let\'s keep going!')
        if hoa.lower() == 'y':
            print('How much will you be paying monthly?')
            hoa_fees = int(input('HOA Fees: $'))
            self.total_monthly_expenses += hoa_fees
            print('Perfect, now that we\'ve added that, let\'s continue.')
        print('Is there any amount you would like to set aside monthly for yard maintenance, housekeeping, etc.?(y/n)')
        service = input('Extra Services: ')
        if service.lower() == 'n':
            print('Okay, let\'s continue to our next question.')
        if service.lower() == 'y':
            print('How much will you be setting aside for extra services?(Please enter digits only)')
            serv_fees = int(input('Services Amount: $'))
            self.total_monthly_expenses += serv_fees
            print('That has been accounted for, let\'s move on to the next step.')
        print('What is your expected mortgage payment?')
        mortgage = int(input('Expected Mortg. Payment: $'))
        self.total_monthly_expenses += mortgage
        print('Now let us incorporate for the vacancy,')
        print('...')
        time.sleep(1)
        print('property management, ')
        print('...')
        time.sleep(1)
        print('and the $110 for minor monthly repairs.')
        print('...')
        time.sleep(2)
        vacancy = self.monthly_rent_income * .05
        self.total_monthly_expenses += vacancy
        prop_manage = self.monthly_rent_income * .10
        self.total_monthly_expenses += prop_manage
        capex_rep = 110
        self.total_monthly_expenses += capex_rep
        new_month_exp = '%.2f' % self.total_monthly_expenses
        #hle['Total Monthly Exp.'] = self.total_monthly_expenses
        print(f'We have calculated your total monthly expenses at: ${new_month_exp}')
        print('Next we\'ll go over cash flow!')

    def dinerito(self):
        self.cash_flow = self.monthly_rent_income - self.total_monthly_expenses
        new_cf = '%.2f' % self.cash_flow
        self.acf = self.cash_flow * 12
        new_acf = '%.2f' % self.acf
        #hle_home[‘Annual Cash Flow’] = acf
        print(f'\nYour monthly cash flow is estimated at: ${new_cf} bringing your annual cash flow to: ${new_acf}')
        print('Now let\'s take a look at what your cash on cash ROI will be!')

    def investment(self):
        print('\nWhat percentage will you pay for your down payment?(Enter 20% = .20)')
        down_pay = float(input('Down Payment: '))
        down_payment = self.home_value * down_pay
        self.total_investment += down_payment
        print(f'Your estimated down payment is: ${down_payment}')
        print('Now how much have you allotted for your rehab budget?')
        rehab_budget = int(input('Rehab Amount: '))
        self.total_investment += rehab_budget
        print('Lastly, if you have any other costs you\'ve come up with, please enter the total amount for them.')
        misc = int(input('Misc Amount: '))
        self.total_investment += misc
        print('Perfect, now let\'s calculate your total investment.')
        closing_cost = self.home_value * .04
        self.total_investment += closing_cost
        print(f'Your total investment comes up to {self.total_investment}.')
        coc_roi = (self.acf / self.total_investment) * 100
        coc_roif = "{:.2f}".format(coc_roi)
        print('Calculating your ROI')
        print('...')
        time.sleep(2)
        print('...')
        print(f'Your cash on cash ROI is: {coc_roif}%')
        #hle_home[‘Cash on Cash ROI’] = coc_roi
    

class Hidden:

    def show_desc():
        print('''
        Welcome to Hidden Leaf Estates and thank you for choosing our ROI calculator. Please note that our algorithm takes vacancy(monthly rent income * .05), property management(monthly rental income * .10) and small repairs($110) into account for monthly expenses and a conservative closing cost(home value * .04%) for your total investment. Information you should have on hand:
        1. Property Type
        2. Property Value
        3. Expected Monthly Rental Income/Additional Income
        4. Estimated Property Tax
        5. Estimated Property Insurance
        6. Monthly Utilities Amount(if you will be paying utilities)
        7. HOA Fees(if you will be paying those)
        8. Extra Monthly Services Amount
        9. Estimated Mortgage Payment
        10. Down Payment(%)
        11. Rehab Budget Amount
        12. Any Misc Amount
        ''')

    def get_rich():

        Hidden.show_desc()
        my_investment = Roi()

        while True:
            answer = input('Hidden Leaf Estates is ready to help, do you have all your information on hand?(y/n)\n Enter here: ').strip().lower()
            
            if answer == 'y':
                my_investment.price()
                my_investment.monthly_rev()
                my_investment.monthly_exp()
                my_investment.dinerito()
                my_investment.investment()
                print('\nThank you for choosing Hidden Leaf Estates, we wish you all the best on your real estate journey, happy investing!')
                break

            elif answer == 'n':
                print('No worries, we\'ll be here and ready to help when you have that on hand, we\'ll see you soon')
                break

            else:
                print('Invalid input, please enter from the following options.')

Hidden.get_rich()