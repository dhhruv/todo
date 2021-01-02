# Todo List Script..

This Script/Program is written as a part of CoronaSafe Engineering Fellowship Test Problem by Pupilfirst in the Python Programming Language passing all the test cases as given in the .js file.

**Tested on Windows OS.**
**Author: Dhruv Panchal**

## Getting started

1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command
    ```
    python3 --version
    ```
    This should output some information on the installed Python version.
    You can also install ruby by following these instructions. https://installpython3.com/

2. You are expected to write the code in `todo.py` file.

3. Once you are done with the changes you should be able to execute the todo app by running the following command from the terminal.

   **On Windows:**

   ```
   todo.bat
   ```

## Run Automated Tests

1. Install Node.js: You need to have npm installed in your computer for this problem. It comes with Node.js and you can get it by installing Node from https://nodejs.org/en/

2. Run `npm install` to install all dependencies

3. Create symbolic link to the executable file

   **On Windows:**

   ```
   > mklink todo todo.bat
   ```
   **Note: This is a mandatory step else you've to use `todo.bat` instead of `todo` in the Command Prompt in Windows OS.**

4. Now run `npm test` and you will see all the tests failing. As you fill in each functionality, you can re-run the tests to see them passing one by one.

## Specification

1. The app can be run in the console with `./todo`.

2. The app should read from and write to a `todo.txt` text file. Each todo item occupies a single line in this file. Here is an example file that has 2 todo items.

    ```txt
    water the plants
    change light bulb
    ```

3.  When a todo item is completed, it should be removed from `todo.txt` and instead added to the `done.txt` text file. This file has a different format:

    ```txt
    x 2020-06-12 the text contents of the todo item
    ```

    1. the letter x
    2. the current date in `yyyy-mm-dd` format
    3. the original text

    The date when the todo is marked as completed is recorded in the `yyyy-mm-dd` format (ISO 8601). For example, a date like `15th August, 2020` is represented as `2020-08-15`.

    **Note:- Here I added a something out of the box where `todo report` will generate the pending and completed tasks of the current day so if there are completed tasks in `done.txt` of days other than current day then they won't be counted in the report of current day.**

4.  The application must open the files `todo.txt` and `done.txt` from where the app is run, and not where the app is located. For example, if we invoke the app like this:

    ```
    $ cd ~/plans
    $ ~/apps/todo ls
    ```
    The application should look for the text files in `~/plans`, since that is the user’s current directory.

    **Note:- To make the above specification work, I changed the `todo.bat` from**
    ```
    @echo off
    python3 todo.py %1 %2
    ``` 
    **to**
    ```
    @echo off
    python "%~dp0\todo.py" %1 %2
    ```
    **This will operate the `todo.py` Script from the Current Directory where the Command Prompt is used so the above mentioned specification is solved.**



## Usage

### 1. Help

Executing the command without any arguments, or with a single argument `help` prints the CLI usage.

```
$ ./todo help
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
```
**Note: If there are arguments after help for eg. `todo help abc` then it will throw an Exception due to given specifications in the Initial README and will recommend to use `todo help`.**

### 2. List all pending todos

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo should be displayed first.

```
$ ./todo ls
[2] change light bulb
[1] water the plants
```
**Note: If there are arguments after ls for eg. `todo ls abc` then it will throw an Exception due to given specifications in the Initial README and will recommend to use `todo help`.**

### 3. Add a new todo

Use the `add` command. The text of the todo item should be enclosed within double quotes (otherwise only the first word is considered as the todo text, and the remaining words are treated as different arguments).

```
$ ./todo add "the thing i need to do"
Added todo: "the thing i need to do"
```

### 4. Delete a todo item

Use the `del` command to remove a todo item by its number.

```
$ ./todo del 3
Deleted todo #3
```

Attempting to delete a non-existent todo item should display an error message.

```
$ ./todo del 5
Error: todo #5 does not exist. Nothing deleted.
```
**Note: The Script will throw an Exception if the passed argument is not an integer for eg. `todo del abc` will throw an Exception so it is mandatory to pass an integer.**

### 5. Mark a todo item as completed

Use the `done` command to mark a todo item as completed by its number.

```
$ ./todo done 1
Marked todo #1 as done.
```

Attempting to mark a non-existed todo item as completed will display an error message.

```
$ ./todo done 5
Error: todo #5 does not exist.
```
**Note: The Script will throw an Exception if the passed argument is not an integer for eg. `todo done abc` will throw an Exception so it is mandatory to pass an integer.**

### 6. Generate a report

Use the `report` command to see the latest tally of pending and completed todos.

```
$ ./todo report
dd/mm/yyyy Pending : 1 Completed : 4
```
**Note: If there are arguments after report for eg. `todo report abc` then it will throw an Exception due to given specifications in the Initial README and will recommend to use `todo help`. Here I added a something out of the box where `todo report` will generate the pending and completed tasks of the current day so if there are completed tasks in `done.txt` of days other than current day then they won't be counted in the report of current day.**