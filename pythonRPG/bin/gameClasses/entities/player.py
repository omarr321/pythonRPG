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
    __money = 400
    __maxHealth = 100
    __health = 100
    __attack = [100, 200]
    __attMod = None
    __defence = [5,15]
    __defMod = None

    def __init__(self, name, levelCap=0, load=False, attMod=None, defMod=None, xp=None, inv=None, money=None, maxHP=None, HP=None):
        self.__name = name
        if load:
            self.__inv = inv
            self.__xp = xp
            self.__attMod = attMod
            self.__defMod = defMod
            self.__money = money
            self.__maxHealth = maxHP
            self.__health = HP
        else:
            self.__inv = Inv()
            self.__xp = XP(levelCap)
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

    def getAttMod(self):
        return self.__attMod

    def getDefMod(self):
        return self.__defMod

    def getAttack(self, monster):
        if isinstance(monster, Monster):
            temp = list()
            att = random.randrange(self.__attack[0], self.__attack[1]+1)
            temp.append([att, "BASE", 1, False])
            if not self.__attMod == None:
                weapon = self.__attMod.getEffects()

                for x in weapon:
                    if isinstance(x, Effect):
                        if not x.getType() == EffectStatus.DEFENSE:
                            if x.getType() == EffectStatus.HEAL:
                                thing = x.getRandom()
                                self.addHealth(thing)
                                temp.append([thing, "", 0, True])
                            elif x.getType() == EffectStatus.DAMAGE:
                                thing = x.getRandom()
                                #monster.attack(thing)
                                temp.append([thing, "NORMAL", 1, False])
                            else:
                                thing = x.getRandom()
                                muti = self.__getAttackMutipler(x, monster.getType())
                                #monster.attack(thing * muti)
                                temp.append([int(thing*muti), x.getType().name, muti, False])
            return temp
        else:
            print("Monster is not monster!")
            return list()

    def getDefence(self, monster):
        if isinstance(monster, Monster):
            temp = list()
            deff = random.randrange(self.__defence[0], self.__defence[1]+1)
            temp.append([deff, "BASE", 1])
            if not self.__defMod == None:
                armor = self.__defMod.getEffects()
                for x in armor:
                    if isinstance(x, Effect):
                        if x.getType() == EffectStatus.DEFENSE:
                            thing = x.getRandom()
                        #self.subHealth(thing)
                        temp.append([thing, x.getType().name, 1])
            return temp
        else:
            print("Monster is not monster!")
            return list()

    def unequipItem(self, id):
        temp = self.__inv.unequip(id)
        if temp != None:
            if isinstance(temp, Weapon):
                self.__defMod = None
            elif isinstance(temp, Armor):
                self.__attMod = None

    def equipItem(self, id):
        temp = self.__inv.equip(id)
        if isinstance(temp, Armor):
            self.__defMod = temp
        elif isinstance(temp, Weapon):
            self.__attMod = temp

    def getInvLen(self):
        return self.__inv.getLen()

    def getName(self):
        return self.__name

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
        temp = self.__xp.addXP(num)
        if temp[0]:
            self.__maxHealth = int(self.__maxHealth + (self.__maxHealth/5)*(self.__xp.getLevel()*(self.__xp.getLevel()/7)))
        return temp[1]

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
        temp = temp + "--------------------------"
        return temp