# Write your code here
import random


def isPresentName(f_name, name):
    f = open(f_name, 'r')
    for item in f:
        if name in item:
            f.close()
            return True
    f.close()
    return False


def getValue(f_name, name):
    f = open(f_name, 'r')
    for lines in f:
        if name in lines:
            return int(lines.split()[len(lines.split()) - 1])
    return -1


def Stronger(options, key):
    size = len(options) // 2
    i = 0
    res = []
    found = False
    while size:
        if options[i] == key:
            found = True
        if found:
            i += 1
            if i == len(options):
                i = 0
            res.append(options[i])
            size -= 1
        else:
            i += 1

    return res


name = input('Enter your name: ')
print('Hello,', name)

if isPresentName('rating.txt', name):
    score = getValue('rating.txt', name)
else:
    score = 0
args = input().split(',')
if args == ['']:
    args = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    inp = input()
    if inp == '!exit':
        print('Bye!')
        break
    elif inp == '!rating':
        print('Your rating:', score)
    elif inp in args:
        opt = args[random.randint(0, len(args)-1)]

        if opt == inp:
            print('There is a draw (' + opt + ')')
            score += 50
        else:
            strongers = Stronger(args,opt)
            if inp in strongers:
                print('Well done. The computer chose ' + opt + ' and failed')
                score += 100
            else:
                print('Sorry, but the computer chose ' + opt)
    else:
        print('Invalid input')
