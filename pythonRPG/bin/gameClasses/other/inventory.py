import sys
import os

from ..items import Item
from ..items import Armor
from ..items import Potion
from ..items import Weapon
from .utility import sortList

class Inv:
    __inv = None

    def __init__(self):
        self.__inv = list()

    def getItem(self, id):
        if id <= 0 or id > len(self.__inv):
            return None
        else:
            id = id - 1
            return self.__inv[id][0]

    def addItem(self, item, equiped=False):
        if isinstance(item, Item):
            self.__inv.append([item, equiped])
            return True
        else:
            return False

    def removeItem(self, id):
        if id <= 0 or id > len(self.__inv):
            return None
        else:
            id = id - 1
            return self.__inv.pop(id)[0]

    def getlist(self, item):
        temp = Inv()
        if isinstance(item, Weapon):
            for x in self.__inv:
                if isinstance(x[0], Weapon):
                    temp.addItem(x[0])
        elif isinstance(item, Armor):
            for x in self.__inv:
                if isinstance(x[0], Armor):
                    temp.addItem(x[0])
        elif isinstance(item, Potion):
            for x in self.__inv:
                if isinstance(x[0], Potion):
                    temp.addItem(x[0])
        else:
            return None

        return temp

    def sort(self):
        armorE = list()
        weaponE = list()
        armor = list()
        weapon = list()
        potion = list()
            
        for x in self.__inv:
            if isinstance(x[0], Armor):
                if x[1] == True:
                    armorE.append(x)
                else:
                    armor.append(x)
            elif isinstance(x[0], Weapon):
                if x[1] == True:
                    weaponE.append(x)
                else:
                    weapon.append(x)
            else:
                potion.append(x)
        
        armor = sortList(armor,0)
        weapon = sortList(weapon, 0)
        potion = sortList(potion, 0)

        together = list()
        
        for x in armorE:
            together.append(x)
        for x in weaponE:
            together.append(x)
        
        for x in armor:
            together.append(x)

        for x in  weapon:
            together.append(x)

        for x in potion:
            together.append(x)

        self.__inv = together

    def unequip(self,id):
        if id <= 0 or id > len(self.__inv):
            id = id - 1
            self.__inv[id][1] = False
            return self.__inv[id]
        return None

    def equip(self, id):
        if isinstance(self.__inv[id][0], Potion):
            return None

        for x in self.__inv:
            if isinstance(self.__inv[id][0], Weapon):
                if isinstance(x[0], Weapon):
                    x[1] = False
            elif isinstance(self.__inv[id][0], Armor):
                if isinstance(x[0], Armor):
                    x[1] = False

        self.__inv[id][1] = True
        return self.__inv[id][0]

    def getLen(self):
        return len(self.__inv)

    def toString(self, numbered=False, equiped=False):
        self.sort()

        if len(self.__inv) == 0:
            return "Your inventory is empty!\n"

        temp = ""

        for c, x in enumerate(self.__inv):
            if numbered:
                if c < 9:
                    temp = temp + "0" + str(c+1) + " | "
                else:
                    temp = temp + str(c+1) + " | "

            temp = temp + x[0].toStringLine()

            if  equiped:
                temp = temp + " | "
                if x[1] == False:
                    temp = temp + "--------"
                else:
                    temp = temp + "EQUIPPED"

            temp = temp + "\n"

        return temp

    def toSave(self):
        temp = list()
        for x in self.__inv:
            if isinstance(x[0], Weapon):
                temp.append([0, x[0]])
            elif isinstance(x[0], Armor):
                temp.append([1, x[0]])
            elif isinstance(x[0], Potion):
                temp.append([2, x[0]])
        return temp

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")