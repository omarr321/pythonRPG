#!/usr/bin/env python3

import sys
import os
import time
import random
from bin.gameClasses.items import *
from bin.gameClasses.entities import *
from bin.gameClasses.entities import Shop

#sys.path.append(os.path.abspath(os.path.join("bin", "gameClasses")))  

class Game:
    __player = ""

    def __init__(self):
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

            

        self.__player = Player(temp)
        #!--FOR TESTING DO NOT KEEP IN AFTER FINAL RLEASE--!#
        self.__player.addMoney(1000)
        #!--FOR TESTING DO NOT KEEP IN AFTER FINAL RLEASE--!#

        self.clearScreen()


    def play(self):
        #self.visitShop()
        temp =  random.randrange(5, 15)
        for _ in range(0, temp):
            self.fightMonster()
        
        self.fightMonster()
    
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
                        print("Type anything to contine...")
                    elif isinstance(temp, Potion):
                        print("----------------------------------------------------")
                        print(temp.toString(), end="")
                        print("----------------------------------------------------")
                        print("Type anything to contine...")
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

        


    def visitShop(self):
        temp = random.randrange(5, 15)
        currShop = Shop(temp, self.__player.getXP().getLevel())
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
                        print ("You do not have enough money!")
                    else:
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
                    print("Thank you for visiting my shop! Please come again!")
                    print("Type anything to contine...", end="")
                    input()
                    return None
            elif temp == 6:
                #TODO: Implement saving
                print("Error: Saving is not implemented!")
                print("Type anything to contine...", end="")
                input()
            elif temp == 7:
                print("Goodbye!")
                exit(0)

    #TODO:Make it so the monster drops items sometimes.
    def fightMonster(self):
        (_, _, files) = next(os.walk("monsters"))
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
                    self.__player.addXP(xp)
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
                #TODO: Fix potion list thing
                print("Error: Potion useage is broken!")
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

    def clearScreen(self):
        for _ in range(0, 50):
            print("\n\n\n\n\n")

if __name__ == "__main__":
    temp = Game()
    temp.play()