import time 
import os

myWord = "cookie"
myString = "cookie"
myList = list(myString)

missList = []

guessList = []
for a in myList:
	guessList.append("_")

print(guessList)

count = 0


frameList = [

'''     +---+
     0   |
         |
         |
        ===''','''
     +---+
     0   |
     |   |
         |
        ===''','''
     +---+
     0   |
     |   |
    /    |
        ===''','''
     +---+
     0   |
     |   |
    / |  |
        ===''','''
     +---+
     0   |
   --|   |
    / |  |
        ===''','''
     +---+
     0   |
   --|-- |
    / |  |
        ==='''

]

mins = 0

print("Welcome to hangman.")
print("Directions: guess the word by entering one letter at a time!")
print("You have 3 minutes to guess the word. If the timer runs out, YOU LOSE.")
start = input("Do you want to start the game?(If yes type 'yes'): ")	
	
if start == "yes":
		while mins != 3:
			time.sleep(60)
			mins += 1
			pass
		print("looks like you ran outta time.")

while True:




	if guessList == ['c','o','o','k','i','e']:
		print("Nice job, you completed the word!")
		print("V I C T O R Y !")
		break

	letter = input("Type a letter: ")


	if letter == "c":
		guessList[0] = "c"
		print(guessList)
	
	elif letter == "o":
		guessList[1] = "o"
		guessList[2] = "o"
		print(guessList)

	elif letter == "k":
		guessList[3] = "k"
		print(guessList)

	elif letter == "i":
		guessList[4] = "i"
		print(guessList)

	elif letter == "e":
		guessList[5] = "e"
		print(guessList)

	else:
		print("Letter is not in the word")
		missList.append(letter)
		print("Missed letters: " + str(missList))
		count = (count) + 1
		print("Misses: " + str(count))
		if count == 1:
			print(frameList[0])
		elif count == 2:
			print(frameList[1])
		elif count == 3:
			print(frameList[2])
		elif count == 4:
			print(frameList[3])
		elif count == 5:
			print(frameList[4])
		elif count == 6:
			print(frameList[5])
			print("GAME OVER")
			break
			
for c in myString:
	if c == letter:
		print(count)
		count += 1

























