from email.policy import default
import sqlite3

connection = sqlite3.connect("databaseTO.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute('CREATE TABLE IF NOT EXISTS tasks (task_id integer PRIMARY KEY AUTOINCREMENT, task_name text, deadline_date text, comment text, status text)')

def add_task(nameOfTask, completionDate, comment, status):
    with connection:
        connection.execute("INSERT INTO tasks (task_name, deadline_date, comment, status) VALUES (?, ?, ?, ?);", (nameOfTask, completionDate, comment, status))


def get_tasks():
    cursor = connection.execute('SELECT * FROM tasks')
    return cursor



    






        


