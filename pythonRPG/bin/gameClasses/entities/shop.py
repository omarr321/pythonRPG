import os
import random
import re
import pickle
from ..items import Armor
from ..items import Weapon
from ..items import Potion
from ..other import Inv
from ...common import currWorkDir

class Shop:
    __path = os.path.join(currWorkDir, "items")
    __inv = None
    __name = ""

    def __init__(self, itemCount=1, playerLevel=1, load=False, name=None, inv=None):
        if load:
            self.__name = name
            self.__inv = inv
            self.__inv.sort()
        else:
            self.__inv = Inv()
            if itemCount < 1:
                raise Exception("itemCount must be greater then 0")

            armorList = list()
            path = os.path.join(self.__path, "armors")
            (__, __, files) = next(os.walk(path))
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.armor)$')
            for x in files:
                if not x == "default.armor":
                    if not regex.search(x):
                        armorList.append(x)
            if len(files) == 0:
                raise Exception("There are no armor files to choose from!")

            weaponList = list()
            path = os.path.join(self.__path, "weapons")
            (__, __, files) = next(os.walk(path))
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.weapon)$')
            for x in files:
                if not x == "default.weapon":
                    if not regex.search(x):
                        weaponList.append(x)
            if len(files) == 0:
                raise Exception("There are no weapon files to choose from!")

            potionList = list()
            path = os.path.join(self.__path, "potions")
            (__, __, files) = next(os.walk(path))
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.potion)$')
            for x in files:
                if not x == "default.potion":
                    if not regex.search(x):
                        potionList.append(x)
            if len(files) == 0:
                raise Exception("There are no potion files to choose from!")

            for _ in range(0, itemCount):
                rand = random.randrange(1,4)
                if rand == 1:
                    rand = random.randrange(0, len(armorList))
                    temp = armorList[rand].split(".")[0]
                    temp = Armor(temp, playerLevel)
                    self.__inv.addItem(temp)

                elif rand == 2:
                    rand = random.randrange(0, len(weaponList))
                    temp = weaponList[rand].split(".")[0]
                    temp = Weapon(temp, playerLevel)
                    self.__inv.addItem(temp)
                else:
                    rand = random.randrange(0, len(potionList))
                    temp = potionList[rand].split(".")[0]
                    temp = Potion(temp, playerLevel)
                    self.__inv.addItem(temp)

                path = os.path.join(currWorkDir, "bin", "lists")

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

    def getCost(self, index):
        temp = self.__inv.getItem(index)
        if isinstance(temp, Weapon):
            return temp.getCostValue()
        elif isinstance(temp, Armor):
            return temp.getCostValue()
        elif isinstance(temp, Potion):
            return temp.getCostValue()

    def getLenght(self):
        return self.__inv.getLen()

    def toString(self):
        temp = "Welcome to " + self.__name + "\n----------------------------------------------------\n"
        if self.__inv.toString(numbered=True) == "Your inventory is empty!\n":
            temp = temp + "There are no items to display!\n"
        else:
            temp = temp + self.__inv.toString(numbered=True)
        return temp

    def getItem(self, id):
        return self.__inv.getItem(id)

    def sellItem(self, item):
        self.__inv.addItem(item)

    def getName(self):
        return self.__name
    
    def getInv(self):
        return self.__inv

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")