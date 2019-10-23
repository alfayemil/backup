# how to make a list
favMovies = ["Star Wars, J:OMEGALUL:KER, JOJO,"]
# print the whole list
print(favMovies)
# print individuals 
print(favMovies[0])
# to add you can append or insert
# append adds to the end
favMovies.append("Killer Bean")
print(favMovies)
# insert will put the item wherever you want
favMovies.insert(1,"Harry Potter")
print(favMovies)
# how to remove items
# remove by name or by index
# remove by name or use remove
favMovies.remove("Killer Bean")
print(favMovies)
#favMovies.remove("Endgame")
# pop will remove the last item unless an index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remoxe whaterver ids in index
print(favMovies)
# get the length of the list
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("What is your favorite movie? ")
favMovies.append(favMovie)
print(favMovie)
print(favMovies[len(favMovies) - 1])  

# loop through a list
count = 1 

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie)
	count = count + 1

numList = [1,3,5,7,9,11,13,15]
# challenge: loop through the list and add all the numbers together, then print the sum
total = 0

for number in numList:
	total = total + number

print("The sum is " + str(total))


