#imports
from random import randint
from time import sleep
#variables
lemonade = 0
money = 10
current_time = 0
day = 0


#functions
def display_stats():
    print("")
    print("Day: "+str(day))
    print("Cups of Lemonade: "+str(lemonade))
    print("Money: "+str(money))
    print("You have %s hours remaining in the day." % str(round(8 - current_time, 1)))
    print("")

def buy_lemonade(amount):
    global lemonade
    global money
    global current_time
    global day
    if money >= 3 * amount:
        lemonade += 10 * amount
        money -= 3 *amount
        sleep(1)
        current_time += 1
        display_stats()
    else:
        print("")
        print("You don't have enough money!")
        print("")

def sell_lemonade():
    global lemonade
    global money
    global current_time
    global day
    if lemonade > 0:
        sell_time = randint(1, 10)/10
        sell_time = round(sell_time, 1)
        sleep(sell_time)
        current_time += sell_time
        current_time = round(current_time, 1)
        lemonade -= 1
        money += 1
        display_stats()
    else:
        print("")
        print("You don't have any lemonade!")
        print("")

def check_time():
    global current_time
    global day
    if current_time >= 8:
        print("Day is done!")
        current_time = 0
        day += 1


#main game loop
print("Welcome to Lemonade Empire!  Type help for a list of commands.")
while True:
    command = input("")

    if command == "help":
        print('''
        buy_lemonade -> buys 10 cups/1 bottle of lemonade for the price of 3 dollars
        sell_lemonade -> sells lemonade for 1 dollar a cup
        display_stats -> displays how much money, lemonade, etc. you have
        exit -> quits the game
        ''')
    if command == "buy_lemonade":
        buy_amount = input("How many bottles?(1 bottle = 10 cups): ")
        try:
            buy_amount = int(buy_amount)
            buy_lemonade(buy_amount)
        except:
            print("Enter a number next time!")
    if command == "sell_lemonade":
        sell_amount = input("How much do you want to sell?: ")
        try:
            sell_amount = int(sell_amount)
            for i in range(sell_amount):
                sell_lemonade()
                check_time()
            print("Done")
        except:
            print("Enter a number next time!")
    if command == "exit":
        break
    if command == "display_stats":
        display_stats()
    check_time()
