# Conditional
print("Welcome to Movie Bot")
age = int(input("How old are you? "))
if age > 17:
print("You can see an R rated movie")
else:
print("You can NOT see an R rated movie")

print("Have a great day")

myNum = 4
choice = int(input("Pick a number between 1 and 10: "))
if myNum == choice:
print("You guessed it")
elif choice < myNum:
print("Too low")
else:
print("Too high")

# == (equal to), <, >, <=, >=, != (not equal to)

bDay = input("Is today your birthday(yes/no): ")
if bDay == "yes":
print("Happy birthday! ")
elif bDay == "no":
print("Have a nice day anyway")
else:
print("Learn how to read directions")