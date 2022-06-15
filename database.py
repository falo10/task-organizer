import sqlite3

connection = sqlite3.connect("databaseTO.db")

def create_table():
    with connection:
        connection.execute('CREATE TABLE IF NOT EXISTS tasks (task_name text, deadline_date text)')

def add_task(nameOfTask, completionDate):
    with connection:
        connection.execute("INSERT INTO tasks VALUES (?, ?);", (nameOfTask, completionDate))


def get_tasks():
    cursor = connection.cursor
    cursor.execute('SELECT * FROM tasks')






        


