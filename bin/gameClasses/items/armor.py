import os
import re
import random
from .item import Item
from .effect import Effect
from .effect import EffectStatus

class Armor(Item):
    __path = os.path.join(os.getcwd(), "items", "armors")
    __armorFile = ""
    __name = ""
    __desc = ""
    __cost = [0, 0]

    def __init__(self, armorName, playerLevel):
        playerLevel = playerLevel - 1
        self.__potionFile = str.lower(str(armorName) + ".armor")
        if not os.path.exists(os.path.join(self.__path, self.__potionFile)):
            raise Exception("Can not find " + armorName + ".armor!")

        self.__name = super().getStringValue("name", self.__path, self.__potionFile)
        self.__desc = super().getStringValue("desc", self.__path, self.__potionFile)
        super().setNumberPair(self.__cost, "cost", self.__path, self.__potionFile)
        
        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

        (_, _, files) = next(os.walk(self.__path))

        temp = armorName + "Effect"
        regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).armor$')
        for x in files:
            if regex.match(x):
                temp = super().getStringValue("type", self.__path, x)
                ran = [0, 0]
                super().setNumberPair(ran, "range", self.__path, x)
                curEffect = Effect(super().getFileEffect(temp), ran)
                if super().getStringValue("solved", self.__path, x) == "True":
                    curEffect.setRandom()
                super().addEffect(curEffect)

    def getCostValue(self):
        return self.__cost

    def toString(self):
        temp = "NAME: " + str(self.__name)
        temp = temp + "\n\t" + str(self.__desc)
        temp = temp + "COST: " + str(self.__cost) + "\n"
        for x in super().getEffects():
            if isinstance(x, Effect):
                temp = temp + x.toStringLine()

        return temp
    
    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        for _ in range(0,leng):
            nameN = nameN + " "
        return "TYPE: Armor    " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

    def toSave(self):
        temp = "type:armor\n"
        temp = temp + "name:" + self.__name + "\n"
        temp = temp + "desc:" + self.__desc + "\n"
        temp = temp + "cost:" + str(self.__cost) + "\n"

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")