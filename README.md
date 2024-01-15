# Todo App

This is Todo App, a cli application in python for keeping track of you todo's.

## Set up
To get started, clone this repository, then run the following command.
```
pipenv install
```
This should install all the required dependencies from the pipfile in your working folder.

## Running
You can start using the app by running the python file in app folder, app/main.py. Followed by a command that satisfies what you want to do.

```
pipenv run python app/main.py < command >
```

You can see the list of commands that you can use for interacting with the app.

```
pipenv run python app/main.py --help
```
The commands should appear in the value of "prositional argument".
> The above code assumes that you have entire code form this github repository cloned in your PC, then you can use it, other wise you'll need to install some package listed in the "pipfile" in above list of files.

## Commands

* show
    - This command line argument will show all the todos.
* add
    - Use this to add a new todo.
* delete
    - Use this to delete a todo.
* update
    - Use this to update a todo, like updating the todo's status from incompleted to completed.

## Example
This example will show how to add a new todo into the app. Run the following command

```
pipenv run python app/main.py add
```
Here "add" is the command for the app.
> Pipenv is used to run the file inside of virtual environment without enter the virtual environment, so pipenv run is the command for that.

You may find the following prompts:
```
enter title: 
enter priority: [ low, medium, high ]:
enter due-date:
```

you can also user the other commands inplace of "add" command.
