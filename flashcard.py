# FlashCard Maker
# JLee
# Version 8?
# Last Edited: 9/13/19


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
    print("--------------------------------------------------------")
    print("\nThese are your current existing projects: ")
    for f in flashList:
        if (f.endswith(".txt")):
            print(f[:-4])

    print("--------------------------------------------------------")
    print("\nWould you like to:\n"
          "1) Create a New FlashCard Set\n"
          "2) Open an existing FlashCard Set\n"
          "3) Rename an existing FlashCard Set\n"
          "4) Delete an existing FlashCard Set\n"
          "0) Quit")
    return raw_input("Input: ")


# Prompt 1 Selection 1: Create a New FlashCard Set
def newSet():
    duplicate = False
    print("--------------------------------------------------------")
    print("\nWhat would you like to name your new FlashCard Set?")
    name = raw_input("Input: ")
    name += ".txt"
    filePath = path + name

    # Will check to see if the inputted file name is already created
    for fileName in os.listdir(path):
        if (name.lower() == fileName.lower()):
            duplicate = True
            name = fileName
            break

    # If the file is already created
    if (duplicate):
        # delete the duplicate it will create in flashList
        deleteFromList(fileName)
        
        while (True):

            print("\nThere seems to be a file already created with the name '%s'" % (name[:-4]))
            print("Do you want to:\n"
                  "1) Use the already created file\n"
                  "2) Overwrite the file")

            choice = raw_input("Input: ")

            # Use the already created file
            if (choice == '1'):
                return name

            # Overwrite the file (by deleting the file, then creating a new file)
            elif (choice == '2'):

                # Make sure user wants to delete/overwrite the file
                print("\nAre you sure?\n"
                      "1) Yes\n"
                      "2) No, go back")
                choice = raw_input("Input: ")

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
    print("\nThese are the existing Sets: ")

    # Associate each number to each set
    number = 1

    for fileName in flashList:
        if fileName.endswith(".txt"):
            # format it nicer because double digit numbers take two character spaces
            if (number >= 10):
                print(str(number) + ") " + fileName[:-4])
            else:
                print(" " + str(number) + ") " + fileName[:-4])
            number += 1

# Prompt 1 Selection 2: List the FlashCard Sets and choose one
def chooseSets():
    printSets()

    # Ask for which set to work on
    print("\nWhich set would you like to open? (input name or number)\n"
          "If none, return 0")
    name = raw_input("Input: ")
    return name



# Prompt 1 Selection 3: Rename a FlashCard Set
def renameSet():
    printSets()

    # Ask for which set to rename
    print("\nWhich set would you like to rename? (input name or number)\n"
          "If none, return 0")
    name = raw_input("Input: ")
    return name


# Prompt 1 Selection 4: List the FlashCard Sets and delete one
def deleteSet():
    printSets()

    # Ask for which set to delete
    print("\nWhich set would you like to delete (input name or number)\n"
          "If none, return 0")
    name = raw_input("Input: ")
    return name


#           ===============PROMPT 2===============
# Prompt 2 What to do with the FlashCard Set
def setAction():
    print("--------------------------------------------------------")
    print("\nNow what would you like to do?\n"
          "1) Read the file \n"
          "2) Add to the file\n"
          "3) Delete from the file\n"
          "4) Test yourself\n"
          "0) Quit ")
    choice = raw_input("Input: ")
    print("--------------------------------------------------------")
    return choice


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
    print("\n")
    print ("+ {:-<6s} + {:-<25s} + {:-<100s}+".format("-","-","-"))
    print ("| {:<6s} | {:<25s} | {:<100s}|".format("INDEX", "WORD", "DEFINITION"))
    print ("+ {:-<6s} + {:-<25s} + {:-<100s}+".format("-", "-", "-"))

    for index in range(1,len(wordList)):
        print("| {:<6d} | {:<25s} | {:<100s}|".format(index, wordList[index], wordDict[wordList[index]]))
        print("+ {:.<6s} + {:.<25s} + {:.<100s}+".format(".",".","."))
        index+=1
    print("\n")


# Prompt 2 Selection 1 Read the File
def readFile(fileName):
    printWords(fileName)


# Prompt 2 Selection 2 Add to the File
def addToFile(fileName):
    #openFile = open(fileName, "a")

    # While user wants to keep adding words, ask for word and its definition
    while (True):
        print("\nWhat word/phrase would you like to add? ")
        word = raw_input("Input: ")
        print("\nWhat is its definition? ")
        definition = raw_input("Input: ")

        openFile = open(fileName, "r")
        # Use Regular Expression to differentiate between new word and its definition
        words = re.split(":|\n", openFile.read())
        openFile.close()
        new_def = ""
        for i in range(len(words) - 1):
            if (i % 2 == 0):
                if (words[i] == word):
                    print("\nIt seems you already have this word! The current definition is already: ")
                    print(words[i + 1])
                    print("\nDo you want to:\n"
                            "1) Use this definition\n"
                            "2) Use the new definition\n"
                            "3) Add the new definition to the current definition")
                    def_choice = raw_input("Input: ")
                    if (def_choice == '1'):
                        new_def = None
                        break
                    elif (def_choice == '2'):
                        new_def = definition
                        break
                    elif (def_choice == '3'):
                        new_def = words[i+1] + " | " + definition
                        break

        # If there is something to add            
        if (new_def != None):
            
            # if it's not a duplicated word, then just add it. Otherwise write a new definition for the word
            if (new_def == ""):
                openFile = open(fileName, "a")
                openFile.write(word + ":" + definition + "\n")
            else:

                # Gets all lines
                with open(fileName, "r") as openFile:
                    lines = openFile.readlines()
                # Will write all words in "lines" if the line isn't the one to delete
                with open(fileName, "w") as openFile:
                    for line in lines:
                        if not line.lower().startswith(word.lower()):
                            openFile.write(line)
                        else:
                            openFile.write(word + ":" + new_def + "\n")
                openFile.close()
        print("\nPress 1 to add another word\n"
              "Press 2 to exit ")
        addAnother = raw_input("Input: ")

        # Add another word
        if (addAnother == '1'):
            continue

        # Exit if it's not 1
        else:
            break

    openFile.close()


