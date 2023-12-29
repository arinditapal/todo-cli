from ui import print_todos, take_todo, take_delete_id, take_update_info, bubble_sort, new_print_todos
from mysql import get_all_todos, add_todo, delete_todo, update_title, update_priority, update_due_date, update_completed



# handlers

# show command arg handler
def show_handler():
    todos = get_all_todos()

    todos = bubble_sort( todos )
    # print_todos( todos )
    new_print_todos( todos )


# add command arg handler
def add_handler():
    todo = take_todo()

    if( todo["title"] ):
        add_todo( todo )
    else:
        print("\n\n:(\ttodo without title not allowed\t:(")


# delete command arg handler
def delete_handler():
    id = take_delete_id()
    delete_todo( id )

# update command arg handler
def update_handler():
    id, todo = take_update_info()

    if( todo["title"] ):
        update_title( id, todo["title"] )
    
    if( todo["priority"] ):
        update_priority( id, todo["priority"] )
    
    if( todo["due_date"] ):
        update_due_date( id, todo["due_date"] )

    if( todo["completed"] ):
        update_completed(id, todo["completed"])
    





