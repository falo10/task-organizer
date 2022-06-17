import datetime
from enum import IntEnum
import database


menu = """Select one of the following opotions below:
1) Add new user
2) Add new task
3) View all your tasks
4) View tasks to do (in order of the deadline)
5) View completed tasks
6) Delete the task from your list
7) Change deadline and comment of task
8) Mark the task as completed
9) Delete user
10) Exit
Your selection: """


def enter_new_user():
	firstName = input('\nEnter first name of the user: ')
	lastName = input('\nEnter last name of the user: ')
	database.add_user(firstName, lastName)


def enter_task():
	try:
		userId = int(input("\nEnter the id of the user for which you want to add the task: "))
	except ValueError:
		print ("\nInvalid input! Try again!\n")
		return True
	nameOfTask = input("\nEnter the task name:  ")
	try:
		completionDate = input ("Enter date by when the task must be completed (dd-mm-YYYY): ")
		completionDateFormat = datetime.datetime.strptime(completionDate, "%d-%m-%Y")
	except ValueError:
		print ("\nInvalid input! Please enter the date with the format (dd-mm-YYYY)\n")
		return True
	else:
		try:
			timestamp = completionDateFormat.timestamp()
		except OSError:
			print ("\nIt cannot be a date before 1970\n")
			return True
	comment = input ("Enter the comment: ")
	database.add_task(nameOfTask, completionDate, comment, timestamp, userId)
	print ("Task has been successfully added to your task list!\n")

def view_users_id(users):
	print ('Here is the list of available users:\n')
	for user in users:
		print (f"{user[1]} {user[2]} -> id = {user[0]}")
	print('\n')


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


def enter_user_to_delete():
	try:
		taskIdToDelete = int(input('\nEnter the id of the user you want to remove from the list: '))
	except ValueError:
		print ("\nInvalid input! Try again!\n")
	else:
		users = database.get_users()
		for user in users:
			if (user[0] == taskIdToDelete):
				print ('ok')
				userFirstNameToDelete = user[1]
				userLastNameToDelete = user[2]	
				decisionToDeleteUser = input (f"You will not be able to undo your decision!!!\n\nAre you sure you want to delete user {userFirstNameToDelete} {userLastNameToDelete}? yes/no: ")
				if (decisionToDeleteUser.upper() == 'YES'):
					database.delete_user(taskIdToDelete)
				elif (decisionToDeleteUser.upper() == 'NO'):
					return True
				else: 
					print ("\nInvalid input!\n") 			
			else:
				continue
		

def enter_task_to_delete():
	try:
		userIdToDelete = int(input('\nEnter the id of the user you want to delete: '))
	except ValueError:
		print ("\nInvalid input! Try again!\n")
	else:

		database.delete_user(userIdToDelete)


def enter_task_to_update():
	try:
		idOfTaskToUpdate = int(input("\nEnter the id of task that you want to update: "))
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

MenuOptions = IntEnum("MenuOption", "User Add View To_DO Completed Delete Update Status DeleteUser Exit")

while ((decision:=input(menu))!= str(MenuOptions.Exit.value)):
	if (decision == str(MenuOptions.User.value)):
		enter_new_user()
		view_users_id(database.get_users())
	elif (decision == str(MenuOptions.Add.value)):
		enter_task()
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
	elif (decision == str(MenuOptions.DeleteUser.value)):
		enter_user_to_delete()
	else:
		print ("\nInvalid input! Try again!\n")


database.close_connection()
