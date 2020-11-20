#!/usr/bin/env python3

import sys
import os
import time
import random
from bin.gameClasses.items import Potion
from bin.gameClasses.items import Weapon
from bin.gameClasses.entities import *
from bin.gameClasses.entities import Shop

#sys.path.append(os.path.abspath(os.path.join("bin", "gameClasses")))  

class Game:
    __player = ""

    def __init__(self):
        print("What is your name: ", end="")
        self.__player = Player(input())
        #!--FOR TESTING DO NOT KEEP IN AFTER FINAL RLEASE--!#
        #temp = Shop(10, 1)
        #print(temp.toString())
        #input()
        #self.__player.getInv().addItem(Weapon("test", 1))
        #self.__player.equipItem(0)
        #!--FOR TESTING DO NOT KEEP IN AFTER FINAL RLEASE--!#

        self.clearScreen()


    def play(self):
        temp =  random.randrange(5, 15)
        for _ in range(0, temp):
            self.fightMonster()
    
    def visitShop(self):
        pass

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
            print("3 | See inventory")
            print("4 | Quit")
            while(True):
                print(">>>",end="")
                temp = input()

                try:
                    temp = int(temp)
                    if (temp < 1 or temp > 4):
                        print("Error: Number out of range!")
                    else:
                        break
                except ValueError:
                    print("Error: You did not enter a number!")
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

                print("Type anything to contine...")
                input()
                self.clearScreen()
                    
            elif (temp == 2):
                self.clearScreen()
                print(self.__player.getInv().getlist(Potion("default", 0)))
                print("Type anything to contine...")
                input()
                self.clearScreen()
            elif (temp == 3):
                self.clearScreen()
                print(self.__player.getInv().toString())
                print("Type anything to contine...")
                input()
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