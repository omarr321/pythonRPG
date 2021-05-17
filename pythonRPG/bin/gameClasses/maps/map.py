from .tile import Tile, Draw, Type

class Map:
    __mapSize = -1
    __mapGrid = None
    __mapPos = [-1, -1]
    __swapTile = None

    __playerPos = [-1, -1]
    __playerTile = None

    def __init__(self, mapX, mapY, mapSize):
        self.__mapPos = [mapX, mapY]
        if mapSize < 1:
            raise ValueError("Error: Map size can not be negative!")
        self.__mapSize = mapSize
        
        tempB = []
        for _ in range(0, mapSize):
            tempA = []
            for _ in range(0, mapSize):
                tempA.append(None)
            tempB.append(tempA)
        self.__mapGrid = tempB
        self.__playerTile = Tile([-1, -1], Type.PLAIN, Draw.PLAYER, None)

    def getTile(self, x, y):
        self.__checkPos(y, x)
        return self.__mapGrid[y-1][x-1]

    def getPlayer(self):
        return self.__playerTile.getData()

    def getMapPos(self):
        return self.__mapPos

    def getMapSize(self):
        return self.__mapSize

    def getPlayerPos(self):
        return self.__playerPos

    def setPlayerPos(self, x, y):
        self.__checkPos(x, y)
        if not(self.__playerPos == [-1, -1]):
            self.setTile(self.__playerPos[0], self.__playerPos[1], self.__swapTile)
        self.__swapTile = self.getTile(x, y)
        self.setTile(x, y, self.__playerTile)
        self.__playerPos = [x, y]

    def setTile(self, x, y, tile):
        self.__checkPos(y, x)
        self.__mapGrid[y-1][x-1] = tile

    def updateMap(self, upRow, bottomRow, leftRow, rightRow):
        for x in range(1, self.__mapSize+1):
            for y in range(1, self.__mapSize+1):
                if x == 1 and y == 1:
                    self.getTile(x, y).update(upRow[0], self.getTile(x, y+1), leftRow[0], self.getTile(x+1, y))
                elif x == self.__mapSize and y == self.__mapSize:
                    self.getTile(x, y).update(self.getTile(x, y-1), bottomRow[self.__mapSize-1], self.getTile(x-1, y), rightRow[self.__mapSize-1])
                elif x == 1 and y == self.__mapSize:
                    self.getTile(x, y).update(self.getTile(x, y-1), bottomRow[0], leftRow[self.__mapSize-1], self.getTile(x+1, y))
                elif x == self.__mapSize and y == 1:
                    self.getTile(x, y).update(upRow[self.__mapSize-1], self.getTile(x, y+1), self.getTile(x-1, y), rightRow[0])
                elif x == 1 and not(y == 1):
                    self.getTile(x, y).update(self.getTile(x, y-1), self.getTile(x, y+1), leftRow[y], self.getTile(x+1, y))
                elif not(x == 1) and y == 1:
                    self.getTile(x, y).update(upRow[x], self.getTile(x, y+1), self.getTile(x-1, y), self.getTile(x+1, y))
                elif x == self.__mapSize and not(y == self.__mapSize):
                    self.getTile(x, y).update(self.getTile(x, y-1), self.getTile(x, y+1), self.getTile(x-1, y), rightRow[y])
                elif not(x == self.__mapSize) and y == self.__mapSize:
                    self.getTile(x, y).update(self.getTile(x, y-1), bottomRow[x], self.getTile(x-1, y), self.getTile(x+1, y))
                else:
                    self.getTile(x, y).update(self.getTile(x, y-1), self.getTile(x, y+1), self.getTile(x-1, y), self.getTile(x+1, y))
    
    def toString(self):
        temp = "|="
        for _ in range(1, self.__mapSize+1):
            temp = temp + "==="
        temp = temp + "=|\n"
        for x in self.__mapGrid:
            temp = temp + "||"
            for y in x:
                temp = temp + y.getDraw().value.split("\n")[0]
            temp = temp + "||\n||"
            for y in x:
                temp = temp + y.getDraw().value.split("\n")[1]
            temp = temp + "||\n||"
            for y in x:
                temp = temp + y.getDraw().value.split("\n")[2]
            temp = temp + "||\n"
        temp = temp + "|="
        for _ in range(1, self.__mapSize+1):
            temp = temp + "==="
        temp = temp + "=|\n"
        return temp

    def toSave(self):
        temp = []
        temp.append(["mapSize", self.__mapSize])
        temp.append(["mapPos", "[" + str(self.__mapPos[0]) + "," + str(self.__mapPos[1]) + "]"])
        temp.append(["playerPos", "[" + str(self.__playerPos[0]) + "," + str(self.__playerPos[1]) + "]"])
        return temp

    def getSwapTile(self):
        return self.__swapTile

    def getPlayerTile(self):
        return self.__playerTile

    def getAllTiles(self):
        temp = []
        for x in range(1, self.__mapSize+1):
            for y in range(1, self.__mapSize+1):
                temp.append(self.getTile(x, y))
        return temp

    def __checkPos(self, x, y):
        if x < 1 or x > self.__mapSize:
            raise ValueError("Error: X must be greater than 0 and less than " + str(self.__mapSize + 1) + "; X is " + str(x) + "!")
        if y < 1 or y > self.__mapSize:
            raise ValueError("Error: Y must be greater than 0 and less than " + str(self.__mapSize + 1) + "; Y is " + str(y) + "!")

if __name__ == "__main__":
    raise Exception("Error: Class can not be run as main. Must be imported!")