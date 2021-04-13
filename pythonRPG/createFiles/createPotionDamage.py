#!/usr/bin/env python3

import os
currWorkDir = os.path.dirname(__file__)
currWorkDir = os.path.split(currWorkDir)[0]
import re

# !!!!!-DO NOT CHANGE-!!!!!
# This is the type of item we are dealing with
OBJ_TYPE = "potion"
# This is the value that shows up in the file for the base
OBJ_BASE_VALUE = "damage"
# This is what will be printed to screen for the base
OBJ_BASE_STRING = "damage"
# This is the path that it will save the files to
OBJ_PATH = os.path.join(currWorkDir, "items", str(OBJ_TYPE) + "s")
# This tells the program to pick a value between the range and use it as the range
OBJ_SOLVED = "true"
# !!!!!-DO NOT CHANGE-!!!!!

def main():
    while(True):
        print("Welcome to POTION CREATOR PRO\n")

        print("This program help with the Potion creation process. It will do all the hard")
        print("work for you. Just answer the question and boom you are all done.\n")

        print("What Would you like to do?")
        print("1 | Create Potion")
        print("2 | Help")
        print("3 | Quit")
        print("----------------------")
        temp = getInput(3)
        if temp == 1:
            createWeapon()
        elif temp == 2:
            helpPage()
        else:
            print("Goodbye!")
            exit(0)

def createWeapon():
    Name = ""
    Desc = ""
    Cost = ""
    BaseValue = ""

    while(True):
        Name = getString("name", str(OBJ_TYPE))
        regex = re.compile('^' + Name + '.weapon$')
        (_, _, files) = next(os.walk(OBJ_PATH))
        flag = False
        for x in files:
            if regex.match(x):
                flag = True

        if flag == False:
            break
        else:
            print("Error: There is already a file with that name!")

    Desc = getString("description", str(OBJ_TYPE))

    Cost = getRange("cost", str(OBJ_TYPE))

    BaseValue = getRange(str(OBJ_BASE_STRING), str(OBJ_TYPE))

    clearScreen()
    print("name: " + str(Name))
    print("description: " + str(Desc))
    print("cost: " + str(Cost))
    print(str(OBJ_BASE_STRING) + str(BaseValue))

    pause()
    clearScreen()
    print("How many effects does the " + str(OBJ_TYPE) + " have?")
    while(True):
        print(">>>", end="")
        try:
            temp = int(input())
            if temp > 5 or temp < 0:
                print("Error: The number has to be beween 1 and 5!")
            else:
                break
        except ValueError:
            print("Error: You did not enter a number!")

    effects = []
    for _ in range(0, temp):
        effects.append(getEffect())

    clearScreen()
    print("The program will now create the " + str(OBJ_TYPE) + " now")
    pause()
    print("Creating " + str(OBJ_TYPE) + "file...", end="")

    namef = Name.replace(" ", "")
    ffile = open(os.path.join(OBJ_PATH, str(namef) + "." + str(OBJ_TYPE)), "w+")
    ffile.write("name:" + Name + "\n")
    ffile.write("desc:" + Desc + "\n")
    ffile.write("cost:" + Cost + "\n")
    ffile.close()

    ffile = open(os.path.join(OBJ_PATH, str(namef) + "Effect1." + str(OBJ_TYPE)), "w+")
    ffile.write("type:" + str(OBJ_BASE_VALUE) + "\n")
    ffile.write("range:" + str(BaseValue) + "\n")
    ffile.write("solved:" + str(OBJ_SOLVED) + "\n")
    ffile.close()

    count = 2
    for x in effects:
        ffile = open(os.path.join(OBJ_PATH, str(namef) + "Effect" + str(count) + "." + str(OBJ_TYPE)), "w+")
        ffile.write("type:" + str(x[0]) + "\n")
        ffile.write("range:" + str(x[1]) + "\n")
        ffile.write("solved:" + str(OBJ_SOLVED) + "\n")
        count = count + 1
    
    print("Done!")
    pause()


def helpPage():
    clearScreen()
    print("Error: Not Implmented")
    pause()
    clearScreen()

def getEffect():
    eType = ""
    eRange = ""
    eSolved = "false"

    print("What effect would you like to add?")
    print("1 | Heal")
    print("2 | Fire")
    print("3 | Ice")
    print("4 | Acid")
    print("5 | Light")
    print("6 | Dark")
    temp = getInput(6)

    if temp == 1:
        eType = "heal"
    elif temp == 2:
        eType = "fire"
    elif temp == 3:
        eType = "ice"
    elif temp == 4:
        eType = "acid"
    elif temp == 5:
        eType = "light"
    else:
        eType = "dark"

    eRange = getRange("value", "effect")

    print("type: " + str(eType))
    print("range: " + str(eRange))
    pause()

    return [eType, eRange, eSolved]

def pause(temp="Type anything to contine..."):
    print(str(temp))
    input()

def getRange(desc, ttype):
    while(True):
        clearScreen()
        temp_1 = ""
        print("[ - ]")
        print("What is lowest " + str(desc) + " of the " + str(ttype) + "?")
        while(True):
            while(True):
                print(">>>", end="")
                try:
                    temp_1 = int(input())
                    break
                except ValueError:
                    print("Error: You did not enter a number!")
            
            if int(temp_1) < 1:
                print("Error: Range is invaild!")
            else:
                break
            
    
        clearScreen()
        while(True):
            temp_2 = ""
            print("[" + str(temp_1) + "- ]")
            print("What is highest " + str(desc) + " of the " + str(ttype) + "?")
            while(True):
                print(">>>", end="")
                try:
                    temp_2 = int(input())
                    break
                except ValueError:
                    print("Error: You did not enter a number!")


            if int(temp_1) >= int(temp_2):
                print("Error: Range is invaild!")
            else:
                break
        clearScreen()
        print("Is this correct: ", end="")
        print("[" + str(temp_1) + "-" + str(temp_2) + "]")
        flag = False
        while(True):
            print("yes/no")
            print(">>>", end="")
            temp = input()
            temp = temp.lower()
            if temp == "yes" or temp == "y":
                flag = True
                break
            elif temp == "no" or temp == "n":
                flag = False
                break
            else:
                print ("Error: Not a vaild input!")
        if flag:
            break
    return "[" + str(temp_1) + "-" + str(temp_2) + "]"

def getString(desc, ttype):
    clearScreen()
    print("What is the " + str(desc) + " of the " + str(ttype) + "?")
    print(">>>", end="")
    return input()

def getInput(numOfoptions):
    while(True):
        print(">>>",end="")
        temp = input()

        try:
            temp = int(temp)
            if (temp < 1 or temp > numOfoptions):
                print("Error: Number out of range!")
            else:
                break
        except ValueError:
            print("Error: You did not enter a number!")
    return temp

def clearScreen():
    for _ in range(0, 50):
        print("\n\n\n\n\n")

if __name__ == "__main__":
    main()
else:
    print("Error: This file can not be imported!")