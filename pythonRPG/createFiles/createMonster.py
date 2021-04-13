#!/usr/bin/env python3

import os
currWorkDir = os.path.dirname(__file__)
currWorkDir = os.path.split(currWorkDir)[0]
import re

# !!!!!-DO NOT CHANGE-!!!!!
# This is the type of item we are dealing with
OBJ_TYPE = "monster"
# This is the path that it will save the files to
OBJ_PATH = os.path.join(currWorkDir, str(OBJ_TYPE) + "s")
# !!!!!-DO NOT CHANGE-!!!!!

def main():
    while(True):
        print("Welcome to MONSTER CREATOR PRO\n")

        print("This program help with the Monster creation process. It will do all the hard")
        print("work for you. Just answer the question and boom you are all done.\n")

        print("What Would you like to do?")
        print("1 | Create Monster")
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
    Ttype = ""
    Desc = ""
    Health = ""
    Attack = ""
    Defense = ""
    XP = ""
    Reward = ""

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

    Ttype = getEffect()[0]

    Desc = getString("description", str(OBJ_TYPE))

    Health = getRange("health", str(OBJ_TYPE))

    Attack = getRange("attack", str(OBJ_TYPE))

    Defense = getRange("defense", str(OBJ_TYPE))

    XP = getRange("xp", str(OBJ_TYPE))

    Reward = getRange("reward", str(OBJ_TYPE))
    
    clearScreen()
    print("name: " + str(Name))
    print("type: " + str(Ttype))
    print("description: " + str(Desc))
    print("health: " + str(Health))
    print("attack: " + str(Attack))
    print("defense: " + str(Defense))
    print("xp: " + str(XP))
    print("reward: " + str(Reward))
    pause()

    clearScreen()
    print("The program will now create the " + str(OBJ_TYPE) + " now")
    pause()
    print("Creating " + str(OBJ_TYPE) + "file...", end="")

    namef = Name.replace(" ", "")
    ffile = open(os.path.join(OBJ_PATH, str(namef) + "." + str(OBJ_TYPE)), "w+")
    ffile.write("name:" + str(Name) + "\n")
    ffile.write("type:" + str(Ttype) + "\n")
    ffile.write("desc:" + str(Desc) + "\n")
    ffile.write("health:" + str(Health) + "\n")
    ffile.write("attack:" + str(Attack) + "\n")
    ffile.write("defense:" + str(Defense) + "\n")
    ffile.write("xp:" + str(XP) + "\n")
    ffile.write("reward:" + str(Reward) + "\n")
    ffile.close()
    
    print("Done!")
    pause()


def helpPage():
    clearScreen()
    print("Error: Not Implmented")
    pause()
    clearScreen()

def getEffect():
    eType = ""
    
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

    return [eType]

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