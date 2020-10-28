from ..other import Inv
from ..other import XP
import random
from ..items import Armor
from ..items import Weapon
from ..items import Potion

class Player:
    __inv = None
    __xp = None
    __name = ""
    __money = 0
    __maxHealth = 100
    __health = 100
    __attack = [1, 5]
    __attMod = None
    __defence = [1,3]
    __defMod = None

    def __init__(self, name, levelCap=0):
        self.__name = name
        self.__xp = XP(levelCap)
        self.__inv = Inv()
        self.__attMod = Weapon("default", 1)
        self.__defMod = Armor("default", 1)

    def getHealth(self):
        return self.__health

    def getMaxHealth(self):
        return self.__maxHealth

    def getInv(self):
        return self.__inv

    def getXP(self):
        return self.__xp

    def getMoney(self):
        return self.__money

    def getAttack(self):
        return random.randrange(self.__attack[0], self.__attack[1]+1) + self.__attMod.getDamageValue()
 
    def getDefence(self):
        return random.randrange(self.__defence[0], self.__defence[1]+1) + self.__defMod.getDefenseValue()

    def equipItem(self, id):
        temp = self.__inv.equip(id)
        if isinstance(temp, Armor):
            self.__defMod = temp
        elif isinstance(temp, Weapon):
            self.__attMod = temp

    def __setHealth(self, num):
        self.__health = num

    def subHealth(self, effect):
        self.__setHealth(self.getHealth - effect)
        if self.__health < 0:
            self.__health = 0

    def addHealth(self, effect):
        self.__setHealth(self.getHealth + effect)
        if self.__health > self.__maxHealth:
            self.__health = self.__maxHealth

    def addXP(self, num):
        if self.__xp.addXP(num):
            self.__maxHealth = int(self.__maxHealth + (self.__maxHealth/5)*(self.__xp.getLevel()*(self.__xp.getLevel()/7)))
        return True

    def addMoney(self, amount):
        self.__money = self.__money + amount

    def removeMoney(self, amount):
        if self.__money - amount < 0:
            return False
        else:
            self.__money = self.__money - amount
            return True

    def toString(self):
        temp = "NAME: " + str(self.__name) + "\n"
        temp = temp + "MONEY: $" + str(self.getMoney()) + "\n" 
        temp = temp + "HEALTH: " + str(self.getHealth()) + "\\" + str(self.getMaxHealth()) + "\n"
        temp = temp + self.__xp.toString() + "\n"
        temp = temp + "------------------------"
        return temp