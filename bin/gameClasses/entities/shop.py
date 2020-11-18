import os
import random
import re
from ..items import Armor
from ..items import Weapon
from ..items import Potion
from ..other import Inv

class Shop:
    __path = os.path.join(os.getcwd(), "items")
    __inv = Inv()
    __name = ""

    def __init__(self, itemCount, playerLevel):
        if itemCount < 1:
            raise Exception("itemCount must be greater then 0")

        for _ in range(0, itemCount):
            rand = random.randrange(1,4)
            if rand == 1:
                path = os.path.join(self.__path, "armors")
                (__, __, files) = next(os.walk(path))
                for x in files:
                    if x == "default.armor":
                        files.remove(x)
                    else:
                        regex = re.compile('Effect[1-9]{1}([0-9]{0,}.armor)$')
                        if regex.search(x):
                            files.remove(x)
                if len(files) == 0:
                    raise Exception("There are no armor files to choose from!")
                rand = random.randrange(0, len(files))
                files = files[rand]
                files = files.split(".")[0]
                files = Armor(files, playerLevel)
                self.__inv.addItem(files)

            elif rand == 2:
                path = os.path.join(self.__path, "weapons")
                (__, __, files) = next(os.walk(path))
                for x in files:
                    if x == "default.weapon":
                        files.remove(x)
                    else:
                        regex = re.compile('Effect[1-9]{1}([0-9]{0,}.weapon)$')
                        if regex.search(x):
                            files.remove(x)
                    
                if len(files) == 0:
                    raise Exception("There are no weapon files to choose from!")
                rand = random.randrange(0, len(files))
                files = files[rand]
                files = files.split(".")[0]
                files = Weapon(files, playerLevel)
                self.__inv.addItem(files)
            else:
                path = os.path.join(self.__path, "potions")
                (__, __, files) = next(os.walk(path))
                for x in files:
                    if x == "default.potion":
                        files.remove(x)
                    else:
                        regex = re.compile('Effect[1-9]{1}([0-9]{0,}.potion)$')
                        if regex.search(x):
                            files.remove(x)
                    
                if len(files) == 0:
                    raise Exception("There are no potion files to choose from!")
                rand = random.randrange(0, len(files))
                files = files[rand]
                files = files.split(".")[0]
                files = Potion(files, playerLevel)
                self.__inv.addItem(files)

            path = os.path.join(os.getcwd(), "bin", "lists")

        name = str(self.__getRandomLine(path, "npcNames.txt")).split(",")[0] + " " + str(self.__getRandomLine(path, "npcNames.txt")).split(",")[0]
        shopDesc = str(self.__getRandomLine(path, "descriptors.txt")).split(",")[0]
        adj = str(self.__getRandomLine(path, "adjetives.txt")).split(",")[0]
        heroSyn = str(self.__getRandomLine(path, "heroSynonums.txt")).split(",")[0]
        shopSyn = str(self.__getRandomLine(path, "shopSynonums.txt")).split(",")[0]

        self.__inv.sort()
        self.__name = name + " " + shopDesc + " " + shopSyn + " for " + adj + " " + heroSyn

    def __getRandomLine(self, dir, file):
        f = open(os.path.join(dir, file))
        x = 0
        fileSize = sum(1 for line in f)
        f = open(os.path.join(dir, file))
        lineNumber = random.randrange(0, fileSize)
        for line in f:
            if x == lineNumber:
                return line
            x = x + 1
        return "Nothing"

    def buyItem(self, index):
        return self.__inv.removeItem(index)

    def toString(self):
        temp = "Welcome to " + self.__name + "\n----------------------------------------------------\n"
        temp = temp + self.__inv.toString(numbered=True)
        return temp

    def getInfo(self, id):
        return self.__inv.getItem(id)[0].toString()

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")