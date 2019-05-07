
#-------------------------------------------------#
# Title: To Do list
# Dev:   Jinee Han
# Date:  May 06, 2019
# Jinee edits Assignment 05 to use Class and Dictionary
#
#------------------------------------------------------#

objFileName = "Todo.txt"
strData = ""
dicRow = {}
lstTable = []

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)
class TodoList:
    @staticmethod
    def DisplayOptionsMenu():
        # Display the menu option.
        print ("""
         Menu of Options
        1) Display the current list
        2) Add a new task.
        3) Remove an existing task.
        4) Save Data to a file.
        5) Exit
        """)

    @staticmethod
    def InputChoice():
        # Ask user a question about their choice.
        strChoice = (str(input("What is your choice? (1-5) ")))
        return strChoice

    @staticmethod
    def SeeDataInTable(currentTable):
        # Display a list of existing tasks.
        print ("The current To-Do tasks are: ")
        for row in currentTable:
            print (row["Task"] + ", " + row["Priority"])

    @staticmethod
    def AddTask():
        # Ask the user about new task information to add on the list.
        strTask = str(input("What is the new task? ")).strip()
        strPriority = str(input("What is the priority? ")).strip()
        return strTask, strPriority

    @staticmethod
    def RemoveData():
        # Ask the user about the task they want to remove
        return str(input("Which one would you like to remove? "))

    @staticmethod
    def SaveDataToFile():
        # Ask the user if they want to save the data to file
        return str(input("Would you like to save the data into a file? (y/n) ")).strip().lower()

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python List and Dictionary.

class DataProvider:
    @staticmethod
    def GetToDoListFromFile(lstTable):
        # bring the text file
        objFile = open("ToDo.txt","r")
        for line in objFile:
            strData = line.split(",")
            dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()

    @staticmethod
    def InsertTask(task, priority, lstTable):
        # add the new task into the existing list
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)

    @staticmethod
    def RemoveItemFromTable(indexToRemove, lstTable):
        # Remove the task by the order number
        lstItem = lstTable[int(indexToRemove)]
        del lstTable[int(indexToRemove)]
        print("You are removing the following:\n\r", lstItem)

    @staticmethod
    def SaveTableToFile(lstTable):
        # write the task into the existing test file
        objF = open("ToDo.txt", 'w')

        for row in lstTable:
            tempDic = dict(row)
            textToWrite = tempDic["Task"] + "," + tempDic["Priority"] + "\n"
            objF.write(textToWrite)

        objF.close()
        print("The following was saved to a file:\n\r", lstTable)

# Step 2
# Display a menu of choices to the user
DataProvider.GetToDoListFromFile(lstTable)
while(True):
    # Display all todo items to user
    TodoList.DisplayOptionsMenu()
    strChoice = TodoList.InputChoice().strip()

    if (strChoice == '1'):
        # Display current table to user
        TodoList.SeeDataInTable(lstTable)
    elif (strChoice == '2'):
        # Add a new item to the list/Table
        strTask, strPriority = TodoList.AddTask()
        DataProvider.InsertTask(strTask, strPriority, lstTable)
    elif (strChoice == '3'):
        # Remove a new item to the list/Table
        indexToRemove = TodoList.RemoveData()
        DataProvider.RemoveItemFromTable(indexToRemove, lstTable)
    elif (strChoice == '4'):
        # Save tasks to the ToDo.txt file
        userChoice = TodoList.SaveDataToFile()
        if (userChoice == 'y'):
            DataProvider.SaveTableToFile(lstTable)
        else:
            print ("You chose not to save th file.")
    elif (strChoice == '5'):
        # Exit program
        break
