import sqlite3


CREATE_USERS_TABLE =  """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
);"""

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    deadline TEXT,
    comment TEXT,
    status TEXT,
    date_timestamp REAL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id)
);"""


INSERT_INTO_TASKS_TABLE = "INSERT INTO tasks(task_name, deadline, comment, status, date_timestamp, user_id) VALUES (?, ?, ?, ?, ?, ?);"
INSERT_INTO_USERS_TABLE = "INSERT INTO users(first_name, last_name) VALUES (?, ?);"


SELECT_USER_ID = 'SELECT * FROM users;'
SELECT_ALL_TASKS = 'SELECT * FROM tasks;'
SELECT_COMPLETED_TASKS = 'SELECT * FROM tasks WHERE status = ?;'
SELECT_TASKS_TO_DO = 'SELECT * FROM tasks WHERE status = ? ORDER BY date_timestamp;'
DELETE_TASK = 'DELETE FROM tasks WHERE id = ?;'
DELETE_USER = 'DELETE FROM users WHERE id = ?;'
UPDATE_TASK = 'UPDATE tasks SET deadline =?, comment=? WHERE id=?;'
UPDATE_STATUS = 'UPDATE tasks SET status = ? WHERE id=?;'

completedStatus = "COMPLETED"
statusDefault = 'TO DO'

connection = sqlite3.connect("databaseTO.db")


def create_table():
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_TASKS_TABLE)
        

def add_user(firstName, lastName):
     with connection:
        connection.execute(INSERT_INTO_USERS_TABLE, (firstName, lastName))


def get_users():
    cursor = connection.execute(SELECT_USER_ID)
    return cursor


def add_task(nameOfTask, completionDate, comment, timestamp, userId):
    with connection:
        connection.execute(INSERT_INTO_TASKS_TABLE, (nameOfTask, completionDate, comment, statusDefault, timestamp, userId))

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

def delete_user(userIdToDelete):
        with connection:
            connection.execute(DELETE_USER, (userIdToDelete,))
    
    
def update (newCompletionDate,newComment, idOfTaskToUpdate):
    with connection:
        connection.execute(UPDATE_TASK, (newCompletionDate, newComment, idOfTaskToUpdate))

def update_status (taskIdToComplete):
    with connection:
        connection.execute(UPDATE_STATUS,(completedStatus, taskIdToComplete))


def close_connection ():
    connection.close()