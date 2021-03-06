from enum import Enum, unique
import random

class Effect:
    __range = [0, 0]
    __type = None
    __solved = None
    def __init__(self, effect, range, solved=False):
        if not isinstance(effect,EffectStatus):
            raise Exception("Not a vaild Effect!")
        self.__range = range
        self.__type = effect
        self.__solved = solved

    def getType(self):
        return self.__type

    def getRange(self):
        return self.__range

    def getRandom(self):
        if self.__solved:
            return self.__range
        else:
            return random.randrange(self.__range[0], self.__range[1]+1)

    @staticmethod
    def getStringEffect(i):
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

    def setRandom(self):
        self.__range = random.randrange(self.__range[0], self.__range[1]+1)
        self.__solved = True

    def toString(self):
        temp = "TYPE: " + self.__type.value + "\n"
        if self.__solved:
            temp = temp + "RANGE: " + str(self.__range) + "\n"
        else:
            temp = temp + "RANGE: [" + str(self.__range[0]) + "-" + str(self.__range[1]) + "]\n"
        return temp

    def toStringLine(self):
        temp = "TYPE: " + self.__type.value

        if self.__solved:
            temp = temp + "\tRANGE: " + str(self.__range) + "\n"
        else:
            temp = temp + "\tRANGE: [" + str(self.__range[0]) + "-" + str(self.__range[1]) + "]\n"
        return temp

    def toSave(self):
        temp = list()
        temp.append([0, "type", self.__type.value])
        if self.__solved:
            temp.append([0, "range", self.__range])
        else:
            temp.append([1, "range", self.__range])
        temp.append([0, "solved", str.lower(str(self.__solved))])

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