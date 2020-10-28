import os
import random
from .item import Item

class Weapon(Item):
    __path = os.path.join(os.getcwd(), "items", "weapons")
    __weaponFile = ""
    __name = ""
    __desc = ""
    __cost = [0, 0]

    def __init__(self, weaponName, playerLevel):
        playerLevel = playerLevel - 1
        self.__weaponFile = str.lower(str(weaponName) + ".weapon")
        if not os.path.exists(os.path.join(self.__path, self.__weaponFile)):
            raise Exception("Can not find " + weaponName + ".weapon!")

        self.__name = super().getStringValue("name", self.__path, weaponName)
        self.__desc = super().getStringValue("desc", self.__path, weaponName)
        super().setNumberPair(self.__damage, "attack", self.__path,weaponName)
        super().setNumberPair(self.__cost, "cost", self.__path, weaponName)

        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)

        self.__damage[0] = int(self.__damage[0] + (self.__damage[0]/3)*(playerLevel*(playerLevel/4)))
        self.__damage[1] = int(self.__damage[1] + (self.__damage[1]/3)*(playerLevel*(playerLevel/4)))
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

    def getDamageValue(self):
        return random.randrange(self.__damage[0], self.__damage[1] + 1)

    def getCostValue(self):
        return self.__cost

    def toString(self):
        temp = "NAME: " + str(self.__name)
        temp = temp + "\t" + str(self.__desc) + "DAMAGE: " + super().pairValueToStr(self.__damage) + "\n"
        temp = temp + "COST: " + str(self.__cost) + "\n"

        return temp

        
    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        for _ in range(0,leng):
            nameN = nameN + " "
        return "TYPE: Weapon   " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")