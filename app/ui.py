# giving priorities a number to be able to sort them
priorities = { "high": 0, "medium": 1, "low": 2 }

# bubble sort the todos
def bubble_sort( todos ):
    for i in range( len(todos) - 1):
        if priorities[ todos[i][2] ] > priorities[ todos[i + 1][2] ]:
            todos[i], todos[i + 1] = todos[i + 1], todos[i]
    return todos

# show all todos
def print_todos( todos ):

    for todo in todos:
        for i in range(len(todo)):
            if i == 4 : 
                if todo[i]:
                    print("finished", end="\t")
                else:
                    print("ongoing", end='\t')
                continue
            print( todo[i], end="\t")
        print()


# take todo details from user
def take_todo():
    todo = {}

    title = input("title: ")
    priority = input("priority: [low, medium, high]: ")
    due_date = input("due-date: ")

    todo["title"] = title
    todo["priority"] = priority
    todo["due_date"] = due_date

    return todo

# take id to delete from user
def take_delete_id():

    id = int( input("Enter id of todo to delete: ") )

    return id

# take id, update todo from user
def take_update_info():

    id = int(  input( "Enter id to update: ") )
    
    title, priority, due_date, completed = None, None, None, None

    choice = input("Do you want to change title??  y or n: ")
    if( choice == 'y' or choice == 'Y' ):
        title = input("New title: ")
    
    choice = input("Do you want to change priority?? y or n: ")
    if( choice == 'y' or choice == 'Y'):
        priority = input("New priority: ")
    
    choice = input("Do you want to change due-date?? y or n: ")
    if( choice == 'y' or choice == 'Y'):
        due_date = input("New due-date: ")

    choice = input("Do you want to change completed?? y or n: ")
    if( choice == 'y' or choice == 'Y'):
        completed = int(input("New completed:[0 - ongoing, 1 - finished] "))

    todo = { 
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": completed
    }

    return id, todo

