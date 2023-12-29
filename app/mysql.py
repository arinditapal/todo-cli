import sqlite3


conn = sqlite3.connect("todos.db")

cur = conn.cursor()


# get all todos
def get_all_todos():

    sql = "SELECT * FROM todos"
    result = cur.execute( sql )
    todos = result.fetchall()

    return todos

# add  one todo
def add_todo( todo ):

    title = todo['title']
    priority = todo['priority']
    due_date = todo['due_date']

    sql = f"INSERT INTO todos(title, priority, due_date) VALUES( '{title}', '{priority}', '{due_date}')"
    result = cur.execute( sql )
    conn.commit()


# delete one todo
def delete_todo( id ):

    sql = f" DELETE FROM todos WHERE id = { id } "
    cur.execute( sql )
    conn.commit()


# update title
def update_title( id, title ):
    sql = f"UPDATE todos SET title = '{title}' WHERE id = { id }"
    cur.execute( sql )
    conn.commit()

# update priority 
def update_priority( id, priority ):
    sql = f"UPDATE todos SET priority = {priority} WHERE id = { id }"
    cur.execute( sql )
    conn.commit()

# update due-date
def update_due_date( id, due_date ):
    sql = f"UPDATE todos SET due_date = '{due_date}' WHERE id = { id }"
    cur.execute( sql )
    conn.commit()

# update completed field
def update_completed( id, completed ):
    sql = f"UPDATE todos SET completed = {completed} WHERE id = { id }"
    cur.execute( sql )
    conn.commit()
    