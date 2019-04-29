# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Jinee Han
# Date:  April 29, 2019
# Create a editable To Do list for a user
# -------------------------------------------------#

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

objFileName = "Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"
objFile = open("ToDo.txt", "r")

lstTable = []

for line in objFile:
    strippedText = line.strip('\n')
    text = strippedText.split(',')
    dicRow = {"Task":text[0], "Priority": text[1]}
    lstTable.append(dicRow)

# Step 2 - Display a menu of choices to the user
while (True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Get the new item to add to the table
        strTask = str(input("Please enter a task: "))
        strPriority = str(input("Please enter a priority: "))

        # Add the new item to the list
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        indexToRemove = input("Enter the number of the task to remove - ")
        lstItem = lstTable[int(indexToRemove)]
        del lstTable[int(indexToRemove)]
        print("You are removing the following:\n\r", lstItem)
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objF = open("ToDo.txt", 'w')

        for row in lstTable:
            tempDic = dict(row)
            textToWrite = tempDic["Task"] + "," + tempDic["Priority"] + "\n"
            objF.write(textToWrite)

        objF.close()
        print("The following was saved to a file:\n\r", lstTable)
    elif (strChoice == '5'):
        break  # and Exit the program

