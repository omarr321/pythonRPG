from enum import Enum, unique
import random

class Effect:
    __range = [0, 0]
    __type = None
    __solved = False
    def __init__(self, effect, range):
        if not isinstance(effect,EffectStatus):
            raise Exception("Not a vaild Effect!")
        self.__range = range
        self.__type = effect

    def getType(self):
        return self.__type

    def getRange(self):
        return self.__range

    def getRandom(self):
        if self.__solved:
            return self.__range
        else:
            return random.randrange(self.__range[0], self.__range[1]+1)

    def setRandom(self):
        self.__range = random.randrange(self.__range[0], self.__range[1]+1)
        self.__solved = True

    def toSave(self):
        temp = "range:[" + str(self.__range[0]) + "-" + str(self.__range[1]) + "]\n"
        temp = temp + "type:" + str(self.__type.value)
        return temp

    def toString(self):
        temp = "TYPE: " + self.__type.value + "\n"
        temp = "RANGE: [" + self.__range[0] + "-" + self.__range[1] + "]\n"
        return temp

    def toStringLine(self):
        temp = "TYPE: " + self.__type.value
        temp = "\tRANGE: [" + self.__range[0] + "-" + self.__range[1] + "]\n"
        return temp




@unique
class EffectStatus(Enum):
    HEAL = "heal"
    DAMAGE = "damage"
    DEFENSE = "defense"
    FIRE = "fire"
    ICE = "ice"
    ACID = "acid"
    LIGHT = "light"
    DARK = "dark"

if __name__ == "__main__":
    raise Exception ("Class can not be run as main. Must be imported!")