#imports
from random import randint
from time import sleep
#variables
lemonade = 0
money = 10
current_time = 0


#functions
def buy_lemonade():
    global lemonade
    global money
    global current_time
    if money >= 3:
        lemonade += 10
        money -= 3
        current_time += 1
        print("")
        print("Cups of Lemonade: "+str(lemonade))
        print("Money left: "+str(money))
        print("You have %s hours remaining in the day." % str(round(8 - current_time, 1)))
        print("")
    else:
        print("")
        print("You don't have enough money!")
        print("")

def sell_lemonade():
    global lemonade
    global money
    global current_time
    if lemonade > 0:
        sell_time = randint(1, 10)/10
        sell_time = round(sell_time, 1)
        sleep(sell_time)
        current_time += sell_time
        current_time = round(current_time, 1)
        lemonade -= 1
        money += 1
        print("")
        print("Cups of Lemonade: "+str(lemonade))
        print("Money: "+str(money))
        print("You have %s hours remaining in the day." % str(round(8 - current_time, 1)))
        print("")
    else:
        print("")
        print("You don't have any lemonade!")
        print("")


#main game loop
print("Welcome to Lemonade Empire!  Type help for a list of commands.")
while True:
    command = input("")

    if command == "help":
        print('''
        buy_lemonade -> buys 10 cups of lemonade for the price of 3 dollars
        sell_lemonade -> sells lemonade for 1 dollar a cup
        display_stats -> displays how much money, lemonade, etc. you have
        exit -> quits the game
        ''')
    if command == "buy_lemonade":
        buy_lemonade()
    if command == "sell_lemonade":
        sell_lemonade()
    if command == "exit":
        break
    if command == "display_stats":
        print("")
        print("Cups of Lemonade: "+str(lemonade))
        print("Money: "+str(money))
        print("You have %s hours remaining in the day." % str(round(8 - current_time, 1)))
        print("")
    if current_time > 8:
        print("Day is done!")
        current_time = 0
