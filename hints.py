#how to turn a string into a list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list with _ where the letters go 
guessList = []
for a in myList:
	guessList.append("_")

print(guessList)

#How to replace a specific item in a list
# So say the user types r for guess you would
guessList[1] = "r"
print(guessList)

