# FlashCard Maker
# Joshua Lee
# Version 4
# Last Edited: 8/7/19


#               ==============IMPORT STATEMENTS=============
# import os to set the current working directory to global variable "path"
import os
# import random to randomly select words to test yourself
import random
# import regex to find words and its corresponding definition when testing yourself
import re

#               ==============GLOBAL VARIABLES===============
# path to the flashcard set directory
path = os.getcwd()
path += "/flashcards/"

# dictionary of all FlashSets
flashDict = {}
flashDict[str(0)] = "0"
number = 1

# will add all text files to the flash dictionary
# sorted in alphabetical order
# number has to be a string because user input is always a string
for fileName in sorted(os.listdir(path)):
    if fileName.endswith(".txt"):
        flashDict[str(number)] = fileName
        number += 1


# function to help update the fileDict when deleting files
def deleteFromDict(fileName):
    if fileName in flashDict.values():
        try:
            # Will find the wanted file and delete it from flashDict
            for i in flashDict:
                if flashDict[i] == fileName:
                    flashDict.pop(str(i))
                    break

            num = 1
            for filee in sorted(os.listdir(path)):
                if filee.endswith(".txt"):
                    flashDict[str(num)] = filee
                    num += 1

        except KeyError:
            print("Key not found")

# function to help update the fileDict when creating files
def addToDict(fileName):
    flashDict[str(len(flashDict))] = fileName
    number = 1
    for filee in sorted(os.listdir(path)):
        if filee.endswith(".txt"):
            flashDict[str(number)] = filee
            number += 1

    # renumber the dictionary in alphabetical order
    """
    for i in range(dictLength-1):
        for j in range(i, dictLength-1):
            if flashDict[str(i)] < flashDict[str(j)]:
                flashDict[str(i)], flashDict[str(j)] = flashDict[str(j)], flashDict[str(i)]
    """

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
          "2) Work on an existing FlashCard Set\n"
          "3) Delete an existing FlashCard Set\n"
          "4) Quit ")
    return raw_input()


# Prompt 1 Selection 1: Create a New FlashCard Set
def newSet():
    duplicate = False
    name = raw_input("What would you like to name your new FlashCard Set? (DON'T ADD '.txt') ")
    name += ".txt"
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

    # Associate each number to each set
    number = 1

    for num, fileName in flashDict.items():
        if fileName.endswith(".txt"):
            print(num + ") " + fileName)
            number += 1

    # Ask for which set to work on
    name = raw_input("\nWhich set would you like to work on? (include '.txt')\n"
                     "If none, return 0 ")
    return name


# Prompt 1 Selection 3: List the FlashCard Sets and delete one
def deleteSet():
    # Print all existing sets
    print("These are the existing Sets: ")

    # Associate each number to each set
    number = 1

    for fileName in flashDict.values():
        if fileName.endswith(".txt"):
            print(str(number) + ") " + fileName)
            number+= 1

    # Ask for which set to delete
    name = raw_input("\nWhich set would you like to delete (select name or number)\n"
                     "If none, return 0\n")
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
    openFile = open(fileName, "a")

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

    openFile.close()


# Prompt 2 Selection 3 Test yourself
def testFile(fileName):
    openFile = open(fileName, "r")
    words = re.split(":|\n", openFile.read())
    wordDict = {}

    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordDict[words[i]] = words[i + 1]


    items = wordDict.items()
    random.shuffle(items)
    print("For each word, enter what you think the definition is\n")
    print("-----------------------------------------------------\n")
    for word, definition in items:
        print("The Word is: " + word)
        randomInput = raw_input()
        print("The Definition is: " + definition + '\n')
        print("--------------------------------------\n")

    openFile.close()


#               ===============MAIN METHOD=============
if __name__ == "__main__":
    fileName = ""

    # while the user wants to continue to do things
    while (True):
        choice1 = intro()

        # P1S1: create a new set
        if (choice1 == '1'):
            fileName = newSet()
            addToDict(fileName)

        # P1S2: choose an existing set
        elif (choice1 == '2'):
            fileName = chooseSets()

            if (fileName == '0'):
                print("You chose to exit!")
                continue

            # If the input isn't a txt file, then check to see if the input is a key
            if fileName in flashDict.keys():
                fileName = flashDict[fileName]

        # P1S3: delete an existing set
        elif (choice1 == '3'):
            fileName = deleteSet()

            # If the input isn't a txt file, then check to see if the input is a key
            if fileName in flashDict.keys():
                fileName = flashDict[fileName]

            # flashDict[0] = '0' so it'll still exit
            if (fileName == '0'):
                print("You chose to exit!")

            else:
                confirm = raw_input("Are you sure?\n"
                                "1) yes\n"
                                "2) no, go back ")
                if (confirm == '1'):
                    try:
                        os.remove(path + fileName)
                        deleteFromDict(fileName)
                    except OSError:
                        print ("Inputted file is invalid!")

            continue

        # P1S4: exit the program
        elif (choice1 == '4'):
            print("Goodbye!")
            break

        # If fileName doesn't end with .txt, then don't continue


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

# specify if you want the word then get def, def then get word, multiple choice, etc.

# be able to delete words in eaech set

# when you want to delete a file, just input a number associated to it instead of having to type the name of the file (dicitonary)

# make spacings (input and print) consistent and clean