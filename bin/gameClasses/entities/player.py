from other import Inv
from other import XP

class Player:
    __inv = Inv()
    __xp = XP()
    __name = ""
    __money = 0
    __maxHealth = 100
    __health = 100
    __attack = [1, 5]
    __attMod = [0, 0]
    __defence = [1,3]
    __defMod = [0, 0]

    def __init__(self, name):
        self.__name = name

    def getHealth(self):
        return self.__health

    def getMaxHealth(self):
        return self.__maxHealth

    def getInv(self):
        return self.__inv

    def getMoney(self):
        return self.__money

    def getAttack(self):
        pass

    def getDefence(self):
        pass

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
        temp = "MONEY: $" + str(self.getMoney()) + "\n" 
        temp = temp + "HEALTH: " + str(self.getHealth()) + "\\" + str(self.getMaxHealth()) + "\n"
        temp = temp + self.__xp.toString() + "\n"
        temp = temp + "------------------------"
        return temp