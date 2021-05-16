import os
import shutil
import random
import re
from .armor import Armor
from .weapon import Weapon
from .potion import Potion
from .effect import Effect
from .effect import EffectStatus
from ..entities import Shop
from ..entities import Player
from ..other import Inv
from ..other import XP

saveDir = os.path.join(os.path.split(os.path.split(os.path.dirname(__file__))[0])[0], "saves")


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

    def loadAll(self, saveName):
        return [self.__Load().loadPlayer(saveName), self.__Load().loadShop(saveName)]

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

            if not (player.getDefMod() == None):
                self.saveItem(os.path.join(currDir, "playerArmor"), "armor", "armor", player.getDefMod())

            if not (player.getAttMod() == None):
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

    class __Load:
        def loadPlayer(self, saveName):
            currPath = os.path.join(saveDir, saveName)

            name = self.loadString("name", os.path.join(currPath, "player"), "playerBasic.save")
            money = self.loadString("money", os.path.join(currPath, "player"), "playerBasic.save")
            maxHP = self.loadString("maxHP", os.path.join(currPath, "player"), "playerBasic.save")
            HP = self.loadString("HP", os.path.join(currPath, "player"), "playerBasic.save")

            inv = self.loadInv(saveName, os.path.join(currPath, "player", "playerInv"))

            try:
                armor = self.loadItem(saveName, os.path.join(currPath, "player", "playerArmor"), "armor", "armor",
                                      solved=True)
                inv.addItem(armor, True)
            except FileNotFoundError:
                armor = None

            try:
                weapon = self.loadItem(saveName, os.path.join(currPath, "player", "playerWeapon"), "weapon", "weapon",
                                       solved=True)
                inv.addItem(weapon, True)
            except FileNotFoundError:
                weapon = None

            totalXP = self.loadNum("totalXP", os.path.join(currPath, "player"), "playerXP.save")
            levelXP = self.loadNum("levelXP", os.path.join(currPath, "player"), "playerXP.save")
            level = self.loadNum("level", os.path.join(currPath, "player"), "playerXP.save")
            xp = self.loadNum("xp", os.path.join(currPath, "player"), "playerXP.save")
            levelCap = self.loadNum("levelCap", os.path.join(currPath, "player"), "playerXP.save")

            xpp = XP(load=True, tXP=totalXP, lXP=levelXP, level=level, xp=xp, lCap=levelCap)

            return Player(name, load=True, attMod=weapon, defMod=armor, xp=xpp, inv=inv, money=money, maxHP=maxHP,
                          HP=HP)

        def loadShop(self, saveName):
            currPath = os.path.join(saveDir, saveName)
            name = self.loadString("name", os.path.join(currPath, "shop"), "shopBasic.save")
            inv = self.loadInv(saveName, os.path.join(currPath, "shop", "shopInv"))
            return Shop(load=True, name=name, inv=inv)

        def loadInv(self, saveName, path):
            currPath = os.path.join(saveDir, saveName, path)

            items = list()
            (_, _, files) = next(os.walk(currPath))
            regex = re.compile('Effect[1-9]{1}([0-9]{0,})')
            for x in files:
                if not regex.search(x):
                    items.append(x)
            if len(files) == 0:
                return

            temp = Inv()

            for x in items:
                temp.addItem(self.loadItem(saveName, path, x.split(".")[0], x.split(".")[1], solved=True))

            return temp

        def loadItem(self, saveName, path, itemName, itemExt, solved=False):
            currPath = os.path.join(saveDir, saveName, path)

            name = self.loadString("name", currPath, itemName + "." + itemExt)
            desc = self.loadString("desc", currPath, itemName + "." + itemExt)
            cost = [0, 0]
            if solved:
                cost = self.loadNum("cost", currPath, itemName + "." + itemExt)
            else:
                self.loadNumPair(cost, "cost", currPath, itemName + "." + itemExt)
            effects = self.loadEffects(saveName, currPath, itemName, itemExt)
            if itemExt == "potion":
                return Potion(load=True, name=name, desc=desc, cost=cost, effects=effects)
            elif itemExt == "armor":
                return Armor(load=True, name=name, desc=desc, cost=cost, effects=effects)
            elif itemExt == "weapon":
                return Weapon(load=True, name=name, desc=desc, cost=cost, effects=effects)

        def loadEffects(self, saveName, path, objName, objExt):
            currPath = os.path.join(saveDir, saveName, path)
            (_, _, files) = next(os.walk(currPath))
            effects = list()

            temp = str(objName) + "Effect"
            regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).' + objExt + '$')
            for x in files:
                if regex.match(x):
                    temp = self.loadString("type", currPath, x)
                    ran = [0, 0]

                    if self.loadString("solved", currPath, x) == "true":
                        ran = self.loadNum("range", currPath, x)
                    else:
                        self.loadNumPair(ran, "range", currPath, x)

                    curEffect = Effect(Effect.getStringEffect(temp), ran, True)
                    effects.append(curEffect)
            return effects

        def loadString(self, key, path, fileName):
            f = open(os.path.join(path, fileName))
            for line in f:
                if line.startswith(key + ":"):
                    temp = line.split(":")
                    f.close()
                    return temp[1].rstrip()
            f.close()
            raise KeyError("Can not find key \"" + str(key) + "\"!")

        def loadNum(self, key, path, fileName):
            temp = self.loadString(key, path, fileName)
            try:
                temp = int(temp)
            except ValueError:
                raise ValueError("Value is not a number!")
            return temp

        def loadNumPair(self, arr, key, path, fileName):
            f = open(os.path.join(path, fileName))
            for line in f:
                if line.startswith(key + ":"):
                    temp = line.split(":")
                    try:
                        temp = temp[1].split("[")
                        temp = temp[1].split("]")
                        temp = temp[0].split("-")
                        arr[0] = int(temp[0])
                        arr[1] = int(temp[1])
                        f.close()
                        return
                    except ValueError:
                        f.close()
                        raise ValueError("Value is not a number pair!")
                    except IndexError:
                        f.close()
                        raise ValueError("Value is not a number pair!")
            f.close()
            raise KeyError("Can not find key \"" + str(key) + "\"!")
