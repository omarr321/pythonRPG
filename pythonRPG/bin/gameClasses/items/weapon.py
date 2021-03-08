import os
import re
import random
from .item import Item
from .effect import Effect
from .effect import EffectStatus
from ...common import currWorkDir

class Weapon(Item):
    __path = os.path.join(currWorkDir, "items", "weapons")
    __weaponFile = ""
    _cost = [0, 0]
    _name = ""
    _desc = ""

    def __init__(self, weaponName, playerLevel):
        Item.__init__(self)
        playerLevel = playerLevel - 1
        self.__weaponFile = str.lower(str(weaponName) + ".weapon")
        if not os.path.exists(os.path.join(self.__path, self.__weaponFile)):
            raise Exception("Can not find " + weaponName + ".weapon!")

        self._name = super().getStringValue("name", self.__path, self.__weaponFile)
        self._desc = super().getStringValue("desc", self.__path, self.__weaponFile)
        super().setNumberPair(self._cost, "cost", self.__path, self.__weaponFile)
        
        self._cost = random.randrange(self._cost[0], self._cost[1] + 1)
        self._cost = int(self._cost + (self._cost/2)*(playerLevel*(playerLevel/3)))

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
            ran[0] = int(ran[0] + (ran[0]/2)*(playerLevel*(playerLevel/3)))
            ran[1] = int(ran[1] + (ran[1]/2)*(playerLevel*(playerLevel/3)))
            curEffect = Effect(self.getFileEffect(temp), ran)
            if super().getStringValue("solved", self.__path, x) == "true":
                curEffect.setRandom()
            self.addEffect(curEffect)

    def toString(self):
        temp = "NAME: " + str(self._name) + "\tCOST: " + str(self._cost) + "\n"
        temp = temp + "\t" + str(self._desc) + "\nEFFECTS:\n"
        effectList = self.getEffects()
        if len(effectList) == 0:
            temp = temp + "\tNONE\n"
        else:
            for x in effectList:
                if isinstance(x, Effect):
                    temp = temp + "\t" + x.toStringLine()

        return temp

    def toStringLine(self):
        nameN = self._name.split("\n")[0]
        leng = 16 - len(self._name)
        if leng < 0:
            nameN = nameN[:13] + "..."
        else:
            for _ in range(0,leng):
                nameN = nameN + " "
        return "TYPE: Weapon   " + " NAME: " + str(nameN) + " COST: " + str(self._cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")