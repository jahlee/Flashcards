# FlashCard Maker
# Joshua Lee
# Version 7
# Last Edited: 8/12/19


#               ==============IMPORT STATEMENTS=============
# import os to set the current working directory to global variable "path"
import os
# import random to randomly select words to test yourself
import random
# import regex to find words and its corresponding definition when testing yourself
import re

#               ==============GLOBAL VARIABLES/SETUP===============
# path to the flashcard set directory
path = os.getcwd()
path += "/flashcards/"

# create a directory called flashcards to hold all the FlashCard Sets if not already created
if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)

# List of all FlashSets
flashList = ["0"]

# will add all text files to the Flash List
# sorted in alphabetical order
# number has to be a string because user input is always a string
for fileName in sorted(os.listdir(path)):
    if fileName.endswith(".txt"):
        flashList.append((fileName))


# function to help update Flash List when deleting files
def deleteFromList(fileName):
    global flashList
    if fileName in flashList:
        # Will find the wanted file if it exists and delete it from flashList
        try:
            flashList.remove(fileName)
            print(fileName)
            flashList = sorted(flashList)
        except ValueError:
            print("Value not found!")

# function to help update Flash List when creating files
def addToList(fileName):
    global flashList
    flashList.append(fileName)
    flashList = sorted(flashList)

# funciton to help update Flash List when updating a file
def updateList(oldFile, newFile):
    addToList(newFile)
    deleteFromList(oldFile)



#               ===============PROMPT 1================
# introduction + prompt 1
def intro():
    print("These are your current projects: ")
    for f in flashList:
        if (f.endswith(".txt")):
            print(f[:-4])

    print("--------------------------------------------------------")
    print("Would you like to:\n"
          "1) Create a New FlashCard Set\n"
          "2) Open an existing FlashCard Set\n"
          "3) Rename an existing FlashCard Set\n"
          "4) Delete an existing FlashCard Set\n"
          "5) Quit ")
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

                # Go back to first question
                elif (choice == '2'):
                    print("\n")
                    continue

    # Creates a new file
    filePtr = open(filePath, "w")
    filePtr.close()

    return name


# helper method that prints all the sets with its number/index next to it
def printSets():
    # Print all existing sets
    print("These are the existing Sets: ")

    # Associate each number to each set
    number = 1

    for fileName in flashList:
        if fileName.endswith(".txt"):
            print(str(number) + ") " + fileName[:-4])
            number += 1

# Prompt 1 Selection 2: List the FlashCard Sets and choose one
def chooseSets():
    printSets()

    # Ask for which set to work on
    name = raw_input("\nWhich set would you like to open? (input name or number)\n"
                     "If none, return 0 ")
    return name



# Prompt 1 Selection 3: Rename a FlashCard Set
def renameSet():
    printSets()

    # Ask for which set to rename
    name = raw_input("\nWhich set would you like to rename? (input name or number)\n"
                     "If none, return 0 ")

    return name


# Prompt 1 Selection 4: List the FlashCard Sets and delete one
def deleteSet():
    printSets()

    # Ask for which set to delete
    name = raw_input("\nWhich set would you like to delete (input name or number)\n"
                     "If none, return 0\n")
    return name


#           ===============PROMPT 2===============
# Prompt 2 What to do with the FlashCard Set
def setAction():
    print("\nNow what would you like to do?\n"
          "1) Read the file \n"
          "2) Add to the file\n"
          "3) Delete from the file\n"
          "4) Test yourself\n"
          "5) Quit ")
    return raw_input()


