import os
import random
from .effect import Effect
from .effect import EffectStatus

class Item(object):
    __effects = list()
    _cost = [0, 0]
    _name = ""
    _desc = ""

    def __init__(self):
        self.__effects = list()

    def getStringValue(self, key, path, fileName):
        f = open(os.path.join(path, fileName))
        for line in f:
            if line.startswith(key + ":"):
                temp = line.split(":")
                f.close()
                return temp[1].rstrip()
        f.close()
        raise Exception("Can not find key \"" + str(key) + "\"!")
    
    def setNumberPair(self, arr, key, path, fileName):
        f = open(os.path.join(path, fileName))
        for line in f:
            if line.startswith(key + ":"):
                temp = line.split(":")
                try:
                    temp = temp[1].split("[")
                    temp = temp[1].split("]")
                    temp = temp[0].split("-")
                    arr[0] = int(temp[0])
                    arr[1] = int(temp[1])
                    f.close()
                    return
                except ValueError:
                    f.close()
                    raise ValueError("Value is not a number pair!")
                except IndexError:
                    f.close()
                    raise ValueError("Value is not a number pair!")
        f.close()
        raise Exception("Can not find key \"" + str(key) + "\"!")

    def pairValueToStr(self, arr):
        return str(arr[0]) + "-" + str(arr[1])

    def addEffect(self, effect):
        if not isinstance(effect, Effect):
            raise Exception ("Effect is not a Effect class!")

        self.__effects.append(effect)

    def getName(self):
        return self._name

    def getEffects(self):
        return self.__effects

    # This method has been moved to the effect Class.
    def getFileEffect(self, i):
        return Effect.getStringEffect(i)

    def getCostValue(self):
        return self._cost

    def halfCostValue(self):
        self._cost = int(self._cost / 2)
        if self._cost == 0:
            self._cost += 1

    def doubleCostValue(self):
        self._cost = self._cost * 2

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")