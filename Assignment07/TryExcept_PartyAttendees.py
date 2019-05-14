#-----------------------------------------------------------------#
# Title: Error Handling
# Dev:   Jinee Han
# Date:  May 12, 2019
# ChangeLog: (Who, When, What)
# Jinee Created a RSVP list for a party
#------------------------------------------------------------------#

# Ask the user RSVP for the party
# with their name and the number of parties.


# Try: Write a text file.
try:
    objFile = open('PartyAttendees.txt', 'w+')
    print ("The Attendees are: ")
    print (objFile.read())

# User input for the attendance's name and number of parties
    while(True):
        attendeeName = str(input("Who is attending? (Please Enter to exit.)\n"))
        if len(attendeeName) > 0:
            numberInParty = int(input("How many people are you with?\n"))
            saveTheData = objFile.write("Name: "  + attendeeName + ', Number of People: ' + str(numberInParty)+"\n")
        else:
            break

# Display the saved data

    print ("Here is the data saved.")
    objFile.seek(0)
    print (objFile.read())
    objFile.close()

# Except: Display the error reason
except Exception as e:
    print ("The error has occurred: ")
    print (e)

