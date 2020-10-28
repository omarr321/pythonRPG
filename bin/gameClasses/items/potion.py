import os
import re
import random
from .item import Item
from .effect import Effect
from .effect import EffectStatus

class Potion(Item):
    __path = os.path.join(os.getcwd(), "items", "potions")
    __potionFile = ""
    __name = ""
    __desc = ""
    __cost = [0, 0]

    def __init__(self, potionName, playerLevel):
        playerLevel = playerLevel - 1
        self.__potionFile = str.lower(str(potionName) + ".potion")
        if not os.path.exists(os.path.join(self.__path, self.__potionFile)):
            raise Exception("Can not find " + potionName + ".potion!")

        self.__name = super().getStringValue("name", self.__path, self.__potionFile)
        self.__desc = super().getStringValue("desc", self.__path, self.__potionFile)
        super().setNumberPair(self.__cost, "cost", self.__path, self.__potionFile)
        
        (_, _, files) = next(os.walk(self.__path))

        temp = potionName + "Effect"
        regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).potion$')
        for x in files:
            if regex.match(x):
                temp = super().getStringValue("type", self.__path, x)
                ran = [0, 0]
                super().setNumberPair(ran, "range", self.__path, x)
                super().addEffect(Effect(super().getFileEffect(temp), ran))


        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

    def getCostValue(self):
        return self.__cost

    def toString(self):
        temp = "NAME: " + str(self.__name)
        temp = temp + "\t" + str(self.__desc)
        temp = temp + "COST: " + str(self.__cost) + "\n"

        return temp

        
    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        for _ in range(0,leng):
            nameN = nameN + " "
        return "TYPE: Potion   " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")