def printWords(fileName):
    openFile = open(fileName, "r")
    # Use Regular Expression to differentiate between new word and its definition
    words = re.split(":|\n", openFile.read())
    wordList = ["0"]
    wordDict = {}
    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordList.append(words[i])
            wordDict[words[i]] = words[i+1]

    wordList.sort()

    # It'll be the max chars long + 5 on each side
    # wordLength = max(len(key.split()) for key in wordDict.keys())

    #print('-' * 101)
    print ("+ {:-<6s} + {:-<25s} + {:-<75s}+".format("-","-","-"))
    print ("| {:<6s} | {:<25s} | {:<75s}|".format("INDEX", "WORD", "DEFINITION"))
    #print('-' * 101)
    print ("+ {:-<6s} + {:-<25s} + {:-<75s}+".format("-", "-", "-"))

    for index in range(1,len(wordList)):

        print("| {:<6d} | {:<25s} | {:<75s}|".format(index, wordList[index], wordDict[wordList[index]]))
        print("+ {:.<6s} + {:.<25s} + {:.<75s}+".format(".",".","."))
        #print('- ' * 51 + '-')
        #print("| {:<8s} | {:<20s} | {:<65s}|".format("","",""))
        index+=1
    #print('=' * 103)

# Prompt 2 Selection 1 Read the File
def readFile(fileName):
    printWords(fileName)


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

            # Exit if it's not 1
            else:
                break


        # Redo changes
        elif (addChanges == '2'):
            continue


        # Exit
        elif (addChanges == '3'):
            openFile.close()
            break

    openFile.close()


# Prompt 2 Selection 3 Delete from the File
def deleteFromFile(fileName):
    printWords(fileName)
    toDelete = raw_input("Which word would you like to delete? (Enter index or name)\n"
                         "Enter 0 to exit ")

    openFile = open(fileName, "r")
    # Use Regular Expression to differentiate between new word and its definition
    words = re.split(":|\n|''", openFile.read())
    openFile.close()

    wordList = ["0"]
    wordDict = {}
    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordList.append(words[i])
            wordDict[words[i]] = words[i + 1]

    wordList.sort()

    # If the input isn't a txt file, then check to see if the input is a key
    # If it is not a number, then it is not a valid input
    # If it is not a string, then something got messed up somewhere
    # flashList[0] = '0' so it'll still exit
    if (toDelete == '0'):
        print("You chose to exit!")

    elif (toDelete in wordList):
        # Gets all lines
        with open(fileName, "r") as openFile:
            lines = openFile.readlines()
        # Will write all words in "lines" if the line isn't the one to delete
        with open(fileName, "w") as openFile:
            for line in lines:
                if not line.lower().startswith(toDelete.lower()):
                    openFile.write(line)
        openFile.close()

    else:
        try:
            if toDelete in str(range(len(wordList))):
                toDelete = wordList[int(toDelete)]
                # Gets all lines
                with open(fileName, "r") as openFile:
                    lines = openFile.readlines()
                # Will write all words in "lines" if the line isn't the one to delete
                with open(fileName, "w") as openFile:
                    for line in lines:
                        if not line.lower().startswith(toDelete.lower()):
                            openFile.write(line)
                openFile.close()
            else:
                print("Input does not exist")

        except ValueError:
            print("Not a valid input!")




# Prompt 2 Selection 4 Test yourself
def testFile(fileName):
    openFile = open(fileName, "r")
    # Use Regular Expression to differentiate between new word and its definition
    words = re.split(":|\n|''", openFile.read())
    wordDict = {}

    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordDict[words[i]] = words[i + 1]


    items = wordDict.items()
    random.shuffle(items)
    print("For each word, enter what you think the definition is\n"
          "If you want to exit, enter 1")
    print("-----------------------------------------------------\n")
    for word, definition in items:
        print("The Word is: " + word)

        # Will exit if user inputs 1
        randomInput = raw_input()
        if (randomInput == '1'):
            break

        print("The Definition is: " + definition + '\n')
        print("--------------------------------------\n")

    openFile.close()


