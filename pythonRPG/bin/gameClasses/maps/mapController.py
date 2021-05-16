from .map import Map
from enum import Enum, unique
from .tile import Tile
from .tile import Draw
from .tile import Type
from bin.gameClasses.items import *
from bin.gameClasses.entities.shop import Shop
from bin.gameClasses.entities.player import Player
import random


class MapController:
    __mapArr = [[None, None, None], [None, None, None], [None, None, None]]
    __player = None
    __defaultUp = []
    __defaultDown = []
    __defaultLeft = []
    __defaultRight = []
    __defaultTile = Tile([-1, -1], Type.PLAIN, Draw.NONE, None)

    def __init__(self, player):
        self.__player = player
        for _ in range(1, 11):
            self.__defaultUp.append(self.__defaultTile)
            self.__defaultDown.append(self.__defaultTile)
            self.__defaultLeft.append(self.__defaultTile)
            self.__defaultRight.append(self.__defaultTile)

    def getMap(self, x, y):
        self.__checkPos(x, y)
        return self.__mapArr[y - 1][x - 1]

    def setMap(self, x, y, map):
        self.__checkPos(x, y)
        self.__mapArr[y - 1][x - 1] = map

    def swapMap(self, x1, y1, x2, y2):
        self.__checkPos(x1, y1)
        self.__checkPos(x2, y2)
        temp = self.getMap(x1, y1)
        self.setMap(x1, y1, self.getMap(x2, y2))
        self.setMap(x2, y2, temp)

    def updateMap(self, x, y):
        self.__checkPos(x, y)
        self.getMap(x, y).updateMap(self.__defaultUp, self.__defaultDown, self.__defaultLeft, self.__defaultRight)

    def genNewMap(self, mapCords):
        print("  (1/5) Generating map (" + str(mapCords[0]) + "-" + str(mapCords[1]) + ")...", end="")
        temp = Map(mapCords[0], mapCords[1], 10, self.__player)
        print("Done!")
        print("  (2/5) Filling in map...", end="")
        for x in range(1, 11):
            for y in range(1, 11):
                numT = random.randint(1, 100)
                if numT <= 11:
                    temp.setTile(x, y, Tile([x, y], Type.PLAIN, Draw.PLAIN_ONE, None))
                elif numT <= 22:
                    temp.setTile(x, y, Tile([x, y], Type.PLAIN, Draw.PLAIN_TWO, None))
                elif numT <= 33:
                    temp.setTile(x, y, Tile([x, y], Type.PLAIN, Draw.PLAIN_THREE, None))
                else:
                    temp.setTile(x, y, Tile([x, y], Type.PLAIN, Draw.NONE, None))
        print("Done!")
        print("  (3/5) Generating trees...", end="")
        self.__genTrees(temp, 0, 6, None)
        print("Done!")
        print("  (4/5) Generating roads...", end="")
        self.__genRoads(temp, 0, 20, None)
        print("Done!")
        print("  (5/5) Generating shops...", end="")
        self.__genShops(temp, 0, 10)
        print("Done!")
        return temp

    def __genTrees(self, map, num, max, list):
        listT = []
        if num == max:
            return
        if list is None:
            treeSpawn = random.randint(1, 5)
            for _ in range(0, treeSpawn):
                tempX = random.randint(1, 10)
                tempY = random.randint(1, 10)
                map.setTile(tempX, tempY, Tile([tempX, tempY], Type.WILDERNESS, Draw.TREE, None))
                listT.append([tempX, tempY])
        else:
            for l in list:
                x = l[0]
                y = l[1]

                try:
                    temp = random.randint(1, 10)
                    if temp <= 6:
                        map.setTile(x - 1, y, Tile([x - 1, y], Type.WILDERNESS, Draw.TREE, None))
                        listT.append([x - 1, y])
                except ValueError:
                    pass

                try:
                    temp = random.randint(1, 10)
                    if temp <= 6:
                        map.setTile(x + 1, y, Tile([x + 1, y], Type.WILDERNESS, Draw.TREE, None))
                        listT.append([x + 1, y])
                except ValueError:
                    pass

                try:
                    temp = random.randint(1, 10)
                    if temp <= 6:
                        map.setTile(x, y - 1, Tile([x, y - 1], Type.WILDERNESS, Draw.TREE, None))
                        listT.append([x, y - 1])
                except ValueError:
                    pass

                try:
                    temp = random.randint(1, 10)
                    if temp <= 6:
                        map.setTile(x, y + 1, Tile([x, y + 1], Type.WILDERNESS, Draw.TREE, None))
                        listT.append([x, y + 1])
                except ValueError:
                    pass

        curr = num + 1
        self.__genTrees(map, curr, max, listT)

    def __genRoads(self, map, num, max, list):
        listT = []
        if num == max:
            return
        if list is None:
            roadSpawn = random.randint(1, 3)
            for _ in range(0, roadSpawn):
                tempX = random.randint(1, 10)
                tempY = random.randint(1, 10)
                map.setTile(tempX, tempY, Tile([tempX, tempY], Type.ROAD, Draw.ROAD_DEAD_END_NOWAY, None))
                listT.append([tempX, tempY])
        else:
            for l in list:
                x = l[0]
                y = l[1]

                upV = True
                downV = True
                leftV = True
                rightV = True

                upTile = None
                downTile = None
                leftTile = None
                rightTile = None

                try:
                    upTile = map.getTile(x, y - 1)
                except ValueError:
                    upV = False

                try:
                    downTile = map.getTile(x, y + 1)
                except ValueError:
                    downV = False

                try:
                    leftTile = map.getTile(x - 1, y)
                except ValueError:
                    leftV = False

                try:
                    rightTile = map.getTile(x + 1, y)
                except ValueError:
                    rightV = False

                if upV:
                    if upTile.getType() == Type.ROAD:
                        upV = False

                if downV:
                    if downTile.getType() == Type.ROAD:
                        downV = False

                if leftV:
                    if leftTile.getType() == Type.ROAD:
                        leftV = False

                if rightV:
                    if rightTile.getType() == Type.ROAD:
                        rightV = False

                try:
                    temp = map.getTile(x - 1, y - 1)
                    if temp.getType() == Type.ROAD:
                        upV = False
                        leftV = False
                except ValueError:
                    pass

                try:
                    temp = map.getTile(x + 1, y - 1)
                    if temp.getType() == Type.ROAD:
                        upV = False
                        rightV = False
                except ValueError:
                    pass

                try:
                    temp = map.getTile(x - 1, y + 1)
                    if temp.getType() == Type.ROAD:
                        downV = False
                        leftV = False
                except ValueError:
                    pass

                try:
                    temp = map.getTile(x + 1, y + 1)
                    if temp.getType() == Type.ROAD:
                        downV = False
                        rightV = False
                except ValueError:
                    pass

                if not upV and not downV and not leftV and not rightV:
                    pass
                else:
                    while True:
                        temp = random.randint(1, 4)
                        if temp == 1:
                            if upV:
                                map.setTile(x, y - 1, Tile([x, y - 1], Type.ROAD, Draw.ROAD_DEAD_END_NOWAY, None))
                                listT.append([x, y - 1])
                                break
                        elif temp == 2:
                            if downV:
                                map.setTile(x, y + 1, Tile([x, y + 1], Type.ROAD, Draw.ROAD_DEAD_END_NOWAY, None))
                                listT.append([x, y + 1])
                                break
                        elif temp == 3:
                            if leftV:
                                map.setTile(x - 1, y, Tile([x - 1, y], Type.ROAD, Draw.ROAD_DEAD_END_NOWAY, None))
                                listT.append([x - 1, y])
                                break
                        elif temp == 4:
                            if rightV:
                                map.setTile(x + 1, y, Tile([x + 1, y], Type.ROAD, Draw.ROAD_DEAD_END_NOWAY, None))
                                listT.append([x + 1, y])
                                break

        curr = num + 1
        self.__genRoads(map, curr, max, listT)

    def __genShops(self, map, num, max):
        if num == max:
            return

        if random.randint(1, 100) <= 20:
            flag = False
            tempX = random.randint(1, 10)
            tempY = random.randint(1, 10)

            try:
                if map.getTile(tempX - 1, tempY).getType() == Type.ROAD:
                    flag = True
            except ValueError:
                pass

            try:
                if map.getTile(tempX + 1, tempY).getType() == Type.ROAD:
                    flag = True
            except ValueError:
                pass

            try:
                if map.getTile(tempX, tempY - 1).getType() == Type.ROAD:
                    flag = True
            except ValueError:
                pass

            try:
                if map.getTile(tempX, tempY + 1).getType() == Type.ROAD:
                    flag = True
            except ValueError:
                pass

            if map.getTile(tempX, tempY).getType() == Type.ROAD:
                flag = False

            if flag:
                map.setTile(tempX, tempY, Tile([tempX, tempY], Type.BUILDING, Draw.SHOP, Shop(random.randint(5, 20), self.__player.getXP().getLevel())))

        curr = num + 1
        self.__genShops(map, curr, max)

    def __checkPos(self, x, y):
        if x < 1 or x > 3:
            raise ValueError("Error: X must be greater than 0 and less than 4; X is " + str(x) + "!")
        if y < 1 or y > 3:
            raise ValueError("Error: Y must be greater than 0 and less than 4; Y is " + str(x) + "!")

    @unique
    class Move(Enum):
        LEFT = "left"
        RIGHT = "right"
        UP = "up"
        DOWN = "down"


if __name__ == "__main__":
    MapController(None)
    # raise Exception("Class can not be run as main. Must be imported!")
