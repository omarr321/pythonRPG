import os
import random
from .effect import Effect
from .effect import EffectStatus
from .gameDataController import GameDataController

class Item(object):
    __effects = list()
    _cost = [0, 0]
    _name = ""
    _desc = ""

    def __init__(self):
        self.__effects = list()

    # This method has been moved to the gameDataController Class. This is a
    # redirect until I make it so then items use the gameDataController class.
    def getStringValue(self, key, path, fileName):
        return GameDataController().Load().loadString(key, path, fileName)
    
    # This method has been moved to the gameDataController Class. This is a
    # redirect until I make it so then items use the gameDataController class.
    def setNumberPair(self, arr, key, path, fileName):
       return GameDataController().Load().loadNumPair(arr, key, path, fileName)

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

    def getFileEffect(self, i):
        if i == "heal":
            return EffectStatus.HEAL
        elif i == "damage":
            return EffectStatus.DAMAGE
        elif i == "defense":
            return EffectStatus.DEFENSE
        elif i == "fire":
            return EffectStatus.FIRE
        elif i == "ice":
            return EffectStatus.ICE
        elif i == "acid":
            return EffectStatus.ACID
        elif i == "light":
            return EffectStatus.LIGHT
        elif i == "dark":
            return EffectStatus.DARK
        else:
            return None

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