#               ===============MAIN METHOD=============
if __name__ == "__main__":
    fileName = ""
    print("Hello! Welcome to FlashCard Maker!")
    print("--------------------------------------------------------")
    # while the user wants to continue to do things
    while (True):
        choice1 = intro()

        # P1S1: create a new set
        if (choice1 == '1'):
            fileName = newSet()
            addToList(fileName)

        # P1S2: choose an existing set
        elif (choice1 == '2'):
            fileName = chooseSets()

            if (fileName == '0'):
                print("You chose to exit!")
                continue

            # If the input isn't a txt file, then check to see if the input is a key
            # If it is not a number, then it is not a valid input
            # If it is not a string, then something got messed up somewhere
            try:
                if fileName in str(range(len(flashList))):
                    fileName = flashList[int(fileName)]
                else:
                    print("Input is not valid!")
                    continue
            except ValueError:
                print("Not a valid input!")
            except TypeError:
                print("Wrong type!")



        # P1S3: rename an existing set
        elif (choice1 == '3'):
            fileName = renameSet()

            # If the input isn't a txt file, then check to see if the input is a key
            # If it is not a number, then it is not a valid input
            # If it is not a string, then something got messed up somewhere
            try:
                if fileName in str(range(len(flashList))):
                    fileName = flashList[int(fileName)]
            except ValueError:
                print("Not a valid input!")
                continue
            except TypeError:
                print("Wrong type!")
                continue

            # flashList[0] = '0' so it'll still exit
            if (fileName == '0'):
                print("You chose to exit!")

            else:
                newFileName = raw_input("What would you like to name your new file? (Don't add '.txt') ")
                newFileName += ".txt"
                confirm = raw_input("Are you sure?\n"
                                    "1) yes\n"
                                    "2) no, go back ")
                if (confirm == '1'):
                    try:
                        os.rename(path + fileName, path + newFileName)
                        updateList(fileName, newFileName)
                    except OSError:
                        print ("Inputted file is invalid!")

            # Go back to prompt 1
            continue


        # P1S4: delete an existing set
        elif (choice1 == '4'):
            fileName = deleteSet()

            # check to see if the input is a key rather than the txt file
            # If it is not a number, then it is not a valid input 
            # If it is not a string, then something got messed up somewhere
            try:
                if fileName in str(range(len(flashList))):
                    fileName = flashList[int(fileName)]
            except ValueError:
                print("Not a valid input!")
            except TypeError:
                print("Wrong type!")

            # flashList[0] = '0' so it'll still exit
            if (fileName == '0'):
                print("You chose to exit!")
                continue

            else:
                confirm = raw_input("Are you sure?\n"
                                "1) yes\n"
                                "2) no, go back ")
                if (confirm == '1'):
                    try:
                        os.remove(path + fileName)
                        deleteFromList(fileName)
                    except OSError:
                        print ("Inputted file is invalid!")

            continue

        # P1S5: exit the program
        elif (choice1 == '5'):
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

            # P2S3: delete from the file
            elif (choice2 == '3'):
                deleteFromFile(flashPath)

            # P2S4: test yourself
            elif (choice2 == '4'):
                testFile(flashPath)

            # P2S5: exit prompt 2 to go back to prompt 1
            elif (choice2 == '5'):
                print("Exiting!")
                break


# Create a method that will check to see if an added word already exists and see if you want to
# overwrite the old def with a new def, add to the new def, or create a separate def for the same word

# specify if you want the word then get def, def then get word, multiple choice, etc.

# Deleting words might have some bugs

# if you input the beginning of a file, then return all files that start with the same input
# ex: if you input h then it'll output all files that start with h

# make spacings (input and print) consistent and clean


# make variable names better

# create helper methods
# print ----- (esp after you choose exit)
# will do the try except except >> p1s2 is a little diff with the else statement
#

# should i make this all of these methods part of a class so that i can implement it in other files?
# if i do, then global variables are made in the initiazlier or just as instance varaibles or soemthing!

# make the table responsive to the input length, create multiple lines if possible

#Currently when you input the name of the file, it won't go
# it only checks for the number value
# change it so that you just need to insert the name of the project
# its better to take out .txt from print because it'd confused the user!!!

# make everything case insensitive (for prompt 1 regarding files)