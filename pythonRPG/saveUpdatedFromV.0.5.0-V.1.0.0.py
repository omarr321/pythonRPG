#!/usr/bin/env python3

import pickle
import os
import sys

currWorkDir = os.path.dirname(__file__)
currWorkDir = os.path.join(currWorkDir, "bin", "saves")

shop = None
player = None

print("Welcome to save file updater!")
print("\nThis file will update save versions 0.5.0 to saves version 1.0.0.")
print("Type anything to contine...")
input()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("What is the name of the save?")
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
    print("(1/3)Loading old save game...", end="")
    shop = pickle.load(open(os.path.join(currWorkDir, temp + "Shop.save"), "rb"))
    player = pickle.load(open(os.path.join(currWorkDir, temp + "Player.save"), "rb"))
    print("Done!")
except FileNotFoundError:
    print("Error: There is no save file with that name!")
    print("Type anything to contine...", end="")
    input()
    print("Goodbye!")
    exit(1)
except pickle.UnpicklingError:
    print("Error: There was a problem loading the save files!")
    print("Type anything to contine...", end="")
    input()
    print("Goodbye!")
    exit(1)

print("(2/3)Converting to new save format...", end="")
GameDataController.saveAll(temp, player, shop)
print("Done!")

print("(3/3)Deleting old save...", end="")
os.remove(os.path.join(currWorkDir, temp + "Shop.save"))
os.remove(os.path.join(currWorkDir, temp + "Player.save"))
print("Done!")

print("Type anything to contine...", end="")
input()
print("Goodbye!")
exit(1)

class GameDataController:
    def saveAll(self, saveName, player, shop):
        currDir = os.path.join(saveDir, saveName)
        if os.path.exists(currDir):
            shutil.rmtree(currDir)
        os.makedirs(currDir)

        os.makedirs(os.path.join(currDir, "player"))
        os.makedirs(os.path.join(currDir, "player", "playerArmor"))
        os.makedirs(os.path.join(currDir, "player", "playerInv"))
        os.makedirs(os.path.join(currDir, "player", "playerWeapon"))
        
        os.makedirs(os.path.join(currDir, "shop"))
        os.makedirs(os.path.join(currDir, "shop", "shopInv"))

        self.__Save().savePlayer(saveName, player)
        self.__Save().saveShop(saveName, shop)

    class __Save:
        def savePlayer(self, saveName, player):
            currDir = os.path.join(saveDir, saveName, "player")

            self.writeString(currDir, "playerBasic.save", "name", player.getName())
            self.writeString(currDir, "playerBasic.save", "money", player.getMoney())
            self.writeString(currDir, "playerBasic.save", "maxHP", player.getMaxHealth())
            self.writeString(currDir, "playerBasic.save", "HP", player.getHealth())

            temp = player.getXP()
            self.writeString(currDir, "playerXP.save", "totalXP", temp.getTotalXP())
            self.writeString(currDir, "playerXP.save", "levelXP", temp.getLevelXP())
            self.writeString(currDir, "playerXP.save", "level", temp.getLevel())
            self.writeString(currDir, "playerXP.save", "xp", temp.getXP())
            self.writeString(currDir, "playerXP.save", "levelCap", temp.getLevelCap())

            if not(player.getDefMod() == None):
                self.saveItem(os.path.join(currDir, "playerArmor"), "armor", "armor", player.getDefMod())

            if not(player.getAttMod() == None):
                self.saveItem(os.path.join(currDir, "playerWeapon"), "weapon", "weapon", player.getAttMod())

            self.saveInv(os.path.join(currDir, "playerInv"), player.getInv())

        def saveShop(self, saveName, shop):
            currDir = os.path.join(saveDir, saveName, "shop")
            self.writeString(currDir, "shopBasic.save", "name", shop.getName())
            self.saveInv(os.path.join(currDir, "shopInv"), shop.getInv())

    
        def saveInv(self, path, inv):
            number = 1
            for x in inv.toSave():
                if x[0] == 0:
                    self.saveItem(path, "item" + str(number), "weapon", x[1])
                elif x[0] == 1:
                    self.saveItem(path, "item" + str(number), "armor", x[1])
                elif x[0] == 2:
                    self.saveItem(path, "item" + str(number), "potion", x[1])
                number = number + 1

        def saveItem(self, path, fileName, ext, item):
            temp = item.toSave()
            for x in temp:
                if x[0] == 0:
                    self.writeString(path, fileName + "." + ext, x[1], x[2])
                elif x[0] == 1:
                    self.writeRange(path, fileName + "." + ext, x[1], x[2][0], x[2][1])
                elif x[0] == 2:
                    effects = x[2]
                    number = 1
                    for y in effects:
                        temp = fileName + "Effect" + str(number)
                        self.saveEffect(path, temp, ext, y)
                        number = number + 1

        def saveEffect(self, path, fileName, ext, effect):
            temp = effect.toSave()

            for x in temp:
                if x[0] == 0:
                    self.writeString(path, fileName + "." + ext, x[1], x[2])
                elif x[0] == 1:
                    self.writeRange(path, fileName + "." + ext, x[1], x[2][0], x[2][1])

        def writeString(self, path, fileName, key, value):
            ffile = open(os.path.join(path, fileName), "a+")
            ffile.write(key + ":" + str(value) + "\n")
            ffile.close()


        def writeRange(self, path, fileName, key, mmin, mmax):
            ffile = open(os.path.join(path, fileName), "a+")
            ffile.write(key + ":[" + str(mmin) + "-" + str(mmax) + "]\n")
            ffile.close()

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")