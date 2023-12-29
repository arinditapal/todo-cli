from colorama import Fore , Style

# giving priorities a number to be able to sort them
priorities = { "high": 0, "medium": 1, "low": 2 }

# info about what values in completed field means
completed = { 0: "...", 1: 'finish'}

# convert the completed value from db into on-going or finished
def convert_completed_field( num_completed_field ):
    return completed[num_completed_field]

todos = [ 5, 4, 3, 2, 1 ]

# bubble sort the todos
def bubble_sort( todos ):
    n = len(todos)
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if convert_completed_field(todos[j][2]) > convert_completed_field(todos[j + 1][2]):
                    todos[j], todos[j + 1] = todos[j + 1], todos[j]
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
            if i == 2:
                print( f"{Fore.YELLOW} {todo[i]} {Style.RESET_ALL}", end='\t')
                continue
            print( todo[i], end="\t")
        print()

# more prettier way of print_todos()
def new_print_todos( todos ):

    print( f"{'id':<5} {'title':<20} {'priority':<10} {'due-date':<10} {'completed':<10}" )
    for i in range( len(todos) ):
        
        todo = f"{todos[i][0]:<5} {todos[i][1]:<20} {Fore.GREEN} {todos[i][2]:<10} {Style.RESET_ALL} {todos[i][3]:<10} {convert_completed_field(todos[i][4]):<10}"

        print( todo )



# take todo details from user
def take_todo():
    todo = {}

    title = input("title: ").strip()
    priority = input("priority: [low, medium, high]: ").strip()
    due_date = input("due-date: ").strip()

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
        title = input("New title: ").strip()
    
    choice = input("Do you want to change priority?? y or n: ")
    if( choice == 'y' or choice == 'Y'):
        priority = input("New priority: ").strip()
    
    choice = input("Do you want to change due-date?? y or n: ")
    if( choice == 'y' or choice == 'Y'):
        due_date = input("New due-date: ").strip()

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

