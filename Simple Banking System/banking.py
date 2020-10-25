import sqlite3
import random

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
    conn.commit()
except sqlite3.OperationalError:
    pass

card_pin_list = []
balance = 0


def generateCard():
    s = 0
    card_n = '400000'
    for i in range(9):
        card_n += str(random.randint(0, 9))
    card_no = card_n
    card_n = list(card_n)

    for i in range(15):
        if i % 2 == 0:
            tmp = card_n[:i]
            tmp.append(str(int(card_n[i]) * 2))
            card_n = tmp + card_n[i + 1:]
            if int(card_n[i]) > 9:
                card_n = card_n[:i] + list(str(int(card_n[i]) - 9)) + card_n[i + 1:]
        s += int(card_n[i])
    checksum = -1
    for j in range(10):
        if (s + j) % 10 == 0:
            checksum = j
            break
    return card_no + str(checksum)


def PassesLuns(card_num):
    card_n = list(card_num)
    s = 0
    for i in range(15):
        if i % 2 == 0:
            tmp = card_n[:i]
            tmp.append(str(int(card_n[i]) * 2))
            card_n = tmp + card_n[i + 1:]
            if int(card_n[i]) > 9:
                card_n = card_n[:i] + list(str(int(card_n[i]) - 9)) + card_n[i + 1:]
        s += int(card_n[i])
    checksum = card_num[15]
    if (int(checksum) + s) % 10 == 0:
        return True
    return False


def generatePin():
    pin = ''
    for i in range(4):
        pin += str(random.randint(0, 9))
    return pin


def CreateAnAccount():
    card_no = generateCard()
    pin_no = generatePin()
    card_pin_list.append((card_no, pin_no))
    print('Your card has been created')
    print('Your card number:')
    print(card_no)
    print('Your card PIN:')
    print(pin_no)
    cur.execute('INSERT INTO card (id,number,pin) VALUES ({},"{}","{}")'.format(
        len(cur.execute('SELECT * FROM card').fetchall()), card_no, pin_no))
    conn.commit()


def VerifiedCardDetails(card_no, pin_no='-1'):
    cur.execute('SELECT * FROM card')
    lot = cur.fetchall()
    for i in range(len(lot)):
        if (lot[i][1] == card_no and pin_no == '-1') or (lot[i][1] == card_no and lot[i][2] == pin_no):
            return i
    return -1


def CheckBalance(key):
    print('Balance:', cur.execute('SELECT * FROM card WHERE id={}'.format(key)).fetchall()[0][3])


def getBalance(key):
    return cur.execute('SELECT * FROM card WHERE id={}'.format(key)).fetchall()[0][3]


def UpdateMoney(key, by):
    cur.execute('UPDATE card SET balance={} WHERE id = {}'.format(getBalance(key) + by, key))
    conn.commit()


def AddIncome(key, val):
    UpdateMoney(key, val)


def DoTransfer(key, frm, to):
    verCard = VerifiedCardDetails(to)
    if frm == to:
        print("You can't transfer money to the same account!")
    elif not PassesLuns(to):
        print('Probably you made a mistake in the card number. Please try again!')
    elif verCard == -1:
        print('Such a card does not exist.')
    else:
        print('Enter how much money you want to transfer:')
        money = int(input())
        if money > getBalance(key):
            print('Not enough money!')
        else:
            UpdateMoney(key, -money)
            UpdateMoney(verCard, money)
            print('Success!')


def CloseAccount(key):
    cur.execute('DELETE FROM card WHERE id={}'.format(key))
    conn.commit()


def login(key, card_num):
    while True:
        print()
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        choice = int(input())
        print()
        if choice == 0:
            print('Bye!')
            exit()
        elif choice == 1:
            CheckBalance(key)
        elif choice == 2:
            print('Enter income:')
            val = int(input())
            AddIncome(key, val)
            print('Income was added!')
        elif choice == 3:
            print('Transfer')
            print('Enter card number:')
            to = input()
            DoTransfer(key, card_num, to)
        elif choice == 4:
            CloseAccount(key)
            print('The account has been closed!')
            return
        elif choice == 5:
            print('You have successfully logged out!')
            return


while True:
    print()
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    ch = int(input())
    print()
    if ch == 1:
        CreateAnAccount()
    elif ch == 2:
        print('Enter your card number:')
        card = input()
        print('Enter your PIN:')
        p = input()
        print()
        keyVal = VerifiedCardDetails(card, p)
        if keyVal != -1:
            print('You have successfully logged in!')
            login(keyVal, card)
        else:
            print('Wrong card number or PIN!')
    elif ch == 0:
        print('Bye!')
        exit()
