#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
from datetime import datetime


def printHelp():

    todohelp = \
        """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(todohelp.encode('utf8'))


def addToList(st):

    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as todoFileOri:
            data = todoFileOri.read()
        with open('todo.txt', 'w') as todoFileMod:
            todoFileMod.write(st + '\n' + data)
    else:
        with open('todo.txt', 'w') as todoFile:
            todoFile.write(st + '\n')
    sys.stdout.buffer.write('Added todo: "{}"'.format(st).encode('utf8'
                            ))


def showList():

    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as todoFileOri:
            data = todoFileOri.readlines()
        ct = len(data)
        st = ''
        for line in data:
            st += '[{}] {}'.format(ct, line)
            ct -= 1
        sys.stdout.buffer.write(st.encode('utf8'))
    else:
        sys.stdout.buffer.write('There are no pending todos!'.encode('utf8'
                                ))


def delFromList(num):

    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as todoFileOri:
            data = todoFileOri.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            sys.stdout.buffer.write('Error: todo #{} does not exist. Nothing deleted.'.format(num).encode('utf8'
                                    ))
        else:
            with open('todo.txt', 'w') as todoFileMod:
                for line in data:
                    if ct != num:
                        todoFileMod.write(line)
                    ct -= 1
            sys.stdout.buffer.write('Deleted todo #{}'.format(num).encode('utf8'
                                    ))
    else:

        sys.stdout.buffer.write('Error: todo #{} does not exist. Nothing deleted.'.format(num).encode('utf8'
                                ))


def markDone(num):

    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as todoFileOri:
            data = todoFileOri.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            sys.stdout.buffer.write('Error: todo #{} does not exist.'.format(num).encode('utf8'
                                    ))
        else:
            with open('todo.txt', 'w') as todoFileMod:
                if os.path.isfile('done.txt'):
                    with open('done.txt', 'r') as doneFileOri:
                        doneData = doneFileOri.read()
                    with open('done.txt', 'w') as doneFileMod:
                        for line in data:
                            if ct == num:
                                doneFileMod.write('x '
                                        + datetime.today().strftime('%Y-%m-%d'
                                        ) + ' ' + line)
                            else:
                                todoFileMod.write(line)
                            ct -= 1
                        doneFileMod.write(doneData)
                else:
                    with open('done.txt', 'w') as doneFileMod:
                        for line in data:
                            if ct == num:
                                doneFileMod.write('x '
                                        + datetime.today().strftime('%Y-%m-%d'
                                        ) + ' ' + line)
                            else:
                                todoFileMod.write(line)
                            ct -= 1
            sys.stdout.buffer.write('Marked todo #{} as done.'.format(num).encode('utf8'
                                    ))
    else:
        sys.stdout.buffer.write('Error: todo #{} does not exist.'.format(num).encode('utf8'
                                ))


def generateReport():

    countTodo = 0
    countDone = 0
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as todoFile:
            todoData = todoFile.readlines()
        countTodo = len(todoData)
    if os.path.isfile('done.txt'):
        countDone = 0
        with open('done.txt', 'r') as doneFile:
            doneData = doneFile.readlines()
            for i in doneData:
                temp = i.split()
                if temp[1] == str(datetime.today().strftime('%Y-%m-%d'
                                  )):
                    countDone += 1
    st = datetime.today().strftime('%Y-%m-%d') \
        + ' Pending : {} Completed : {}'.format(countTodo, countDone)
    sys.stdout.buffer.write(st.encode('utf8'))


def main():

    if len(sys.argv) == 1:
        printHelp()
    elif sys.argv[1] == 'help':
        if len(sys.argv) == 2:
            printHelp()
        else:
            sys.stdout.buffer.write('Too Many Arguments for help! Please use "./todo help" for Usage Information'.encode('utf8'
                                    ))
    elif sys.argv[1] == 'ls':
        if len(sys.argv) == 2:
            showList()
        else:
            sys.stdout.buffer.write('Too Many Arguments for ls! Please use "./todo help" for Usage Information'.encode('utf8'
                                    ))
    elif sys.argv[1] == 'add':
        if len(sys.argv) == 3:
            addToList(sys.argv[2])
        else:
            sys.stdout.buffer.write('Error: Missing todo string. Nothing added!'.encode('utf8'
                                    ))
    elif sys.argv[1] == 'del':
        if len(sys.argv) == 3:
            try:
                val = int(sys.argv[2])
                delFromList(int(sys.argv[2]))
            except ValueError:
                sys.stdout.buffer.write('Given arguement for del is not an integer! Please use "./todo help" for Usage Information'.encode('utf8'
                        ))
        else:
            sys.stdout.buffer.write('Error: Missing NUMBER for deleting todo.'.encode('utf8'
                                    ))
    elif sys.argv[1] == 'done':
        if len(sys.argv) == 3:
            try:
                val = int(sys.argv[2])
                markDone(int(sys.argv[2]))
            except ValueError:
                sys.stdout.buffer.write('Given arguement for done is not an integer! Please use "./todo help" for Usage Information'.encode('utf8'
                        ))
        else:
            sys.stdout.buffer.write('Error: Missing NUMBER for marking todo as done.'.encode('utf8'
                                    ))
    elif sys.argv[1] == 'report':
        if len(sys.argv) == 2:
            generateReport()
        else:
            sys.stdout.buffer.write('Too Many Arguments for report! Please use "./todo help" for Usage Information'.encode('utf8'
                                    ))
    else:
        sys.stdout.buffer.write('Option Not Available. Please use "./todo help" for Usage Information'.encode('utf8'
                                ))


if __name__ == '__main__':
    main()
