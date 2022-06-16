from email.policy import default
import sqlite3

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    task_id integer PRIMARY KEY AUTOINCREMENT,
    task_name text,
    deadline_date text,
    comment text,
    status text
);"""

INSERT_INTO_TABLE = "INSERT INTO tasks(task_name, deadline_date, comment, status) VALUES (?, ?, ?, ?);"

SELECT_ALL_TASKS = 'SELECT * FROM tasks;'
SELECT_DONE_TASKS = 'SELECT * FROM tasks WHERE status = ?;'
SELECT_TASKS_TO_DO = 'SELECT * FROM tasks WHERE status = ?;'
DELETE_TASK = 'DELETE FROM task WHERE task_id = ?;'

connection = sqlite3.connect("databaseTO.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(CREATE_TASKS_TABLE)

def add_task(nameOfTask, completionDate, comment, status):
    with connection:
        connection.execute(INSERT_INTO_TABLE, (nameOfTask, completionDate, comment, status))


def get_tasks():
    cursor = connection.execute(SELECT_ALL_TASKS)
    return cursor



    






        


