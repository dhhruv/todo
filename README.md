<h1 align="center" style="margin-top: -4px !important;">Todo List Client...</h2>
<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen">
  <img src="https://img.shields.io/badge/python-3.8-blue">
  <img src="https://img.shields.io/badge/os-windows-success">
</p>

This Script/Program is written as a part of CoronaSafe Engineering Fellowship Test Problem by Pupilfirst in the Python Programming Language passing all the test cases as given in the .js file. Proof of all Test Cases passing is as shown below.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/102444820-13485180-4050-11eb-8de3-ed3b0a86c13d.PNG">
</p>
<br>

## Getting started

1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command

	```
	  python3 --version

	```
  This should output some information on the installed Python version.
	You can also install ruby by following these instructions. https://installpython3.com/

2. You are expected to write the code in `todo.py` file.

3. Once you are done with the changes you should be able to execute the todo app by running the following commandfrom the terminal.

   **On Windows:**

   ```
   ./todo.bat
   ```

   **On \*nix:**

   ```
   ./todo.sh
   ```

## Run Automated Tests

1. Install Node.js: You need to have npm installed in your computer for this problem. It comes with Node.js and you can get it by installing Node from https://nodejs.org/en/

2. Run `npm install` to install all dependencies

3. Create symbolic link to the executable file

   **On Windows:**

   ```
   > mklink todo todo.bat
   ```

   **On \*nix:**

   ```
   $ ln -s todo.sh todo
   ```

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

4.  The application must open the files `todo.txt` and `done.txt` from where the app is run, and not where the app is located. For example, if we invoke the app like this:

    ```
    $ cd ~/plans
    $ ~/apps/todo ls
    ```

    The application should look for the text files in `~/plans`, since that is the user’s current directory.

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

### 2. List all pending todos

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo should be displayed first.

```
$ ./todo ls
[2] change light bulb
[1] water the plants
```

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

### 6. Generate a report

Use the `report` command to see the latest tally of pending and completed todos.

```
$ ./todo report
dd/mm/yyyy Pending : 1 Completed : 4
```
