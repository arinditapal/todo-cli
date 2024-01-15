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
pipenv run python app/main.py <command>
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
0. To show all the todos 
```shell
$  pipenv run python app/main.py show
id    title                priority   due-date   completed
5     drink water           high        evening    ...
7     walk                  high        to         finish
13    buy milk              high        today      ...
6     drive bike            medium      today      ...
1     buy bread             low         today      finish
3     make ice              low         today      ...
10    got to party          low         today      ...
12    walk                  low                    ...

```
1. To add a todo

```shell
$  pipenv run python app/main.py add
enter title: buy milk
enter priority: [ low, medium, high ]: high
enter due-date: today
```

2. To delete a todo
```shell
$  pipenv run python app/main.py delete
Enter id of todo to delete: 4
```

3. To update a todo
```shell
$   pipenv run python app/main.py update

Enter id to update: 13
Do you want to change title??  [ y, n ]: n

Do you want to change priority?? [ y, n ]: n

Do you want to change due-date?? [ y, n ]: n

Do you want to change completed?? [ y, n ]: y
enter new completed:[ 0 - ongoing, 1 - finished ]: 1
```
<!-- link: [github](github.com)

image: ![sparrow](https://imgs.search.brave.com/PubjYDNzvZol2CTrocTHJs6xHuUS9v9wyyx2uTBrpRo/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNTk0/NjM0MDE4L3Bob3Rv/L3NwYXJyb3cuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPWto/RUNEd3J1TUxqaGFK/Z0ppWTdyNnZJZXpM/Ml9ITXBBaW42dlZT/elhtckk9) -->