#!/usr/bin/env python3

import os
import shutil

name = ""
desc = ""
gen = [0, 0]
cost = [0, 0]


def getNumberInput(message):
	while True:
		try:
			temp = int(input(message))
			return temp
		except:
			print("Error: input is not a number. Try Again")

def getNumberRange(message, min, max):
	while True:
		temp = getNumberInput(message)
		if temp > max or temp < min:
			print("Error: input out of range. Try again")
		else:
			return temp

def setValue(arr, message, range):
	temp = "What is the item's min " + str(message) + " (1-" + str(range) + "): "
	arr[0] = getNumberRange(temp, 1, range)

	temp = "What is the item's max " + str(message) + " (" + str(arr[0]+1) + "-" + str(arr[0]+range) + "): "
	arr[1] = getNumberRange(temp, arr[0]+1, arr[0]+range)

def main():
    temp = ""
    while True:
        temp = input("What is the item type that you want to create (armor, potion, weapon): ")
        temp = str.lower(temp)
        if temp == "armor" or temp == "potion" or temp == "weapon":
            break
        else:
            print("Error: not a value input")

    itemType = temp
    
    name = input("What is the item's name: ")
    name = str.lower(name)
    
    desc = input("What is the item's description: ")
    
    setValue(cost, "cost", 500)

    if itemType == "armor":
        setValue(gen, "defense", 1000)
    elif itemType == "potion":
        setValue(gen, "heal", 1000)
    else:
        setValue(gen, "attaCK", 1000)

    print("Item's type: " + str(itemType))
    print("Item's name: " + str(name))
    print("Item's description: " + str(desc))
    if itemType == "armor":
        print("Item's defense: " + str(gen[0]) + "-" + str(gen[1]))
    elif itemType == "potion":
        print("Item's heal: " + str(gen[0]) + "-" + str(gen[1]))
    else:
        print("Item's attack: " + str(gen[0]) + "-" + str(gen[1]))

    
    while True:
        temp = input("Would you like to save this item (y/n): ")
        temp = str.lower(temp)
        if temp == "y" or temp == "yes":
            path = ""
            f = ""
            if itemType == "armor":
                path = os.path.join(currWorkDir, "..", "..", "items", "armors")
                print("Saving " + str(name) + ".armor...", end="")
                f = open(str(name) + ".armor", "w+")
            elif itemType == "potion":
                path = os.path.join(currWorkDir, "..", "..", "items", "potions")
                print("Saving " + str(name) + ".potion...", end="")
                f = open(str(name) + ".potion", "w+")
            else:
                path = os.path.join(currWorkDir, "..", "..", "items", "weapons")
                print("Saving " + str(name) + ".weapon...", end="")
                f = open(str(name) + ".weapon", "w+")
            
            f.write("type:" + str(itemType) + "\n")
            f.write("name:" + str(name) + "\n")
            f.write("desc:" + str(desc) + "\n")
            
            if itemType == "armor":
                f.write("defense:" + "[" + str(gen[0]) + "-" + str(gen[1]) + "]" + "\n")
                shutil.move(os.path.join(currWorkDir, name + ".armor"), path)
            elif itemType == "potion":
                f.write("heal:" + "[" + str(gen[0]) + "-" + str(gen[1]) + "]" + "\n")
                shutil.move(os.path.join(currWorkDir, name + ".potion"), path)
            else:
                f.write("attack:" + "[" + str(gen[0]) + "-" + str(gen[1]) + "]" + "\n")
                shutil.move(os.path.join(currWorkDir, name + ".weapon"), path)

            f.write("cost:" + "[" + str(cost[0]) + "-" + str(cost[1]) + "]" + "\n")
            f.close()
            
            print("Done!")
            print("Have a great day!")
            break
        elif temp == "n" or temp == "no":
            print("Have a great day!")
            break
        else:
            print("Error: Not a valid input. Try again")

if __name__ == "__main__":
	main()