class CoffeeMachine:

    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups

    def State(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print('$' + str(self.money), 'of money')

    def isResourceAvailable(self, water, milk, coffee):
        if water > self.water:
            print('Sorry, not enough water!')
            return False
        if milk > self.milk:
            print('Sorry, not enough milk!')
            return False
        if coffee > self.coffee:
            print('Sorry, not enough coffee beans!')
            return False
        if self.cups == 0:
            print('Sorry, not enough cups!')
            return False
        return True

    def Update(self, water, milk, coffee, money, cups=-1):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
        self.money += money

    def Buy(self, water, milk, coffee, money):
        if self.isResourceAvailable(water, milk, coffee):
            print('I have enough resources, making you a coffee!')
            self.Update(-water, -milk, -coffee, money)

    def Fill(self, water, milk, coffee, cups):
        self.Update(water, milk, coffee, 0, cups)

    def Take(self):
        t = self.money
        self.money -= self.money
        return t


machine = CoffeeMachine(550, 400, 540, 120, 9)

while True:
    print('Write action (buy, fill, take):')
    choice = input()
    print()
    if choice == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        ch = input()
        if ch == 'back':
            print()
            continue
        if ch == '1':
            machine.Buy(250, 0, 16, 4)
        elif ch == '2':
            machine.Buy(350, 75, 20, 7)
        elif ch == '3':
            machine.Buy(200, 100, 12, 6)
    elif choice == 'fill':
        print('Write how many ml of water do you want to add:')
        w = int(input())
        print('Write how many ml of milk do you want to add:')
        m = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        cof = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        cup = int(input())
        machine.Fill(w, m, cof, cup)
    elif choice == 'take':
        print('I gave you', '$' + str(machine.Take()))
    elif choice == 'remaining':
        machine.State()
    elif choice == 'exit':
        break
    print()

# money = 550
# water = 400
# milk = 540
# coffee = 120
# cups = 9
#
#
# def State():
#     print('The coffee machine has:')
#     print(water, 'of water')
#     print(milk, 'of milk')
#     print(coffee, 'of coffee beans')
#     print(cups, 'of disposable cups')
#     if money == 0:
#         print(money, 'of money')
#     else:
#         print('$' + str(money), 'of money')
#
#
# while True:
#     print('Write action (buy, fill, take):')
#     choice = input()
#     print()
#     if choice == 'buy':
#         print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
#         ch = input()
#         if ch == '1':
#             if water >= 250 and coffee >= 16:
#                 print('I have enough resources, making you a coffee!')
#                 water -= 250
#                 coffee -= 16
#                 money += 4
#                 cups -= 1
#             else:
#                 if water < 250:
#                     print('Sorry, not enough water!')
#                 else:
#                     print('Sorry, not enough coffee beans!')
#         elif ch == '2':
#             if water >= 350 and milk >= 75 and coffee >= 20:
#                 print('I have enough resources, making you a coffee!')
#                 water -= 350
#                 milk -= 75
#                 coffee -= 20
#                 money += 7
#                 cups -= 1
#             else:
#                 if water < 350:
#                     print('Sorry, not enough water!')
#                 elif milk < 75:
#                     print('Sorry, not enough milk!')
#                 else:
#                     print('Sorry, not enough coffee beans!')
#         elif ch == '3':
#             if water >= 200 and milk >= 100 and coffee >= 12:
#                 print('I have enough resources, making you a coffee!')
#                 water -= 200
#                 milk -= 100
#                 coffee -= 12
#                 money += 6
#                 cups -= 1
#             else:
#                 if water < 200:
#                     print('Sorry, not enough water!')
#                 elif milk < 100:
#                     print('Sorry, not enough milk!')
#                 else:
#                     print('Sorry, not enough coffee beans!')
#         elif ch == 'back':
#             print()
#             continue
#     elif choice == 'fill':
#         print('Write how many ml of water do you want to add:')
#         water += int(input())
#         print('Write how many ml of milk do you want to add:')
#         milk += int(input())
#         print('Write how many grams of coffee beans do you want to add:')
#         coffee += int(input())
#         print('Write how many disposable cups of coffee do you want to add:')
#         cups += int(input())
#     elif choice == 'take':
#         print('I gave you', '$' + str(money))
#         money -= money
#     elif choice == 'remaining':
#         State()
#     elif choice == 'exit':
#         break
#     print()

# print('Write how many ml of water the coffee machine has:')
# max_water = int(input())
# print('Write how many ml of milk the coffee machine has:')
# max_milk = int(input())
# print('Write how many grams of coffee beans the coffee machine has:')
# max_coffee = int(input())
# print('Write how many cups of coffee you will need:')
# num = int(input())
#
# if num * 200 > max_water or num * 50 > max_milk or num * 15 > max_coffee:
#     N = min(min(max_water // 200, max_milk // 50), max_coffee // 15)
#     print('No, I can make only', N, 'cups of coffee')
# else:
#     max_water -= num * 200
#     max_milk -= num * 50
#     max_coffee -= num * 15
#     N = min(min(max_water // 200, max_milk // 50), max_coffee // 15)
#     if N >= 1:
#         print('Yes, I can make that amount of coffee (and even', N, 'more than that)')
#     else:
#         print('Yes, I can make that amount of coffee')

# print('For', num, 'cups of coffee you will need:')
# print(num * 200, 'ml of water')
# print(num * 50, 'ml of milk')
# print(num * 15, 'g of coffee beans')

# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')
