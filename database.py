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
    users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users(id) ON DELETE CASCADE
);"""

INSERT_INTO_TASKS_TABLE = 'INSERT INTO tasks(task_name, deadline, comment, status, date_timestamp, users_id) VALUES (?, ?, ?, "TO DO", ?, ?);'
INSERT_INTO_USERS_TABLE = 'INSERT INTO users(first_name, last_name) VALUES (?, ?);'




SELECT_USER_ID = 'SELECT * FROM users;'
SELECT_ALL_TASKS = 'SELECT * FROM tasks;'
SELECT_COMPLETED_TASKS = 'SELECT * FROM tasks WHERE status = "COMPLETED";'
SELECT_TASKS_TO_DO = 'SELECT * FROM tasks WHERE status = "TO DO" ORDER BY date_timestamp;'

SELECT_ALL_USER_TASKS = 'SELECT * FROM tasks JOIN users ON tasks.users_id = users.id WHERE users.id = ?;'
SELECT_COMPLETED_USER_TASKS = 'SELECT * FROM tasks JOIN users ON tasks.users_id = users.id WHERE users.id = ? AND tasks.status = "COMPLETED";'
SELECT_TO_DO_USER_TASKS = 'SELECT * FROM tasks JOIN users ON tasks.users_id = users.id WHERE users.id = ? AND tasks.status = "TO DO" ORDER BY date_timestamp;'

DELETE_TASK = 'DELETE FROM tasks WHERE id = ?;'
DELETE_USER = 'DELETE FROM users WHERE id = ?;'
UPDATE_TASK = 'UPDATE tasks SET deadline =?, comment=? WHERE id=?;'
UPDATE_STATUS = 'UPDATE tasks SET status = "COMPLETED" WHERE id=?;'


connection = sqlite3.connect("databaseTO.db")
connection.execute("PRAGMA foreign_keys = 1")


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
        try:
            connection.execute(INSERT_INTO_TASKS_TABLE, (nameOfTask, completionDate, comment, timestamp, userId))
        except sqlite3.IntegrityError:
            print ('\nUser with that id does not exist. Try again!\n')

def get_tasks(userId):
    cursor = connection.execute(SELECT_ALL_USER_TASKS, (userId,))
    return cursor

def get_to_do_tasks(userId):
    cursor = connection.execute(SELECT_TO_DO_USER_TASKS, (userId,))
    return cursor
    
def get_completed_tasks(userId):
    cursor = connection.execute(SELECT_COMPLETED_USER_TASKS, (userId,))
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
        connection.execute(UPDATE_STATUS,(taskIdToComplete,))

def close_connection ():
    connection.close()