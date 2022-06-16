from enum import IntEnum
import database


menu = """Select one of the following opotions below:
1) Add new task
2) View your tasks
3) Exit
Your selection: """


def enter_task():
	nameOfTask = input("Enter the task name:  ")
	completionDate = input ("Enter date by when the task must be completed: ")
	comment = input ("Enter the comment: ")
	status = 'to do'
	database.add_task(nameOfTask, completionDate, comment, status)

def view_task(tasks):
	for task in tasks:
		print (f"{task['deadline_date']}\n{task['task_name']}\n{task['comment']}\n\n")


database.create_table()

print ("""Welcome to Task Organizer by falo10, now You will never forget your tasks at work again!""")

MenuOptions = IntEnum("MenuOption", "Add View Exit")

while ((decision:=input(menu))!= str(MenuOptions.Exit.value)):
	if (decision == str(MenuOptions.Add.value)):
		enter_task()
		print ("Task has been successfully added to your task list\n")
	elif (decision == str(MenuOptions.View.value)):
		view_task(database.get_tasks())
	else:
		print ("Invalid input! Try again!")