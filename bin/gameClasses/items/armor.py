import os
import random
from .item import Item

class Armor(Item):
    __path = os.path.join(os.getcwd(), "..", "..", "items", "armors")
    __armorFile = ""
    __name = ""
    __desc = ""
    __defense = [0, 0]
    __cost = [0, 0]

    def __init__(self, armorName, playerLevel):
        self.__armorFile = str.lower(str(armorName) + ".armor")
        if not os.path.exists(os.path.join(self.__path, self.__armorFile)):
            raise Exception("Can not find " + armorName + ".armor!")

        self.__name = self.__getStringValue("name")
        self.__desc = self.__getStringValue("desc")
        self.__setNumberPair(self.__defense, "defense")
        self.__setNumberPair(self.__cost, "cost")
        self.__cost = random.randrange(self.__cost[0], self.__cost[1] + 1)

        self.__defense[0] = int(self.__defense[0] + (self.__defense[0]/3)*(playerLevel*(playerLevel/4)))
        self.__defense[1] = int(self.__defense[1] + (self.__defense[1]/3)*(playerLevel*(playerLevel/4)))
        self.__cost = int(self.__cost + (self.__cost/2)*(playerLevel*(playerLevel/3)))

    def __getStringValue(self, key):
        f = open(os.path.join(self.__path, self.__armorFile))
        for line in f:
            if line.startswith(key + ":"):
                temp = line.split(":")
                f.close()
                return temp[1]
        f.close()
        raise Exception("Can not find key \"" + str(key) + "\"!")


    def __setNumberPair(self, arr, key):
        f = open(os.path.join(self.__path, self.__armorFile))
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

    def getDefenseValue(self):
        return random.randrange(self.__defense[0], self.__defense[1] + 1)

    def getCostValue(self):
        return self.__cost

    def toString(self):
        temp = "NAME: " + str(self.__name)
        temp = temp + "\t" + str(self.__desc) + "DEFENSE: " + self.__pairValueToStr(self.__defense) + "\n"
        temp = temp + "COST: " + str(self.__cost) + "\n"

        return temp
    
    def toStringLine(self):
        nameN = self.__name.split("\n")[0]
        leng = 16 - len(self.__name)
        for _ in range(0,leng):
            nameN = nameN + " "
        return "TYPE: Armor    " + " NAME: " + str(nameN) + " COST: " + str(self.__cost)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")