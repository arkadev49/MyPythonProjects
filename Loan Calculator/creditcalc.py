import argparse
import sys
import math

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', help='Type of Payment')
parser.add_argument('-a', '--payment', help='Monthly Payment Amount', type=float)
parser.add_argument('-p', '--principal', help='Principal Amount', type=float)
parser.add_argument('-n', '--periods', help='Number of months needed to repay the loan', type=int)
parser.add_argument('-i', '--interest', help='Interest without percent sign', type=float)
args = parser.parse_args()


def isCorrect():
    if args.type is None:
        return False
    elif len(sys.argv) - 1 < 4:
        return False
    elif args.type != 'annuity' and args.type != 'diff':
        return False
    elif args.type == 'diff' and args.payment is not None:
        return False
    elif args.interest is None:
        return False
    elif args.payment or args.principal or args.interest:
        if args.payment:
            if args.payment < 0:
                return False
        if args.principal:
            if args.principal < 0:
                return False
        if args.interest:
            if args.interest < 0:
                return False
        if args.periods:
            if args.periods < 0:
                return False
    return True


def annuity_monthly_payment_amount(principal, periods, loan_interest):
    i = loan_interest / 1200
    monthly_payment = int(math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))))
    print('Your annuity payment = ' + str(monthly_payment) + '!')
    overpay = int(monthly_payment * periods - principal)
    print('Overpayment = ' + str(overpay))


def loan_principal(annuity_payment, periods, loan_interest):
    i = loan_interest / 1200
    p = int(math.floor(annuity_payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))))
    print('Your loan principal = ' + str(p) + '!')
    overpay = int(annuity_payment * periods - p)
    print('Overpayment = ' + str(overpay))


def number_of_monthly_payments(loan_principal_amt, monthly_payment, loan_interest):
    i = loan_interest / 1200
    n = int(math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal_amt), 1 + i)))
    if n <= 12:
        print('It will take ' + str(n) + ' months to repay this loan!')
    else:
        if n % 12 == 0:
            if n // 12 == 1:
                print('It will take ' + str(n // 12) + ' year to repay this loan!')
            else:
                print('It will take ' + str(n // 12) + ' years to repay this loan!')
        else:
            print('It will take ' + str(n // 12) + ' years and ' + str(n % 12) + ' months to repay this loan!')
    overpay = int(monthly_payment * n - loan_principal_amt)
    print('Overpayment = ' + str(overpay))


def differentiate_payment(interest, principal, periods):
    s = 0
    i = interest / 1200
    for m in range(1, periods + 1):
        d = math.ceil((principal / periods) + i * (principal - ((principal * (m - 1)) / periods)))
        s += d
        print('Month ' + str(m) + ': payment is ' + str(d))
    print()
    print('Overpayment = ' + str(int(s - args.principal)))


if not isCorrect():
    print('Incorrect parameters')
else:
    if args.type == 'diff':
        differentiate_payment(args.interest, args.principal, args.periods)
    elif args.type == 'annuity':
        if args.payment is None:
            annuity_monthly_payment_amount(args.principal, args.periods, args.interest)
        if args.principal is None:
            loan_principal(args.payment, args.periods, args.interest)
        if args.periods is None:
            number_of_monthly_payments(args.principal, args.payment, args.interest)

#######################################################################################################################

"""loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(loan_principal+'\n'+first_month+'\n'+second_month+'\n'+third_month+'\n'+final_output)"""

#######################################################################################################################

"""import math


def calculateMonth():
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    res = math.ceil(loan_principal / monthly_payment)
    print()
    if res == 1:
        print('It will take 1 month to repay the loan')
    else:
        print('It will take ' + str(res) + ' months to repay the loan')


def calculatePayment():
    print("Enter the number of months:")
    months = int(input())
    print()
    payment = math.ceil(loan_principal / months)
    if loan_principal % months != 0:
        last_payment = loan_principal - (months - 1) * payment
    else:
        last_payment = 0
    if last_payment == 0:
        print("Your monthly payment =", payment)
    else:
        print('Your monthly payment = ' + str(payment) + ' and the last payment = ' + str(last_payment) + '.')


print("Enter the loan principal:")
loan_principal = int(input())
print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payments:')
choice = input()
if choice == 'm':
    calculateMonth()
elif choice == 'p':
    calculatePayment()"""

#######################################################################################################################

'''import math


def number_of_monthly_payments():
    print("Enter the loan principal:")
    loan_principal_amt = float(input())
    print('Enter the monthly payment:')
    monthly_payment = float(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    n = int(math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal_amt), 1 + i)))
    if n <= 12:
        print('It will take ' + str(n) + ' months to repay this loan!')
    else:
        if n % 12 == 0:
            if n // 12 == 1:
                print('It will take ' + str(n // 12) + ' year to repay this loan!')
            else:
                print('It will take ' + str(n // 12) + ' years to repay this loan!')
        else:
            print('It will take ' + str(n // 12) + ' years and ' + str(n % 12) + ' months to repay this loan!')


def annuity_monthly_payment_amount():
    print("Enter the loan principal:")
    principal = float(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    monthly_payment = int(math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))))
    print('Your monthly payment = ' + str(monthly_payment) + '!')


def loan_principal():
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    p = int(round(annuity_payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))))
    print('Your loan principal = ' + str(p) + '!')


print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
choice = input()
if choice == 'n':
    number_of_monthly_payments()
elif choice == 'a':
    annuity_monthly_payment_amount()
elif choice == 'p':
    loan_principal()'''


#######################################################################################################################

"""import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e","--echo", help='Displays the string')
parser.add_argument("-r","--root", help="displays square root of the number", type=float)
parser.add_argument("-c","--caller", help='Checks whether the caller is called or not', action='store_true')
args = parser.parse_args()
if args.caller:
    print('Caller is called')
else:
    print('Caller was not called')
if args.echo:
    print(args.echo)
if args.root:
    print(args.root ** 0.5)
print("Thank You for Using This Service.")"""
