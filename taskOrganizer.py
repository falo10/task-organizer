

menu = """Select one of the following opotions below:
1) Add new task
2) View your tasks
3) Delete a completed task

Your selection: """


print ("""Welcome to Task Organizer by falo10, now You will never forget your tasks at work again!""")


while ((decision:=input(menu))!= 3):
	if (decision == "1"):
		print ("lets add.....")
	elif (decision == "2"):
		print ("lets check...")
	else:
		print ("Invalid input! Try again!")