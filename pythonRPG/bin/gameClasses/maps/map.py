class Map:
    __mapSize = -1
    __mapGrid = None
    __mapPos = [-1, -1]
    __swapTile = None

    __playerPos = [-1, -1]
    __playerTile = None

    def __init__(self, mapX, mapY, mapSize, player):
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

    def getTile(self, x, y):
        self.__checkPos(x, y)
        return self.__mapGrid[x-1][y-1]

    def getPlayer(self):
        return self.__playerTile

    def getMapPos(self):
        return self.__mapPos

    def getMapSize(self):
        return self.__mapSize

    def getPlayerPos(self):
        return self.__playerPos

    def setPlayerPos(self, x, y):
        self.__checkPos(x, y)
        if not(self.__playerPos == (-1, -1)):
            self.__mapGrid[self.__playerPos[0]][self.__mapGrid[1]] = self.__swapTile
        self.__swapTile = self.__mapGrid[x-1][y-1]
        self.__mapGrid[x][y] = self.__playerTile

    def setTile(self, x, y, tile):
        self.__checkPos(x, y)
        self.__mapGrid[x-1][y-1] = tile

    def updateMap(self, upRow, bottomRow, leftRow, rightRow):
        for a in self.__mapGrid:
            for b in a:
                print(str(b.getCords()), end="")
            print()

    def __checkPos(self, x, y):
        if x < 1 or x > self.__mapSize:
            raise ValueError("Error: x must be greater than 0 and less than " + str(self.mapSize + 1))
        if y < 1 or y > self.__mapSize:
            raise ValueError("Error: y must be greater than 0 and less than " + str(self.mapSize + 1))

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")