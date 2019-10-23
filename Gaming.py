import random

howUgly = random.randint(1, 100)
score = 0

while True: 
	guess = int(input("Guess the number is from 1 to 100: "))
	score += 1 #guess = guess + 1 
	if guess == howUgly: 
		print("Good job, you guessed it!")
		break
	elif guess > howUgly: 
		print("Too high, try again")
	else:
		print("Too low, try again")

print("You tried " + str(score) + " times")

