#-----------------------------------------------------------------#
# Title: Pickle and Unpickle
# Dev:   Jinee Han
# Date:  May 12, 2019
# ChangeLog: (Who, When, What)
# Jinee pickles a party menu.
#------------------------------------------------------------------#


# Pickling Test
import pickle

print ("Test the pickling.")

# Create a list for the menu.
appetizer = ["cheese board","crostini","beef sliders"]
mainMenu = ["chicken breast","roasted butternut squash"]
sideDish = ["spring salad", "roasted potatoes"]

file = open("partymenu.dat","wb")

# Pickle the menu

pickle.dump(appetizer, file)
pickle.dump(mainMenu, file)
pickle.dump(sideDish, file)

file.close

# Read the pickled menu (Unpickle)

print ("What is the menu for the party?")
file = open("partymenu.dat", "rb")
appetizer = pickle.load(file)
mainMenu = pickle.load(file)
sideDish = pickle.load(file)

print (appetizer)
print (mainMenu)
print (sideDish)

file.close