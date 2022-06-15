from enum import IntEnum
import database

menu = """Select one of the following opotions below:
1) Add new task
2) View your tasks
3) Delete a completed task
4) Exit
Your selection: """


print ("""Welcome to Task Organizer by falo10, now You will never forget your tasks at work again!""")

MenuOptions = IntEnum('MenuOption', "Add View Delete Exit")

while ((decision:=input(menu))!= str(MenuOptions.Exit.value)):
	if (decision == str(MenuOptions.Add.value)):
		database.add_taks()
	elif (decision == str(MenuOptions.View.value)):
		database.view_tasks()
	elif (decision == str(MenuOptions.Delete.value)):
		database.delete_task()
	else:
		print ("Invalid input! Try again!")