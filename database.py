from email.policy import default
import sqlite3

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    task_id integer PRIMARY KEY AUTOINCREMENT,
    task_name text,
    deadline text,
    comment text,
    status text
);"""

INSERT_INTO_TABLE = "INSERT INTO tasks(task_name, deadline, comment, status) VALUES (?, ?, ?, ?);"

SELECT_ALL_TASKS = 'SELECT * FROM tasks;'
SELECT_COMPLETED_TASKS = 'SELECT * FROM tasks WHERE status = ?;'
SELECT_TASKS_TO_DO = 'SELECT * FROM tasks WHERE status = ?;'
DELETE_TASK = 'DELETE FROM tasks WHERE task_id = ?;'
UPDATE_TASK = 'UPDATE tasks SET deadline =?, comment=? WHERE task_id=?;'
UPDATE_STATUS = 'UPDATE tasks SET status = ? WHERE task_id=?;'

completedStatus = "COMPLETED"
statusDefault = 'TO DO'

connection = sqlite3.connect("databaseTO.db")





def create_table():
    with connection:
        connection.execute(CREATE_TASKS_TABLE)

def add_task(nameOfTask, completionDate, comment):
    with connection:
        connection.execute(INSERT_INTO_TABLE, (nameOfTask, completionDate, comment, statusDefault))

def get_tasks():
    cursor = connection.execute(SELECT_ALL_TASKS)
    return cursor

def get_to_do_tasks():
    cursor = connection.execute(SELECT_TASKS_TO_DO, (statusDefault,))
    return cursor
    
def get_completed_tasks():
    cursor = connection.execute(SELECT_COMPLETED_TASKS, (completedStatus,))
    return cursor

def delete_task(taskIdToDelete):
        with connection:
            connection.execute(DELETE_TASK, (taskIdToDelete,))
    
    

def update (newCompletionDate,newComment, idOfTaskToUpdate):
    with connection:
        connection.execute(UPDATE_TASK, (newCompletionDate, newComment, idOfTaskToUpdate))

def update_status (taskIdToComplete):
    with connection:
        connection.execute(UPDATE_STATUS,(completedStatus, taskIdToComplete))


def close_connection ():
    connection.close()