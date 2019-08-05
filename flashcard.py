# FlashCard Maker
# Joshua Lee
# Version 2
# Last Edited: 8/5/19


#               ==============IMPORT STATEMENTS=============
# import os to set the current working directory to global variable "path"
import os
# import random to randomly select words to test yourself
import random
# import regex to find words and its corresponding definition when testing yourself
import re

path = os.getcwd()
path += "/flashcards/"

# create a directory called flashcards to hold all the FlashCard Sets if not already created
if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)


#               ===============PROMPT 1================
# introduction + prompt 1
def intro():
    print("\nHello! Welcome to FlashCard Maker!\n"
          "Would you like to:\n"
          "1) Create a New FlashCard Set\n"
          "2) Look at existing FlashCard Set\n"
          "3) Delete existing FlashCard Set\n"
          "4) Quit ")
    return raw_input()


# Prompt 1 Selection 1: Create a New FlashCard Set
def newSet():
    duplicate = False
    name = raw_input("What would you like to name your new FlashCard Set? (add '.txt') ")
    print ("Your new text file will be %s\n" % (name))
    filePath = path + name

    # Will check to see if the inputted file name is already created
    for fileName in os.listdir(path):
        if (name == fileName):
            duplicate = True
            break

    # If the file is already created
    if (duplicate):
        while (True):
            print("There seems to be a file already created with the name %s" % (name))
            choice = raw_input("Do you want to\n"
                               "1) Use the already created file\n"
                               "2) Overwrite the file\n")

            # Use the already created file
            if (choice == '1'):
                return name

            # Overwrite the file (by deleting the file, then creating a new file)
            elif (choice == '2'):

                # Make sure user wants to delete/overwrite the file
                choice = raw_input("Are you sure?\n"
                                   "1) Yes\n"
                                   "2) No, go back ")

                # Delete the file
                if (choice == '1'):
                    os.remove(filePath)
                    break

                # Go back
                elif (choice == '2'):
                    continue

    # Creates a new file
    filePtr = open(filePath, "w")
    filePtr.close()
    return name


# Prompt 1 Selection 2: List the FlashCard Sets and choose one
def chooseSets():
    # Print all existing sets
    print("These are the existing Sets: ")
    for fileName in os.listdir(path):
        if fileName.endswith(".txt"):
            print(fileName)

    # Ask for which set to work on
    name = raw_input("\nWhich set would you like to work on? (include '.txt')\n"
                     "If none, return 1 ")
    return name


# Prompt 1 Selection 3: Delete a FlashCard Set
def deleteSet():
    # Print all existing sets
    print("These are the existing Sets: ")
    for fileName in os.listdir(path):
        if fileName.endswith(".txt"):
            print(fileName)

    # Ask for which set to delete
    name = raw_input("\nWhich set would you like to delete (include '.txt')\n"
                     "If none, return 1\n")
    return name


#           ===============PROMPT 2===============
# Prompt 2 What to do with the FlashCard Set
def setAction():
    print("\nNow what would you like to do?\n"
          "1) Read the file \n"
          "2) Add to the file\n"
          "3) Test yourself\n"
          "4) Quit ")
    return raw_input()


# Prompt 2 Selection 1 Read the File
def readFile(fileName):
    openFile = open(fileName, "r")
    print('\n' + openFile.read())
    openFile.close()


# Prompt 2 Selection 2 Add to the File
def addToFile(fileName):
    openFile = open(fileName, "w")

    # While user wants to keep adding words, ask for word and its definition
    while (True):
        word = raw_input("What word/phrase would you like to add? ")
        definition = raw_input("What is its definition? ")

        # Confirm word and definition
        print("\nJust to confirm, your word is:\n"
              "\t%s\n"
              "and its definition is:\n"
              "\t%s\n" % (word, definition))

        # Decide to add changes, redo changes, or exit
        print("Press 1 to add these changes\n"
              "Press 2 to redo\n"
              "Press 3 to exit")

        addChanges = raw_input()

        # Add changes
        if (addChanges == '1'):
            openFile.write(word + ":" + definition + '\n')
            addAnother = raw_input("Press 1 to add another word\n"
                                   "Press 2 to exit ")

            # Add another word
            if (addAnother == '1'):
                continue

            # Exit
            elif (addAnother == '2'):
                break


        # Redo changes
        elif (addChanges == '2'):
            continue


        # Exit
        elif (addChanges == '3'):
            openFile.close()
            break


# Prompt 2 Selection 3 Test yourself
def testFile(fileName):
    openFile = open(fileName, "r")
    words = re.split(":|\n", openFile.read())
    wordDict = {}

    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordDict[words[i]] = words[i + 1]


    for i in range(len(words) / 2):
        word, definition = random.choice(list(wordDict.items()))
        print("The word is: " + word)
        randomInput = raw_input("Enter any key when you are ready to see the definition")
        print("The Definition is: " + definition + '\n')


#               ===============MAIN METHOD=============
if __name__ == "__main__":
    fileName = ""

    # while the user wants to continue to do things
    while (True):
        choice1 = intro()

        # P1S1: create a new set
        if (choice1 == '1'):
            fileName = newSet()

        # P1S2: choose an existing set
        elif (choice1 == '2'):
            fileName = chooseSets()
            if (fileName == '1'):
                print("You chose to exit!")
                continue

        # P1S3: delete an existing set
        elif (choice1 == '3'):
            fileName = deleteSet()

            if (fileName == '1'):
                print("You chose to exit!")

            else:
                try:
                    os.remove(path + fileName)
                except OSError:
                    print ("Inputted file is invalid!")

            continue

        # P1S4: exit the program
        elif (choice1 == '4'):
            print("Goodbye!")
            break

        # If user created a new set or is using an existing one, it will go to the next prompt
        # While the user is still editing or using this file, continue to run
        while (True):
            choice2 = setAction()
            flashPath = path + fileName
            # P2S1: read the file
            if (choice2 == '1'):
                readFile(flashPath)

            # P2S2: add to the file
            elif (choice2 == '2'):
                addToFile(flashPath)

            # P2S3: test yourself
            elif (choice2 == '3'):
                testFile(flashPath)

            # P2S4: exit prompt 2 to go back to prompt 1
            elif (choice2 == '4'):
                print("Exiting!")
                break

# Create a method that will check to see if an added word already exists and see if you want to
# overwrite the old def with a new def, add to the new def, or create a separate def for the same word

# Use regex to find word to definition
# Create a dictionary of the words to test yourself
# regex splits at each whitespace... would've done at each : but the each def would have the next word with it... right?
#   wait but if you do whitespace then the definition with multiple words would be cut so its bad hm
# make sure that it doesn't duplicate the same word to def,
# specify if you want the word then get def, def then get word, multiple choice, etc.
