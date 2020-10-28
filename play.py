#!/usr/bin/env python3

import sys
import os
import random
from bin.gameClasses.entities import *

#sys.path.append(os.path.abspath(os.path.join("bin", "gameClasses")))  

class Game:
    __player = ""

    def __init__(self):
        print("What is your name: ", end="")
        self.__player = Player(input())


    def play(self):
        temp =  random.randrange(5, 15)
        for _ in range(0, 1):
            (_, _, files) = next(os.walk("monsters"))
            if len(files) == 0:
                raise Exception("There are no monsters to choose from!")
            rand = random.randrange(0, len(files))
            files = files[rand].split(".")[0]
            monst = Monster(files, self.__player.getXP().getLevel())

            while(True):
                print("You encountered a monster!")
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
                    pass
                elif (temp == 2):
                    pass
                elif (temp == 3):
                    pass
                elif (temp == 4):
                    print("Good Bye!")
                    exit(0)

if __name__ == "__main__":
    temp = Game()
    temp.play()