import time 
import os

myWord = "cookie"
myString = "cookie"
myList = list(myString)

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

print("Welcome to hangman.")
print("Directions: guess the word by entering one letter at a time!")
while True:

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

	else:
		print("Letter is not in the word")
		count = (count) + 1
		print(count)
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

























