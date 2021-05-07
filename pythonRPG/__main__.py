#!/usr/bin/env python3

import sys
import os
import time
import random
import pickle
import re
from bin.gameClasses.items import *
from bin.gameClasses.entities import *
from bin.gameClasses.entities import Shop
from bin.gameClasses.other import utility
from bin.common import currWorkDir

class Game:
    __loaded = False
    __shop = None
    __player = None

    
    __savePath = os.path.join(currWorkDir, "bin", "saves")

    def __init__(self):
        while (True):
            self.clearScreen()
            print("Welcome to PythonRPG!")
            print("version: In-Dev 0.4.1")
            print("What would you like to do?")
            print("1 | Play game")
            print("2 | Credits")
            print("3 | Exit")
            temp = self.getInput(3)

            if temp == 1:
                self.clearScreen()
                print("What is your name? ")
                temp = ""
                while True:
                    print(">>>", end="")
                    temp = input()
                    flag = True
                    for x in temp:
                        xFlag = True
                        yFlag = True
                        zFlag = True
                        if not x.isalpha():
                            xFlag=False
                        if not x.isspace():
                            yFlag = False
                        if not x == '-':
                            zFlag = False

                        if not(xFlag == True or yFlag == True or zFlag == True):
                            print("Error: name can only contain letter, spaces,and hyphons!")
                            flag = False
                            break
                    if flag:
                        break

                try:
                    print("Loading save game...", end="")
                    temp = GameDataController().loadAll(temp)
                    self.__shop = temp[1]
                    self.__player = temp[0]
                    print("Done!")
                    self.__loaded = True
                    time.sleep(3)
                    print("Starting game...")
                    time.sleep(3)
                    self.clearScreen()
                    self.play()
                    break
                except FileNotFoundError:
                    print("Error: There is no save file with that name!")
                    time.sleep(3)
                    print("Starting new game...")
                    time.sleep(3)
                    self.__player = Player(temp)
                    self.clearScreen()
                    self.play()
                except KeyError:
                    print("Error: There was a problem loading the save files!")
                    print("Type anything to contine...", end="")
                    input()
                    print("Goodbye!")
                    exit(1)

            elif temp == 2:
                self.clearScreen()
                print("Game Design by: Omar Radwan")
                print("Game Programmer by: Omar Radwan")
            elif temp == 3:
                print("Goodbye!")
                exit(0)
            print("Type anything to contine...", end="")
            input()

        self.clearScreen()

    def play(self):
        if self.__loaded:
            self.visitShop(shop=self.__shop)
        while(True):
            temp = random.randint(3, 7)
            for _ in range(1, temp):
                self.fightMonster()
            self.visitShop()
    
    def getInput(self, numOfoptions):
        while(True):
                print(">>>",end="")
                temp = input()

                try:
                    temp = int(temp)
                    if (temp < 1 or temp > numOfoptions):
                        print("Error: Number out of range!")
                    else:
                        break
                except ValueError:
                    print("Error: You did not enter a number!")
        return temp

    def useInv(self, printable=False):
        while(True):
            self.clearScreen()
            print("Inventory:")
            print("----------------------------------------------------")
            print(self.__player.getInv().toString(True, True), end="")
            print("----------------------------------------------------")
            if printable:
                return None
            print("What would you like to do?")
            print("1 | Equip Item")
            print("2 | More Info")
            print("3 | Back")
            print("4 | Quit")
            temp = self.getInput(4)
            if temp == 1:
                if self.__player.getInv().toString(True, True) == "Your inventory is empty!\n":
                    print("There are no items in your inventory to equip!")
                    print("Type anything to contine...", end="")
                    input()
                else:
                    print("What item would you like to equip?")
                    temp = self.getInput(self.__player.getInvLen())
                    self.__player.equipItem(temp-1)
            elif temp == 2:
                if self.__player.getInv().toString(True, True) == "Your inventory is empty!\n":
                    print("There are no items in your inventory to see more info for!")
                else:
                    print("What item would you like to see info for?")
                    temp = self.getInput(self.__player.getInvLen())
                    self.clearScreen()
                    temp = self.__player.getInv().getItem(temp)
                    if isinstance(temp, Weapon):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                    elif isinstance(temp, Potion):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------") 
                    elif isinstance(temp, Armor):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                print("Type anything to contine...", end="")
                input()
            elif temp == 3:
                return None
            elif temp == 4:
                print("Goodbye!")
                exit(0)

    def visitShop(self, shop=None):
        currShop = None
        if shop == None:
            currShop = Shop(random.randrange(5,15), self.__player.getXP().getLevel())
        else:
            currShop = shop

        while(True):
            self.clearScreen()
            print(currShop.toString(), end="")
            print("--------------")
            print("MONEY: $" + str(self.__player.getMoney()))
            print("----------------------------------------------------")
            print("What would you like to do?")
            print("1 | Buy Item")
            print("2 | Sell Item")
            print("3 | More Info")
            print("4 | Inventory")
            print("5 | Contine")
            print("6 | Save Game")
            print("7 | Quit")
            temp = self.getInput(7)
            if temp == 1:
                if currShop.getLenght() == 0:
                    print("There are no items to buy!")
                    print("Type anything to contine...", end="")
                    input()
                else:
                    print("What item would you like to buy?")
                    temp = self.getInput(currShop.getLenght())
                    if currShop.getCost(temp) > self.__player.getMoney():
                        print("You do not have enough money!")
                        print("Type anything to contine...", end="")
                        input()
                    else:
                        print("I made it here as well")
                        temp = currShop.buyItem(temp)
                        if isinstance(temp, Weapon):
                            self.__player.removeMoney(temp.getCostValue())
                            temp.halfCostValue()
                            self.__player.getInv().addItem(temp)
                        elif isinstance(temp, Armor):
                            self.__player.removeMoney(temp.getCostValue())
                            temp.halfCostValue()
                            self.__player.getInv().addItem(temp)
                        elif isinstance(temp, Potion):
                            self.__player.removeMoney(temp.getCostValue())
                            temp.halfCostValue()
                            self.__player.getInv().addItem(temp)
            elif temp == 2:
                self.useInv(True)
                if  self.__player.getInvLen() == 0:
                    print("You have no items to sell!")
                    print("Type anything to contine...", end="")
                    input()
                else:
                    print("What item would you like to sell?")
                    temp = self.getInput(self.__player.getInvLen())
                    temp = self.__player.getInv().removeItem(temp)
                    if isinstance(temp, Weapon):
                        self.__player.removeMoney(temp.getCostValue())
                        temp.doubleCostValue()
                        currShop.sellItem(temp)
                    elif isinstance(temp, Armor):
                        self.__player.removeMoney(temp.getCostValue())
                        temp.doubleCostValue()
                        currShop.sellItem(temp)
                    elif isinstance(temp, Potion):
                        self.__player.removeMoney(temp.getCostValue())
                        temp.doubleCostValue()
                        currShop.sellItem(temp)
            elif temp == 3:
                if currShop.getLenght() == 0:
                    print("There are no items in the shop to see more info for!")
                else:
                    print("What item would you like to see info for?")
                    temp = self.getInput(currShop.getLenght())
                    self.clearScreen()
                    temp = currShop.getItem(temp)
                    if isinstance(temp, Weapon):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                    elif isinstance(temp, Potion):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                    elif isinstance(temp, Armor):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                print("Type anything to contine...", end="")
                input()
            elif temp == 4:
                self.useInv()
            elif temp == 5:
                print("Are you sure you want to contine?")
                print("1 | Yes")
                print("2 | No")
                temp = self.getInput(2)
                if temp == 1:
                    self.clearScreen()
                    print("Thank you for visiting my shop! Please come again!")
                    print("Type anything to contine...", end="")
                    input()
                    self.clearScreen()
                    return None
            elif temp == 6:
                print("Saving...", end="")
                GameDataController.saveAll(GameDataController, self.__player.getName(), self.__player, currShop)
                print("Done!")

                print("Type anything to contine...", end="")
                input()
            elif temp == 7:
                print("Goodbye!")
                exit(0)
                
    def fightMonster(self):
        temp = os.path.join(currWorkDir, "monsters")
        (_, _, files) = next(os.walk(temp))
        if len(files) == 0:
            raise Exception("There are no monsters to choose from!")
        rand = random.randrange(0, len(files))
        files = files[rand].split(".")[0]
        monst = Monster(files, self.__player.getXP().getLevel())
        print("You encountered a monster!")
        while(True):
            print(monst.toString())
            print(self.__player.toString())
            print("What would you like to do?")
            print("1 | Attack")
            print("2 | Use Potion")
            print("3 | Inventory")
            print("4 | Quit")
            temp = self.getInput(4)
            if (temp == 1):
                totalPlayerAtt = 0
                self.clearScreen()
                playerAtt = self.__player.getAttack(monst)
                for x in playerAtt:
                    try:
                        x[3]
                        if not x[3]:
                            print("You dealed " + str(x[0]) + " " + str(x[1]) + " damage to the Monster! (x" + str(x[2]) + ")")
                        else:
                            print("You healed " + str(x[0]) + " health!")
                            totalPlayerAtt = totalPlayerAtt - x[0]
                    except IndexError:
                        print("You deal " + str(x[0]) + " damage to the monster!")
                    totalPlayerAtt = totalPlayerAtt + x[0]
                    time.sleep(3)
                monstDef = monst.getDefenceValue()
                print("The monster protects against " + str(monstDef) + " damage!")
                totalPlayerAtt = totalPlayerAtt - monstDef
                if totalPlayerAtt < 0:
                    totalPlayerAtt = 0
                monst.attack(totalPlayerAtt)

                time.sleep(3)

                if monst.isDead():
                    print("You killed the monster!")
                    time.sleep(3)
                    money =  monst.getReward()
                    self.__player.addMoney(money)
                    print("You gained $" + str(money) + "!")
                    time.sleep(3)
                    xp = monst.getXp()
                    print("You gained " + str(xp) + " XP!")
                    time.sleep(1)
                    temp = self.__player.addXP(xp)
                    if temp != 0:
                        print("You leveled up! x" + str(temp))
                    temp = random.randrange(0,10)
                    if temp <= 3:
                        temp = random.randrange(0,10)
                        if temp <= 6:
                            #one items
                            item = self.genRandomItem()
                            print("The monster dropped " + str(item.getName()) + "!")
                            self.__player.getInv().addItem(item)
                        elif temp > 6 and temp <= 9:
                            #two items
                            for _ in range(0,1):
                                time.sleep(3)
                                item = self.genRandomItem()
                                print("The monster dropped " + str(item.getName()) + "!")
                                self.__player.getInv().addItem(item)
                        else:
                            #three items
                            for _ in range(0,2):
                                time.sleep(3)
                                item = self.genRandomItem()
                                print("The monster dropped " + str(item.getName()) + "!")
                                self.__player.getInv().addItem(item)
                    else:
                        time.sleep(3)
                        print("The monster did not drop anything!")

                    time.sleep(3)
                    self.clearScreen()
                    break

                monAtt = monst.getAttackValue()
                print("The monster deals " + str(monAtt) + " damage to you!")
                time.sleep(3)
                playerDef = self.__player.getDefence(monst)
                totalDef = 0
                for x in playerDef:
                    try:
                        x[2]
                        print("You protected against " + str(x[0]) + " damage using your " + str(x[1]) + " defence! (x" + str(x[2]) + ")")
                    except IndexError:
                        print("You protected against " + str(x[0]) + " damage!")
                    totalDef = totalDef + x[0]
                    time.sleep(3)

                monAtt = monAtt - totalDef
                if monAtt < 0:
                    monAtt = 0
                self.__player.subHealth(monAtt)
                #time.sleep(3)
                if self.__player.isDead():
                    self.clearScreen()
                    print("YOU HAVE DIED!")
                    print("Type anything to contine...", end="")
                    input()
                    print("Good Bye!")
                    sys.exit(0)

                print("Type anything to contine...", end="")
                input()
                self.clearScreen()
                    
            elif (temp == 2):
                self.clearScreen()
                temp = self.__player.getInv().getlist(Potion("default", 0))
                if temp.getLen() == 0:
                    print("----------------------------------------------------")
                    print("You have no potions!")
                    print("----------------------------------------------------")
                else:
                    print("----------------------------------------------------")
                    print(temp.toString(True))
                    print("----------------------------------------------------")
                    print("What potion would you like to use?")
                    userIn = self.getInput(temp.getLen())
                    temp = temp.removeItem(userIn)
                    print(temp.toString())
                    print("Who would you like it to effect?")
                    print("1 | You")
                    print("2 | Monster")
                    userIn = self.getInput(2)

                    self.clearScreen()
                    self.__player.getInv().removeItem(userIn)
                    if isinstance(temp, Potion):
                        temp = temp.getEffects()
                        for x in temp:
                            if isinstance(x, Effect):
                                currHeal = x.getRandom()
                                if x.getType() == EffectStatus.HEAL:
                                    if userIn == 1:
                                        self.__player.addHealth(currHeal)
                                        print("You healed " , currHeal, " health!")
                                    else:
                                        monst.heal(currHeal)
                                        print("The monster healed ", currHeal, " health!")
                                elif x.getType() == EffectStatus.DAMAGE:
                                    if userIn == 1:
                                        self.__player.subHealth(currHeal)
                                        print("You took", currHeal, " damage!")
                                    else:
                                        monst.attack(currHeal)
                                        print("The monster took ", currHeal, " damage!")
                        
                        time.sleep(3)
                        if self.__player.isDead():
                            self.clearScreen()
                            print("YOU HAVE DIED!")
                            print("Type anything to contine...", end="")
                            input()
                            print("Good Bye!")
                            sys.exit(0)

                        if monst.isDead():
                            self.clearScreen()
                            print("You killed the monster!")
                            time.sleep(3)
                            money =  monst.getReward()
                            self.__player.addMoney(money)
                            print("You gained $" + str(money) + "!")
                            time.sleep(3)
                            xp = monst.getXp()
                            print("You gained " + str(xp) + " XP!")
                            time.sleep(1)
                            temp = self.__player.addXP(xp)
                            if temp != 0:
                                print("You leveled up! x" + str(temp))
                            time.sleep(3)
                            self.clearScreen()
                            break
                        
                    print("Type anything to contine...", end="")
                    input()
                self.clearScreen()
            elif (temp == 3):
                self.clearScreen()
                self.useInv()
                self.clearScreen()
            elif (temp == 4):
                print("Good Bye!")
                exit(0)

    def genRandomItem(self):
        path = os.path.join(currWorkDir, "items")
        temp = random.randrange(0, 3)
        currList = list()

        if temp == 0:
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.potion)$')
            path = os.path.join(path, "potions")
            (__, __, files) = next(os.walk(path))
            if len(files) == 0:
                raise Exception("There are no potion files to choose from!")
            for x in files:
                if not x == "default.potion":
                    if not regex.search(x):
                        currList.append(x)
            rand = random.randrange(0, len(currList))
            temp = currList[rand].split(".")[0]
            temp = Potion(temp, self.__player.getXP().getLevel())
            return temp

        elif temp == 1:
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.weapon)$')
            path = os.path.join(path, "weapons")
            (__, __, files) = next(os.walk(path))
            if len(files) == 0:
                raise Exception("There are no weapon files to choose from!")
            for x in files:
                if not x == "default.weapon":
                    if not regex.search(x):
                        currList.append(x)
            rand = random.randrange(0, len(currList))
            temp = currList[rand].split(".")[0]
            temp = Weapon(temp, self.__player.getXP().getLevel())
            return temp
        elif temp == 2:
            regex = re.compile('Effect[1-9]{1}([0-9]{0,}.armor)$')
            path = os.path.join(path, "armors")
            (__, __, files) = next(os.walk(path))
            if len(files) == 0:
                raise Exception("There are no armor files to choose from!")
            for x in files:
                if not x == "default.armor":
                    if not regex.search(x):
                        currList.append(x)
            rand = random.randrange(0, len(currList))
            temp = currList[rand].split(".")[0]
            temp = Armor(temp, self.__player.getXP().getLevel())
            return temp
        return None


    def clearScreen(self):
        for _ in range(0, 50):
            print("\n\n\n\n\n")

if __name__ == "__main__":
    temp = Game()
    temp.play()