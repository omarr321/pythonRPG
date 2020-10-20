from entities import *

class Game:
    __player = ""

    def __init__(self):
        print("What is your name: ", end="")
        self.__player = Player(input())


    def play(self):
        pass

if __name__ == "__main__":
    temp = Game()
    temp.play()