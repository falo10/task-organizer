tasks = []


def add_taks():
    nameOfTask = input("Enter the task name:  ")
    completionDate = input ("Enter date by when the task must be completed: ")
    tasks.append({"taskName": nameOfTask, "deadline date": completionDate})



def view_tasks():
    for task in tasks:
        print(f"{task['deadline date']}\n{task['taskName']}\n\n")

def delete_task():
    taskToDelete = input('Enter name of task that you want to delete: ')
    for task in tasks:
        if (task['taskName'] == taskToDelete):
            tasks.remove(task)


