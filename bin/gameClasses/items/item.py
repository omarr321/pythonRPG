import os
import random
from .effect import Effect
from .effect import EffectStatus

class Item:
    __effects = list()

    def getStringValue(self, key, path, fileName):
        f = open(os.path.join(path, fileName))
        for line in f:
            if line.startswith(key + ":"):
                temp = line.split(":")
                f.close()
                return temp[1]
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
                    return
                except ValueError:
                    raise ValueError("Value is not a number pair!")
                except IndexError:
                    raise ValueError("Value is not a number pair!")
        raise Exception("Can not find key \"" + str(key) + "\"!")

    def pairValueToStr(self, arr):
        return str(arr[0]) + "-" + str(arr[1])

    def addEffect(self, effect):
        if not isinstance(effect, Effect):
            raise Exception ("Effect is not a Effect class!")

        self.__effects.append(effect)

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

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")