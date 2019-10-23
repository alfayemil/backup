# Emil
# Period 4

# variable declaration and assignment
# examples
myNum = 12 # integer type 
myString = "12" # string type
print(myString + "3") # OK

# make a variable and assign it the value of your favorite movie
# print "my favorite movies is " followed by the variable 
favM = "Joker"
print("My favorite movie is: " + favM)

#while loops
# example - print from 1 to 10
x = 1 
while x <=10:
	print(x)
	x = x + 1

# count down from 100
x = 100
while x >= 1:
	print(x)
	x = x - 1

# string concatenation
# means putting two strings together
# example 
myName = "emil"
print("hello " + myName)

# input
# example
yourName = input("what is your name? ")
print("hello " + yourName + " have a nice day!")
number = input("Enter a number: ")
number = int(number) + 10
print("The number is " + str(number))

# ask for two numbers, add them and print the sum
NUM = input("type a number: ")
NUM2 = input("type another number: ")
NUM = int(NUM) + int(NUM2)
print("when you add them together, you get this: " + str(NUM))

# if / else statements
# example 
num = int(input("Enter a number: "))
if num > 100:
	print("Your number is more that 100")
elif num == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# ask if today is your birthday 
#if yes print Happy birthday

birthday = input("Is today your birthday?: ")
if birthday == "yes":
	print("HAPPY BIRTHDAY")

