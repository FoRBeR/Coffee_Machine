class CoffeeMachine:
    def __init__(self, start_water, start_milk, start_coffee, start_cups, start_money):
        self.water = start_water
        self.milk = start_milk
        self.coffee = start_coffee
        self.cups = start_cups
        self.money = start_money
        self.input_now = 'action'  # action | buy | add_w | add_m | add_cb | add_c

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def state(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def is_enough(self, t_c):
        if self.cups == 0:
            print('Sorry, not enough disposable cups!')
            return False
        if t_c == 1:
            if self.water < 250:
                print('Sorry, not enough water!')
                return False
            elif self.coffee < 16:
                print('Sorry, not enough coffee!')
                return False
            else:
                print('I have enough resources, making you a coffee!')
                return True
        elif t_c == 2:
            if self.water < 350:
                print('Sorry, not enough water!')
                return False
            elif self.milk < 75:
                print('Sorry, not enough milk!')
                return False
            elif self.coffee < 20:
                print('Sorry, not enough coffee!')
                return False
            else:
                print('I have enough resources, making you a coffee!')
                return True
        elif t_c == 3:
            if self.water < 200:
                print('Sorry, not enough water!')
                return False
            elif self.milk < 100:
                print('Sorry, not enough milk!')
                return False
            elif self.coffee < 12:
                print('Sorry, not enough coffee!')
                return False
            else:
                print('I have enough resources, making you a coffee!')
                return True

    def cooking(self, t_c):
        if self.is_enough(t_c):
            if t_c == 1:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
            elif t_c == 2:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
            elif t_c == 3:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6

    def str_in(self, string):
        if self.input_now == 'action':
            if string[0] == 'e':
                return False
            elif string[0] == 'r':
                self.state()
            elif string[0] == 'f':
                self.input_now = 'add_w'
                print('Write how many ml of water do you want to add:')
            elif string[0] == 't':
                self.take()
            elif string[0] == 'b':
                self.input_now = 'buy'
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        elif self.input_now == 'buy':
            if string[0] != 'b':
                self.cooking(int(string))
            self.input_now = 'action'
        elif self.input_now == 'add_w':
            self.water += int(string)
            print('Write how many ml of milk do you want to add:')
            self.input_now = 'add_m'
        elif self.input_now == 'add_m':
            self.milk += int(string)
            print('Write how many grams of coffee beans do you want to add:')
            self.input_now = 'add_cb'
        elif self.input_now == 'add_cb':
            self.coffee += int(string)
            print('Write how many disposable cups of coffee do you want to add:')
            self.input_now = 'add_c'
        elif self.input_now == 'add_c':
            self.cups += int(string)
            self.input_now = 'action'
        return True


MyMachine = CoffeeMachine(400, 540, 120, 9, 550)
while (MyMachine.str_in(input())):
    continue
