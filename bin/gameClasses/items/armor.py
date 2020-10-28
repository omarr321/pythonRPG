import os
import random
from .item import Item

class Armor(Item):
    __path = os.path.join(os.getcwd(), "items", "armors")
    __armorFile = ""
    __name = ""
    __desc = ""
    __cost = [0, 0]

    def __init__(self, armorName, playerLevel):
        playerLevel = playerLevel - 1
        self.__armorFile = str.lower(str(armorName) + ".armor")
        if not os.path.exists(os.path.join(self.__path, self.__armorFile)):
            raise Exception("Can not find " + armorName + ".armor!")

        self.__name = super().getStringValue("name", self.__path, armorName)
        self.__desc = super().getStringValue("desc", self.__path, armorName)
        super().setNumberPair(self.__defense, "defense", self.__path, armorName)
        super().setNumberPair(self.__cost, "cost", self.__path, armorName)
        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)

        self.__defense[0] = int(self.__defense[0] + (self.__defense[0]/3)*(playerLevel*(playerLevel/4)))
        self.__defense[1] = int(self.__defense[1] + (self.__defense[1]/3)*(playerLevel*(playerLevel/4)))
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

    def getDefenseValue(self):
        return random.randrange(self.__defense[0], self.__defense[1] + 1)

    def getCostValue(self):
        return self.__cost

    def toString(self):
        temp = "NAME: " + str(self.__name)
        temp = temp + "\t" + str(self.__desc) + "DEFENSE: " + super().pairValueToStr(self.__defense) + "\n"
        temp = temp + "COST: " + str(self.__cost) + "\n"

        return temp
    
    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        for _ in range(0,leng):
            nameN = nameN + " "
        return "TYPE: Armor    " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")