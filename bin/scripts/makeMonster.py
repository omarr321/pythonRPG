#!/usr/bin/env python3

import os
import shutil

mType = ""
sType = ""
desc = ""
hp = [0, 0]
att = [0, 0]
deff = [0, 0]
xp = [0, 0]
money = [0, 0]

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
	temp = "What is the monster's min " + str(message) + " (1-" + str(range) + "): "
	arr[0] = getNumberRange(temp, 1, range)

	temp = "What is the monster's max " + str(message) + " (" + str(arr[0]+1) + "-" + str(arr[0]+range) + "): "
	arr[1] = getNumberRange(temp, arr[0]+1, arr[0]+range)

def main():
	mType = input("What is the monster's type: ")
	mType = str.lower(mType)

	sType = input("What is the monster's sub-type: ")
	sType = str.lower(sType)

	desc = input("What is the monster's description: ")

	setValue(hp, "health", 100)

	setValue(att, "attack", 150)

	setValue(deff, "defense", 150)

	setValue(xp, "xp", 500)

	setValue(money, "reward", 500)

	print("Monster's type: " + str(mType))
	print("Monster's sub-type: " + str(sType))
	print("Monster's description: " + str(desc))
	print("Monster's health: " + str(hp[0]) + "-" + str(hp[1]))
	print("Monster's attack: " + str(att[0]) + "-" + str(att[1]))
	print("Monster's defense: " + str(deff[0]) + "-" + str(deff[1]))
	print("Monster's xp: " + str(xp[0]) + "-" + str(xp[1]))
	print("Monster's reward: " + str(money[0]) + "-" + str(money[1]), end="\n\n")

	while True:
		temp = input("Would you like to save this monster (y/n): ")
		temp = str.lower(temp)
		if temp == "y" or temp == "yes":
			path = os.path.join(os.getcwd(), "..", "..", "monsters")
			print("Saving " + str(mType) + ".monster...", end="")
			f = open(str(mType) + ".monster", "w+")
			f.write("type:" + str(mType) + "\n")
			f.write("subType:" + str(sType) + "\n")
			f.write("desc:" + str(desc) + "\n")
			f.write("health:" + "[" + str(hp[0]) + "-" + str(hp[1]) + "]" + "\n")
			f.write("attack:" + "[" + str(att[0]) + "-" + str(att[1]) + "]" + "\n")
			f.write("defense:" + "[" + str(deff[0]) + "-" + str(deff[1]) + "]" + "\n")
			f.write("xp:" + "[" + str(xp[0]) + "-" + str(xp[1]) + "]" + "\n")
			f.write("reward:" + "[" + str(money[0]) + "-" + str(money[0]) + "]" + "\n")
			f.close()
			shutil.move(os.path.join(os.getcwd(), mType+".monster"), path)
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