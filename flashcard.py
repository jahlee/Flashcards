# FlashCard Maker
# Joshua Lee
# Version 1
# Last Edited: 7/30/19

# import os to set the current working directory to global variable "path"
import os
import random

path = os.getcwd()
path += "/flashcards/"

# create a directory called flashcards to hold all the FlashCard Sets if not already created
if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)


# introduction + prompt 1
def intro():
    print("\nHello! Welcome to FlashCard Maker!\n"
          "Would you like to:\n"
          "1) Create a New FlashCard Set\n"
          "2) Work on an existing FlashCard Set\n"
          "3) Quit ")
    return raw_input()


# Prompt 1 Selection 1: Create a New FlashCard Set
def newSet():
    duplicate = False
    name = raw_input("What would you like to name your new FlashCard Set? (no need to add '.txt') ")
    name += ".txt"
    print ("Your new text file will be %s\n" % (name))

    for file in os.listdir(path):
        if (name == file):
            duplicate = True
            break

    if (duplicate):
        while (True):
            print("There seems to be a file already created with the name %s" % (name))
            choice = raw_input("Do you want to\n"
                               "1) Use the already created file\n"
                               "2) Overwrite the file\n")

            if (choice == '1'):
                break
            elif (choice == '2'):
                choice = raw_input("Are you sure?\n"
                                   "1) Yes\n"
                                   "2) No, go back ")
                if (choice == '1'):
                    file = path + name
                    os.remove(file)
                elif (choice == '2'):
                    break
                else:
                    continue

    return name



# Prompt 1 Selection 2: List the FlashCard Sets and choose one
def chooseSets():
    print("These are the existing Sets: ")
    for file in os.listdir(path):
        if file.endswith(".txt"):
            print(file)
    name = raw_input("\nWhich set would you like to work on? (include '.txt')\n"
                         "If none, press 1 ")

    return name


# Prompt 2 What to do with the FlashCard Set
def setAction(file):
    print("You are opening file %s"%(file))
    print("Now what would you like to do?\n"
          "1) Read the file\n"
          "2) Add to the file\n"
          "3) Quit ")
    return raw_input()

# Prompt 2 Selection 1 Read the File
def readFile():
    pass

# Prompt 2 Selection 2 Add to the File
def addToFile():
    pass

# main method
if __name__ == "__main__":
    stop = False
    fileName = ""
    while (not stop):
        choice1 = intro()

        if (choice1 == '1'):
            fileName = newSet()

        elif (choice1 == '2'):
            fileName = chooseSets()
            if (fileName == '1'):
                print("You chose to exit!")
                continue

        elif (choice1 == '3'):
            print("Goodbye!")
            stop = True

        while (True):
            choice2 = setAction(fileName)

            if (choice2 == '1'):
                fileName = newSet()

            elif (choice2 == '2'):
                fileName = chooseSets()
                
            elif (choice2 == '3'):
                print("Exiting!")
                break