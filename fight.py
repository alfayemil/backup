print("Welcome to fighting simulator")
Pname = input("Whats your name? ")
print("Okay " + Pname)
print("Let's start the fight")
import random
Phealth = 5
Chealth = 20

while True:
	print("Wanna punch? press P.")
	print("Wanna kick? press K.")

	choice = input("What's it going to be?: ")
	if choice == "P":	
		Chealth = Chealth - 2
		print("OPPONENT HP: " + str(Chealth))
		pass

	elif choice == "K":
		Chealth = Chealth - 3
		print("OPPONENT HP: " + str(Chealth))
		pass
		

	elif choice == "S":
		print("I see. It looks like you have discovered this secret move")
		print("YOUR OPPONENT IS DEAD")
		Chealth = Chealth - 20
		print(Chealth)

	else:
		print("Cmon man! You can't do that!")


