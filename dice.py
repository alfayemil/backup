# Name: Emil Alfay
# Period: 4
# Dice Rolling Simulator
import random
min = 1
max = 6

roll_again = "yes"

One = 0
Two = 0
Three = 0
Four = 0
Five = 0
Six = 0

def printScore():
	print("1s: " + str(One))
	print("2s: " + str(Two))
	print("3s: " + str(Three))
	print("4s: " + str(Four))
	print("5s: " + str(Five))
	print("6s: " + str(Six))
	
rolls = int(input("How many times would you like to roll a 6-sided dice? "))

while roll_again == "yes" or roll_again == "y":
	print("Rolling the dices...")
	print("The values are...")
	print(random.randint(min,max))
	break


x = 0
while x <= rolls:
	printScore()
	x += 1
	if rolls == 1:
		One = One + 1
		
	elif rolls == 2:
		Two = Two + 1
	
	elif rolls == 3:
		Three = Three + 1
		
	elif rolls == 4:
		Four = Four + 1
		
	elif rolls == 5:
		Five = Five + 1
	
	elif rolls == 6:
		Six = Six + 1
		



		
	
