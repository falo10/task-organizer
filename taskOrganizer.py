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
	nameOfTask = input("\nEnter the task name:  ")
	completionDate = input ("Enter date by when the task must be completed: ")
	comment = input ("Enter the comment: ")
	database.add_task(nameOfTask, completionDate, comment)

def view_task(tasks):
	print("\nHere are all your tasks:\n") 
	for task in tasks:
			print (f"\ntask_name: {task[1]}\ntask_id: {task[0]}\nstatus: {task[4]}\ndeadline: {task[2]}\ncomment: {task[3]}\n\n")
	

def view_to_do_tasks(tasksToDo):
	print("\nHere are all your tasks:\n") 
	for task in tasksToDo:
		print (f"\ntask_name: {task[1]}\ntask_id: {task[0]}\nstatus: {task[4]}\ndeadline: {task[2]}\ncomment: {task[3]}\n\n")

def view_completed_tasks(tasksCompleted):
	print("\nHere are all your tasks:\n") 
	for task in tasksCompleted:
		print (f"\ntask_name: {task[1]}\ntask_id: {task[0]}\nstatus: {task[4]}\ndeadline: {task[2]}\ncomment: {task[3]}\n\n")


def enter_task_to_delete():
	try:
		taskIdToDelete = int(input('\nEnter the id of the task you want to remove from the list: '))
	except ValueError:
		print ("\nInvalid input! Try again!\n")
	else:
		database.delete_task(taskIdToDelete)


def enter_task_to_update():
	try:
		idOfTaskToUpdate = int(input("\nEnter the id of task that you want to update:  "))
		newCompletionDate = input ("Enter new date by when the task must be completed: ")
		newComment = input ("Enter new comment: ")
	except ValueError:
		print ("\nInvalid input! Try again!\n")
	else:
		database.update(newCompletionDate,newComment,idOfTaskToUpdate)

def enter_task_to_update_status():
	try:
		taskIdToComplete = int(input('\nEnter the id of the task you want to change status to COMPLETED: '))
	except ValueError:
		print ("\nInvalid input! Try again!\n")
	else:
		database.update_status(taskIdToComplete)


database.create_table()

print ("Welcome to Task Organizer by falo10, now You will never forget your tasks at work again!\n")

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
		print ("\nInvalid input! Try again!\n")


database.close_connection()
