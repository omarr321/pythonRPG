#!/usr/bin/env python3

numOfEffect = 0

def main():
    while(True):
        print("!!!!!\n!!!!!-THIS IS A WORK IN PROGESS. THIS DOES NOT DO ANYTHING YET-!!!!!\n!!!!!")
        print("Welcome to WEAPON CREATOR PRO\n")

        print("This program help with the Weapon creation process. It will do all the hard")
        print("work for you. Just answer the question and boom you are all done.\n")

        print("What Would you like to do?")
        print("1 | Create Weapon")
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
    wName = ""
    wDesc = ""
    wCost = ""

    wBaseDam = ""

    wName = getString("name", "weapon")

    #TODO: Check if weapon witht hat name exist!

    wDesc = getString("description", "weapon")

    wCost = getRange("cost", "weapon")

    wBaseDam = getRange("damage", "weapon")

    print(str(wName))
    print(str(wDesc))
    print(str(wCost))
    print(str(wBaseDam))

    print("Type anything to contine...", end="")
    input()
    clearScreen()

def helpPage():
    clearScreen()
    print("Error: Not Implmented")
    print("Type anything to contine...", end="")
    input()
    clearScreen()

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