# Prompt 2 Selection 3 Delete from the File
def deleteFromFile(fileName):
    printWords(fileName)
    print("Which word would you like to delete? (Enter index or name)\n"
          "Enter 0 to exit")
    toDelete = raw_input("Input: ")

    openFile = open(fileName, "r")
    # Use Regular Expression to differentiate between new word and its definition
    words = re.split(":|\n", openFile.read())
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

    # input is the word itself
    elif (caseInsensitiveContain(toDelete, wordList) != None):
        # Gets all lines
        with open(fileName, "r") as openFile:
            lines = openFile.readlines()
        # Will write all words in "lines" if the line isn't the one to delete
        with open(fileName, "w") as openFile:
            for line in lines:
                if not line.lower().startswith(toDelete.lower()+":"):
                    openFile.write(line)
        openFile.close()

    # input is (possibly) the index of the word
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
    words = re.split(":|\n", openFile.read())
    wordDict = {}

    for i in range(len(words) - 1):
        if (i % 2 == 0):
            wordDict[words[i]] = words[i + 1]


    items = wordDict.items()
    random.shuffle(items)
    print("\nFor each word, enter what you think the definition is\n"
          "If you want to exit, enter 0\n")
    for word, definition in items:
        print("--------------------------------------------------------\n")
        print("The Word is: " + word)

        # Will exit if user inputs 0
        randomInput = raw_input("Input: ")
        if (randomInput == '0'):
            break

        print("The Definition is: " + definition + '\n')


    openFile.close()


# helper method to see if an object is in a list, case insensitive
# will return the correct case word in the list or "None" if it is not in the list
def caseInsensitiveContain(given_object, given_list):
    for current_object in given_list:
        if (given_object.lower() == current_object.lower()):
            return current_object
    return None


#               ===============MAIN METHOD=============
if __name__ == "__main__":
    fileName = ""
    print("Hello!\n" 
          "Welcome to FlashCard Maker!")
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

            # chooses to exit
            if (fileName == '0'):
                print("You chose to exit!")
                continue
            
            # input is the acutal filename
            temporary = caseInsensitiveContain((fileName + ".txt"), flashList)
            if (temporary != None):
                fileName = temporary
            else:
                # If the input isn't a file, then check to see if the input is a number
                # If it is not a number, then it is not a valid input
                # If it is not a stri ng, then something got messed up somewhere
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

            # input is the acutal filename
            temporary = caseInsensitiveContain((fileName + ".txt"), flashList)
            if (temporary != None):
                fileName = temporary
            else:
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
                print("\nWhat would you like to name your new file?")
                newFileName = raw_input("Input: ")
                newFileName += ".txt"
                print("\nAre you sure?\n"
                      "1) yes\n"
                      "2) no, go back")
                confirm = raw_input("Input: ")
                
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

            # input is the acutal filename
            temporary = caseInsensitiveContain((fileName + ".txt"), flashList)
            if (temporary != None):
                fileName = temporary
            else:
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
                print("\nAre you sure?\n"
                      "1) yes\n"
                      "2) no, go back")
                confirm = raw_input("Input: ")
                if (confirm == '1'):
                    try:
                        os.remove(path + fileName)
                        deleteFromList(fileName)
                    except OSError:
                        print ("Inputted file is invalid!")

            continue

        # P1S0: exit the program
        elif (choice1 == '0'):
            print("\nGoodbye!\n")
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

            # P2S0: exit prompt 2 to go back to prompt 1
            elif (choice2 == '0'):
                print("Exiting!")
                break



# specify if you want the word then get def, def then get word, multiple choice, etc.

# if you input the beginning of a file, then return all files that start with the same input
# ex: if you input h then it'll output all files that start with h

# make variable names better

# create helper methods
# print ----- (esp after you choose exit)
# will do the try except except >> p1s2 is a little diff with the else statement
#

# should i make this all of these methods part of a class so that i can implement it in other files?
# if i do, then global variables are made in the initiazlier or just as instance varaibles or soemthing!

# make the table responsive to the input length, create multiple lines if possible

# make everything case insensitive (for prompt 1 regarding files)

# corner case of input of nothing (enter nothing instead of an actual valye or a number )

# deleting a set only works with the name, not with the number

# make all quits or exits available and "0" 
# have a "go back" function instead of all these confirmations!!!
