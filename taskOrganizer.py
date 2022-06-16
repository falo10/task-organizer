from enum import IntEnum
import database


menu = """Select one of the following opotions below:
1) Add new task
2) View all your tasks
3) View tasks to do
4) View completed tasks
5) Delete the task from your list
6) Change deadline and comment of task
7) Mark the task as completed
8) Exit
Your selection: """


def enter_task():
	nameOfTask = input("Enter the task name:  ")
	completionDate = input ("Enter date by when the task must be completed: ")
	comment = input ("Enter the comment: ")
	database.add_task(nameOfTask, completionDate, comment)

def view_task(tasks):
	for task in tasks:
		print (f"\n{task['task_id']}\n{task['status']}\n{task['deadline']}\n{task['task_name']}\n{task['comment']}\n\n")


def view_to_do_tasks(tasksToDo):
	print("""
Here are all your tasks to do:
			""")
	for task in tasksToDo:
		print (f"\n{task['deadline']}\n{task['task_name']}\n{task['comment']}\n\n")

def view_completed_tasks(tasksCompleted):
	for task in tasksCompleted:
		print("""
Here are all your completed tasks:
			""")
		print (f"\n{task['deadline']}\n{task['task_name']}\n{task['comment']}\n\n")


def enter_task_to_delete():
	taskIdToDelete = int(input('Enter the id of the task you want to remove from the list: '))
	database.delete_task(taskIdToDelete)


def enter_task_to_update():
	idOfTaskToUpdate = int(input("Enter the id of task that you want to update:  "))
	newCompletionDate = input ("Enter new date by when the task must be completed: ")
	newComment = input ("Enter new comment: ")
	database.update(newCompletionDate,newComment,idOfTaskToUpdate)

def enter_task_to_update_status():
	taskIdToComplete = int(input('Enter the id of the task you want to change status to COMPLETED: '))
	database.update_status(taskIdToComplete)


database.create_table()

print ("""Welcome to Task Organizer by falo10, now You will never forget your tasks at work again!""")

MenuOptions = IntEnum("MenuOption", "Add View To_DO Completed Delete Update Status Exit")

while ((decision:=input(menu))!= str(MenuOptions.Exit.value)):
	if (decision == str(MenuOptions.Add.value)):
		enter_task()
		print ("Task has been successfully added to your task list\n")
	elif (decision == str(MenuOptions.View.value)):
		view_task(database.get_tasks())
	elif (decision == str(MenuOptions.To_DO.value)):
		view_to_do_tasks(database.get_to_do_tasks())
	elif (decision == str(MenuOptions.Completed.value)):
		view_completed_tasks(database.get_completed_tasks())
	elif (decision == str(MenuOptions.Delete.value)):
		enter_task_to_delete()
	elif (decision == str(MenuOptions.Update.value)):
		enter_task_to_update()
	elif (decision == str(MenuOptions.Status.value)):
		enter_task_to_update_status()
	else:
		print ("Invalid input! Try again!")