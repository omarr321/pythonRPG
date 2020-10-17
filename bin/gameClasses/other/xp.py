class XP:
    __totalXP = 0
    __levelXP = 0
    __level = 1
    __xp = 0
    __levelCap = 0
    def __init__(self, levelCap=0):
        self.__levelXP = 100
        self.__levelCap = levelCap

    def addXP(self, amount):
        self.__totalXP = int(self.__totalXP + amount)
        self.__xp = int(self.__xp + amount)
        while self.__xp >= self.__levelXP:
            if self.__levelCap == 0:
                print("You leveled up!")
                self.__xp = self.__xp - self.__levelXP
                self.__level = self.__level + 1
                self.__levelXP = int(self.__levelXP + (self.__levelXP/(self.__level*6))*(self.__level))
            else:
                if self.__level != self.__levelCap:
                    print("You leveled up!")
                    self.__xp = self.__xp - self.__levelXP
                    self.__level = self.__level + 1
                    self.__levelXP = int(self.__levelXP + (self.__levelXP/(self.__level*6))*(self.__level))
                else:
                    self.__xp = self.__levelXP
                    break

    def getLevel(self):
        return self.__level

    def getXP(self):
        return self.__xp

    def getLevelXP(self):
        return self.__levelXP

    def toString(self):
        return "Current Level: " + str(self.__level) + "\n" + str(self.__xp) + "\\" + str(self.__levelXP)

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")