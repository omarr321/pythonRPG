import os
import re
import random
from .item import Item
from .effect import Effect
from .effect import EffectStatus
from ...common import currWorkDir

class Armor(Item):
    __path = os.path.join(currWorkDir, "items", "armors")
    __armorFile = ""
    _cost = [0, 0]
    _name = ""
    _desc = ""

    def __init__(self, armorName="", playerLevel=1, load=False, name=None, desc=None, cost=None, effects=None):
        Item.__init__(self)
        if load:
            self._name = name
            self._desc = desc
            self._cost = cost
            for x in effects:
                super().addEffect(x)
        else:
            playerLevel = playerLevel - 1
            self.__armorFile = str.lower(str(armorName) + ".armor")
            if not os.path.exists(os.path.join(self.__path, self.__armorFile)):
                raise Exception("Can not find " + armorName + ".armor!")

            self._name = super().getStringValue("name", self.__path, self.__armorFile)
            self._desc = super().getStringValue("desc", self.__path, self.__armorFile)
            super().setNumberPair(self._cost, "cost", self.__path, self.__armorFile)

            self._cost = random.randrange(self._cost[0], self._cost[1] + 1)
            self._cost = int(self._cost + (self._cost/2)*(playerLevel*(playerLevel/3)))

            (_, _, files) = next(os.walk(self.__path))

            temp = str(armorName) + "Effect"
            regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).armor$')
            for x in files:
                if regex.match(x):
                    temp = super().getStringValue("type", self.__path, x)
                    ran = [0, 0]
                    super().setNumberPair(ran, "range", self.__path, x)
                    ran[0] = int(ran[0] + (ran[0]/2)*(playerLevel*(playerLevel/3)))
                    ran[1] = int(ran[1] + (ran[1]/2)*(playerLevel*(playerLevel/3)))
                    curEffect = Effect(self.getFileEffect(temp), ran)
                    if super().getStringValue("solved", self.__path, x) == "true":
                        curEffect.setRandom()
                    self.addEffect(curEffect)

    def load( name, desc, cost, effects):
        self._name = name
        self._desc = desc
        self._cost = cost
        self.__effects = effects

    def toString(self):
        temp = "NAME: " + str(self._name) + "\tCOST: " + str(self._cost) + "\n"
        temp = temp + "\t" + str(self._desc)
        temp = temp + "\nEFFECTS:\n"
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
        return "TYPE: Armor    " + " NAME: " + str(nameN) + " COST: " + str(self._cost)

    def toSave(self):
        temp = list()
        temp.append([0, "cost", self._cost])
        temp.append([0, "name", self._name])
        temp.append([0, "desc", self._desc])
        temp.append([2, "effects", super().getEffects()])

        return temp

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")