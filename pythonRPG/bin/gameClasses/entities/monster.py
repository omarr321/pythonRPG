import os
import random
from ..items import EffectStatus
from ..items import Effect
from ...common import currWorkDir

class Monster:
    __path = os.path.join(currWorkDir, "monsters")
    __monsterFile = ""
    __name = ""
    __type = None
    __desc = ""
    __hp = [0, 0]
    __att = [0, 0]
    __deff = [0, 0]
    __xp = [0, 0]
    __reward = [0, 0]

    def __init__(self, monsterType, playerLevel):
        playerLevel = playerLevel - 1
        self.__monsterFile = str.lower(str(monsterType) + ".monster")
        if not os.path.exists(os.path.join(self.__path, self.__monsterFile)):
            raise Exception("Can not find " + monsterType + ".monster!")

        self.__name = self.__getStringValue("name")
        self.__type = Effect(self.__getFileEffect(self.__getStringValue("type")), [0,0])
        self.__desc = self.__getStringValue("desc")
        self.__setNumberPair(self.__hp, "health")
        self.__setNumberPair(self.__att, "attack")
        self.__setNumberPair(self.__deff, "defense")
        self.__setNumberPair(self.__xp, "xp")
        self.__setNumberPair(self.__reward, "reward")
        
        self.__hp = random.randrange(self.__hp[0], self.__hp[1] + 1)
        self.__xp = random.randrange(self.__xp[0], self.__xp[1] + 1)
        self.__reward = random.randrange(self.__reward[0], self.__reward[1] + 1)

        self.__hp = int(self.__hp + (self.__hp/3)*(playerLevel*(playerLevel/4)))
        self.__att[0] = int(self.__att[0] + (self.__att[0]/3)*(playerLevel*(playerLevel/4)))
        self.__deff[0] = int(self.__deff[0] + (self.__deff[0]/2)*(playerLevel*(playerLevel/3)))
        self.__att[1] = int(self.__att[1] + (self.__att[1]/3)*(playerLevel*(playerLevel/4)))
        self.__deff[1] = int(self.__deff[1] + (self.__deff[1]/2)*(playerLevel*(playerLevel/3)))
        self.__xp = int(self.__xp + (self.__xp/3)*(playerLevel*(playerLevel/4)))
        self.__reward = int(self.__reward + (self.__reward/2)*(playerLevel*(playerLevel/3)))

    def __getStringValue(self, key):
        f = open(os.path.join(self.__path, self.__monsterFile))
        for line in f:
            if line.startswith(key + ":"):
                temp = line.split(":")
                f.close()
                return temp[1].rstrip()
        f.close()
        raise Exception("Can not find key \"" + str(key) + "\"!")

    def getType(self):
        return self.__type

    def __getFileEffect(self, i):
        if i == "fire":
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

    def __setNumberPair(self, arr, key):
        f = open(os.path.join(self.__path, self.__monsterFile))
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

    def __pairValueToStr(self, arr):
        return str(arr[0]) + "-" + str(arr[1])

    def getAttackValue(self):
        return random.randrange(self.__att[0], self.__att[1]+1)

    def getDefenceValue(self):
        return random.randrange(self.__deff[0], self.__deff[1]+1)

    def getXp(self):
        return self.__xp

    def getReward(self):
        return self.__reward

    def attack(self, value):
        self.__hp = self.__hp - int(value)

    def heal(self, value):
        self.__hp = self.__hp + int(value)

    def isDead(self):
        if self.__hp <= 0:
            return True
        else:
            return False

    def toString(self):
        temp = "NAME: " + str(self.__name) + "\tTYPE: " + str(self.__type.getType().name) + "\n"
        temp = temp + "\t" + str(self.__desc) + "\nHP: " + str(self.__hp)
        temp = temp + "\t\t" + "ATT: " + self.__pairValueToStr(self.__att) + "\t" + "DEF: " + self.__pairValueToStr(self.__deff) + "\n"

        return temp

if __name__ == "__main__":
	raise Exception("Class can not be run as main. Must be imported!")