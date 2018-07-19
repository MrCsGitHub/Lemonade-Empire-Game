#dependencies
from random import randint
from time import sleep
#variables
money = 10


#classes
class time:
    def __init__(self, current_time, day):
        self.day = day
        self.current_time = current_time
    def tick(self):
        self.current_time -= 1
        if self.current_time == 0:
            self.day += 1
            self.current_time = 8
    def display(self):
        print("You have %s hours left in the day." % str(self.current_time))
        print("Day "+str(self.day))
t = time(8, 0)

class lemonade_storage:
    def __init__(self, stored, storage):
        self.stored = stored
        self.storage = storage
    def buy(self, amount_bought):
        global money
        if self.stored + amount_bought * 10 > self.storage:
            print("You can't store that much lemonade!")
        elif money < 3 * amount_bought:
            print("You don't have enough money!")
        else:
            self.stored += amount_bought * 10
            money -= 3 * amount_bought
            t.tick()
    def sell(self, how_long):
        global money
        for i in range(how_long):
            if self.stored > 0:
                for i in range(randint(1, 5)):
                    if self.stored > 0:
                        self.stored -= 1
                        money += 1
                    else:
                        break
            else:
                print("You don't have more any lemonade!")
                break
            t.tick()
l = lemonade_storage(0, 100)

def display_stats():
    print("")
    t.display()
    print("Cups of Lemonade: "+str(l.stored))
    print("Money: "+str(money))
    print("")


#main game loop
while True:
    command = input("")

    if command == "help":
        print('''
        buy_lemonade -> buys 10 cups/1 bottle of lemonade for the price of 3 dollars
        sell_lemonade -> sells lemonade for 1 dollar a cup
        display_stats -> displays how much money, lemonade, etc. you have
        exit -> quits the game
        ''')
    if command == "exit":
        break
    if command == "display_stats":
        display_stats()

    if command == "buy_lemonade":
        amount = input("How many bottles?(1 bottle = 10 cups):")
        try:
            amount = int(amount)
            l.buy(amount)
            display_stats()
        except:
            print("Enter a number next time!")
    if command == "sell_lemonade":
        try:
            how_long = input("How long do you want to sell for?")
            how_long = int(how_long)
            l.sell(how_long)
            display_stats()
        except:
            print("Enter a number next time!")
