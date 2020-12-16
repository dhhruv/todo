import sys
import os.path
from datetime import datetime

todohelp="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""

def addToList(st):

	if os.path.isfile('todo.txt'):
	    print ("File exist")
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.read()
	    with open("todo.txt",'w') as todoFileMod:
	    	todoFileMod.write(st+'\n'+data)
	else:
	    print ("File doesn't exist")
	    with open("todo.txt",'w') as todoFile:
	    	todoFile.write(st+'\n')
	print('Added todo: "{}"'.format(st))
	return 

def showList():

	if os.path.isfile('todo.txt'):
	    print ("File exist")
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    for line in data:
	    	print('[{}] {}'.format(ct,line),end='')
	    	ct-=1
	else:
	    print ("No existing data found...") #check syntax
	return

def delFromList(num):

	if os.path.isfile('todo.txt'):
	    print ("File exist")
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    if num>ct:
	    	print("Error: todo #{} does not exist. Nothing deleted.".format(num))
	    else:
	    	with open("todo.txt",'w') as todoFileMod:
	    		for line in data:
	    			if ct!=num:
	    				todoFileMod.write(line)
	    			ct-=1
	    	print("Deleted todo #{}".format(num))
	else:
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))
	return


def markDone(num):

	if os.path.isfile('todo.txt'):
	    print ("File exist")
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    if num>ct:
	    	print("Error: todo #{} does not exist.".format(num))
	    else:
	    	with open("todo.txt",'w') as todoFileMod:

	    		if os.path.isfile('done.txt'):

	    			with open("done.txt",'r') as doneFileOri:
				    	doneData=doneFileOri.read()
			    	with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			ct-=1
			    		doneFileMod.write(doneData)

		    	else:
		    		with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			ct-=1

	    	print("Marked todo #{} as done.".format(num))
	else:
	    print("Error: todo #{} does not exist.".format(num))
	return

def generateReport():

	countTodo=0
	countDone=0
	if os.path.isfile('todo.txt'):
	    print ("File exist")
	    with open("todo.txt",'r') as todoFile:
	    	todoData=todoFile.readlines()
	    countTodo=len(todoData)
	if os.path.isfile('done.txt'):
	    print ("File exist")
	    with open("done.txt",'r') as doneFile:
	    	doneData=doneFile.readlines()
	    countDone=len(doneData)
	print(datetime.today().strftime('%Y-%m-%d'),end='')
	print(" Pending : {} Completed : {}".format(countTodo,countDone))
	return

def main(): 
	if len(sys.argv)==1:
		print(todohelp,end='')
	elif sys.argv[1]=='help':
		print(todohelp,end='')
	elif sys.argv[1]=='ls':
		showList()
	elif sys.argv[1]=='add':
		addToList(sys.argv[2])
	elif sys.argv[1]=='del':
		delFromList(int(sys.argv[2]))
	elif sys.argv[1]=='done':
		markDone(int(sys.argv[2]))
	elif sys.argv[1]=='report':
		generateReport()
	else:
		print("")


if __name__=="__main__": 
    main() 

"""if sys.argv[1]=='add':
	with open('todo.txt','a') as todofile:
		todolines=todofile.readlines()
		if not todolines:
			todofile.write('[1]')
			todofile.write('')"""