import os
import re
import random
from .item import Item
from .effect import Effect
from .effect import EffectStatus

class Weapon(Item):
    __path = os.path.join(os.getcwd(), "items", "weapons")
    __weaponFile = ""
    __name = ""
    __desc = ""
    __cost = [0, 0]

    def __init__(self, weaponName, playerLevel):
        Item.__init__(self)
        playerLevel = playerLevel - 1
        self.__weaponFile = str.lower(str(weaponName) + ".weapon")
        if not os.path.exists(os.path.join(self.__path, self.__weaponFile)):
            raise Exception("Can not find " + weaponName + ".weapon!")

        self.__name = super().getStringValue("name", self.__path, self.__weaponFile)
        self.__desc = super().getStringValue("desc", self.__path, self.__weaponFile)
        super().setNumberPair(self.__cost, "cost", self.__path, self.__weaponFile)
        
        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

        (_, _, files) = next(os.walk(self.__path))

        temp = str.lower(weaponName) + "Effect"
        regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).weapon$')

        effectList = list()
        for x in files:
            if regex.match(x):
                #print("found effect: " + x)
                effectList.append(x)

        for x in effectList:
            #print("adding effect: " + x)    
            temp = super().getStringValue("type", self.__path, x)
            ran = [0, 0]
            super().setNumberPair(ran, "range", self.__path, x)
            curEffect = Effect(self.getFileEffect(temp), ran)
            if super().getStringValue("solved", self.__path, x) == "True":
                curEffect.setRandom()
            self.addEffect(curEffect)


    def getCostValue(self):
        return self.__cost

    def halfCostValue(self):
        self.__cost = int(self.__cost / 2)
        if self.__cost == 0:
            self.__cost += 1

    def doubleCostValue(self):
        self.__cost = self.__cost * 2

    def toString(self):
        temp = "NAME: " + str(self.__name) + "\tCOST: " + str(self.__cost) + "\n"
        temp = temp + "\t" + str(self.__desc) + "\nEFFECTS:\n"
        effectList = self.getEffects()
        if len(effectList) == 0:
            temp = temp + "\tNONE\n"
        else:
            for x in effectList:
                if isinstance(x, Effect):
                    temp = temp + "\t" + x.toStringLine()

        return temp

    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        if leng < 0:
            nameN = nameN[:13] + "..."
        else:
            for _ in range(0,leng):
                nameN = nameN + " "
        return "TYPE: Weapon   " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")