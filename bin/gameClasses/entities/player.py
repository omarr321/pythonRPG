from ..other import Inv
from ..other import XP
import random
from ..items import Armor
from ..items import Weapon
from ..items import Potion
from .monster import Monster
from ..items import Effect
from ..items import EffectStatus

class Player:
    __inv = None
    __xp = None
    __name = ""
    __money = 0
    __maxHealth = 100
    __health = 100
    __attack = [2, 6]
    __attMod = None
    __defence = [1,4]
    __defMod = None

    def __init__(self, name, levelCap=0):
        self.__name = name
        self.__xp = XP(levelCap)
        self.__inv = Inv()
        self.__attMod = None
        self.__defMod = None

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

    def getAttack(self, monster):
        if isinstance(monster, Monster):
            temp = list()
            att = random.randrange(self.__attack[0], self.__attack[1]+1)
            temp.append([att])
            if not self.__attMod == None:
                weapon = self.__attMod.getEffects()

                for x in weapon:
                    if isinstance(x, Effect):
                        thing = x.getRandom()
                        muti = self.__getAttackMutipler(x, monster.getType())
                        monster.attack(thing * muti)
                        temp.append([thing*muti, x.getType(), muti])
            return temp
        else:
            print("Monster is not monster!")
            return list()

    def getDefence(self, monster):
        if isinstance(monster, Monster):
            temp = list()
            deff = random.randrange(self.__defence[0], self.__defence[1]+1)
            temp.append([deff])
            armor = self.__defMod.getEffects()

            for x in armor:
                if isinstance(x, Effect):
                    thing = x.getRandom()
                    self.subHealth(thing)
                    temp.append([thing, x.getType()])
            return temp
        else:
            print("Monster is not monster!")
            return list()

    def equipItem(self, id):
        temp = self.__inv.equip(id)
        if isinstance(temp, Armor):
            self.__defMod = temp
        elif isinstance(temp, Weapon):
            self.__attMod = temp

    def __getAttackMutipler(self, n1, n2):
        if isinstance(n1, Effect):
            if isinstance(n2, Effect):
                if n1.getType() == EffectStatus.ACID:
                    if n2.getType() == EffectStatus.ACID:
                        return .5
                    elif n2.getType() == EffectStatus.DARK:
                        return .5
                    elif n2.getType() == EffectStatus.FIRE:
                        return .5
                    elif n2.getType() == EffectStatus.ICE:
                        return 2
                    elif n2.getType() == EffectStatus.LIGHT:
                        return 2
                    else:
                        return 1
                elif n1.getType() == EffectStatus.DARK:
                    if n2.getType() == EffectStatus.ACID:
                        return 2
                    elif n2.getType() == EffectStatus.DARK:
                        return .5
                    elif n2.getType() == EffectStatus.FIRE:
                        return 0
                    elif n2.getType() == EffectStatus.ICE:
                        return 0
                    elif n2.getType() == EffectStatus.LIGHT:
                        return 2
                    else:
                        return 1
                elif n1.getType() == EffectStatus.FIRE:
                    if n2.getType() == EffectStatus.ACID:
                        return 2
                    elif n2.getType() == EffectStatus.DARK:
                        return 0
                    elif n2.getType() == EffectStatus.FIRE:
                        return .5
                    elif n2.getType() == EffectStatus.ICE:
                        return 2
                    elif n2.getType() == EffectStatus.LIGHT:
                        return 0
                    else:
                        return 1
                elif n1.getType() == EffectStatus.ICE:
                    if n2.getType() == EffectStatus.ACID:
                        return .5
                    elif n2.getType() == EffectStatus.DARK:
                        return 0
                    elif n2.getType() == EffectStatus.FIRE:
                        return 2
                    elif n2.getType() == EffectStatus.ICE:
                        return .5
                    elif n2.getType() == EffectStatus.LIGHT:
                        return 0
                    else:
                        return 1
                elif n1.getType() == EffectStatus.LIGHT:
                    if n2.getType() == EffectStatus.ACID:
                        return .5
                    elif n2.getType() == EffectStatus.DARK:
                        return 2
                    elif n2.getType() == EffectStatus.FIRE:
                        return 0
                    elif n2.getType() == EffectStatus.ICE:
                        return 0
                    elif n2.getType() == EffectStatus.LIGHT:
                        return .5
                    else:
                        return 1
                else:
                    return 1
            else:
                return 0
        else:
            return 0

    def __setHealth(self, num):
        self.__health = num

    def subHealth(self, effect):
        self.__setHealth(self.getHealth() - effect)
        if self.__health < 0:
            self.__health = 0

    def addHealth(self, effect):
        self.__setHealth(self.getHealth() + effect)
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

    def isDead(self):
        if self.__health == 0:
            return True
        else:
            return False

    def toString(self):
        temp = "NAME: " + str(self.__name) + "\n"
        temp = temp + "MONEY: $" + str(self.getMoney()) + "\n" 
        temp = temp + "HEALTH: " + str(self.getHealth()) + "\\" + str(self.getMaxHealth()) + "\n"
        temp = temp + self.__xp.toString() + "\n"
        temp = temp + "------------------------"
        return temp