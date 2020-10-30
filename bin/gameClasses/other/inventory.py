import sys
import os

from ..items import Item
from ..items import Armor
from ..items import Potion
from ..items import Weapon
from .utility import sortList

class Inv:
    __inv = list()

    def __init__(self):
        pass

    def getItem(self, id):
        if id <= 0 or id > len(self.__inv):
            return None
        else:
            id = id - 1
            return self.__inv[id]

    def addItem(self, item):
        if isinstance(item, Item):
            self.__inv.append([item, False])
            return True
        else:
            return False

    def removeItem(self, id):
        if id <= 0 or id > len(self.__inv):
            id = id - 1
            self.__inv.remove(id)

    def getlist(self, item):
        temp = Inv()
        if isinstance(item, Weapon):
            for x in self.__inv:
                if isinstance(x, Weapon):
                    temp.addItem(x)
        elif isinstance(item, Armor):
            for x in self.__inv:
                if isinstance(x, Armor):
                    temp.addItem(x)
        elif isinstance(item, Potion):
            for x in self.__inv:
                if isinstance(x, Potion):
                    temp.addItem(x)
        else:
            return None

        if temp.toString() == "Your inventory is empty!":
            temp = ""
            if isinstance(item, Potion):
                temp = "You have no potions!"
            elif isinstance(item, Weapon):
                temp = "You have no Weapons!"
            elif isinstance(item, Armor):
                temp = "You have no Armors!"
            return temp
        else:
            return temp.toString()

    def sort(self):
        armor = list()
        weapon = list()
        potion = list()
            
        for x in self.__inv:
            if isinstance(x[0], Armor):
                armor.append(x)
            elif isinstance(x[0], Weapon):
                weapon.append(x)
            else:
                potion.append(x)
        
        armor = sortList(armor,0)
        weapon = sortList(weapon, 0)
        potion = sortList(potion, 0)

        together = list()
        
        for x in armor:
            together.append(x)

        for x in  weapon:
            together.append(x)

        for x in potion:
            together.append(x)

        self.__inv = together

    def __unequip(self,id):
        if id <= 0 or id > len(self.__inv):
            id = id - 1
            self.__inv[id][1] = False
            return True
        return False

    def equip(self, id):
        if isinstance(self.__inv[id][0], Potion):
            print("You can not equip a Potion!")
            return None
        elif isinstance(self.__inv[id][0], Weapon):
            for x in self.__inv:
                if isinstance(x[0], Weapon):
                    x[1] = False
        else:
            for x in self.__inv:
                if isinstance(x[0], Armor):
                    x[1] = False

        if id <= 0 or id > len(self.__inv):
            id = id - 1
            self.__inv[id][1] = True
            return self.__inv[id][0]
        return None

    def toString(self, numbered=False):
        if len(self.__inv) == 0:
            return "Your inventory is empty!"

        temp = ""
        if numbered:
            for c, x in enumerate(self.__inv):
                if c < 9:
                    temp = temp + "0" + str(c+1) + " | " + x[0].toStringLine() + "\n"
                else:
                    temp = temp + str(c+1) + " | " + x[0].toStringLine() + "\n"
            return temp
        else:
            for x in self.__inv:
                temp = temp + x[0].toStringLine() + "\n"
            return temp

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")