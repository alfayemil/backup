print("Welcome to the To Do List")
todolist = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")

	choice = input("Make your choice: ")
	if choice == "q":
		print("Bye!")
		break
	
	elif choice == "a": 
		item = input("Enter what you would like to add to your list: ")
		todolist.append(item)
		print("This is your list: " + str(todolist))
	
	elif choice == "r":
		removeItem = input("Enter what you want to remove from your list: ")
		todolist.remove(removeItem)
	
	elif choice == "p":
		print("Printing the list...")
		print(todolist)
		
	else:
		print("That is not a choice")

