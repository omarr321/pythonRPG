from bin.gameClasses.entities import *
import random

class Game:
    __player = ""

    def __init__(self):
        print("What is your name: ", end="")
        self.__player = Player(input())


    def play(self):
        temp =  random.randrange(5, 15)
        for x in range(0, temp):
            print (str(x))


if __name__ == "__main__":
    temp = Game()
    temp.play()