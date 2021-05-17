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


class GameDataController:
    class Save:
        @staticmethod
        def savePlayer(saveDir, player):
            currDir = saveDir

            GameDataController.Save.writeString(currDir, "playerBasic.save", "name", player.getName())
            GameDataController.Save.writeString(currDir, "playerBasic.save", "money", player.getMoney())
            GameDataController.Save.writeString(currDir, "playerBasic.save", "maxHP", player.getMaxHealth())
            GameDataController.Save.writeString(currDir, "playerBasic.save", "HP", player.getHealth())

            temp = player.getXP()
            GameDataController.Save.writeString(currDir, "playerXP.save", "totalXP", temp.getTotalXP())
            GameDataController.Save.writeString(currDir, "playerXP.save", "levelXP", temp.getLevelXP())
            GameDataController.Save.writeString(currDir, "playerXP.save", "level", temp.getLevel())
            GameDataController.Save.writeString(currDir, "playerXP.save", "xp", temp.getXP())
            GameDataController.Save.writeString(currDir, "playerXP.save", "levelCap", temp.getLevelCap())

            if not (player.getDefMod() is None):
                GameDataController.Save.saveItem(os.path.join(currDir, "playerArmor"), "armor", "armor",
                                                 player.getDefMod())

            if not (player.getAttMod() is None):
                GameDataController.Save.saveItem(os.path.join(currDir, "playerWeapon"), "weapon", "weapon",
                                                 player.getAttMod())

            GameDataController.Save.saveInv(os.path.join(currDir, "playerInv"), player.getInv())

        @staticmethod
        def saveShop(saveDir, shop):
            currDir = saveDir
            os.makedirs(os.path.join(currDir, "shopInv"))
            GameDataController.Save.writeString(currDir, "shopBasic.save", "name", shop.getName())
            GameDataController.Save.saveInv(os.path.join(currDir, "shopInv"), shop.getInv())

        @staticmethod
        def saveInv(path, inv):
            number = 1
            for x in inv.toSave():
                if x[0] == 0:
                    GameDataController.Save.saveItem(path, "item" + str(number), "weapon", x[1])
                elif x[0] == 1:
                    GameDataController.Save.saveItem(path, "item" + str(number), "armor", x[1])
                elif x[0] == 2:
                    GameDataController.Save.saveItem(path, "item" + str(number), "potion", x[1])
                number = number + 1

        @staticmethod
        def saveItem(path, fileName, ext, item):
            temp = item.toSave()
            for x in temp:
                if x[0] == 0:
                    GameDataController.Save.writeString(path, fileName + "." + ext, x[1], x[2])
                elif x[0] == 1:
                    GameDataController.Save.writeRange(path, fileName + "." + ext, x[1], x[2][0], x[2][1])
                elif x[0] == 2:
                    effects = x[2]
                    number = 1
                    for y in effects:
                        temp = fileName + "Effect" + str(number)
                        GameDataController.Save.saveEffect(path, temp, ext, y)
                        number = number + 1

        @staticmethod
        def saveEffect(path, fileName, ext, effect):
            temp = effect.toSave()

            for x in temp:
                if x[0] == 0:
                    GameDataController.Save.writeString(path, fileName + "." + ext, x[1], x[2])
                elif x[0] == 1:
                    GameDataController.Save.writeRange(path, fileName + "." + ext, x[1], x[2][0], x[2][1])

        @staticmethod
        def writeString(path, fileName, key, value):
            ffile = open(os.path.join(path, fileName), "a+")
            ffile.write(key + ":" + str(value) + "\n")
            ffile.close()

        @staticmethod
        def writeRange(path, fileName, key, mmin, mmax):
            ffile = open(os.path.join(path, fileName), "a+")
            ffile.write(key + ":[" + str(mmin) + "-" + str(mmax) + "]\n")
            ffile.close()

    class Load:
        @staticmethod
        def loadPlayer(path):
            currPath = path

            name = GameDataController.Load.loadString("name", os.path.join(currPath, "player"), "playerBasic.save")
            money = GameDataController.Load.loadString("money", os.path.join(currPath, "player"), "playerBasic.save")
            maxHP = GameDataController.Load.loadString("maxHP", os.path.join(currPath, "player"), "playerBasic.save")
            HP = GameDataController.Load.loadString("HP", os.path.join(currPath, "player"), "playerBasic.save")

            inv = GameDataController.Load.loadInv(os.path.join(currPath, "playerInv"))

            try:
                armor = GameDataController.Load.loadItem(os.path.join(currPath, "playerArmor"), "armor", "armor",
                                                         solved=True)
                inv.addItem(armor, True)
            except FileNotFoundError:
                armor = None

            try:
                weapon = GameDataController.Load.loadItem(os.path.join(currPath, "playerWeapon"), "weapon", "weapon",
                                                          solved=True)
                inv.addItem(weapon, True)
            except FileNotFoundError:
                weapon = None

            totalXP = GameDataController.Load.loadNum("totalXP", os.path.join(currPath, "player"), "playerXP.save")
            levelXP = GameDataController.Load.loadNum("levelXP", os.path.join(currPath, "player"), "playerXP.save")
            level = GameDataController.Load.loadNum("level", os.path.join(currPath, "player"), "playerXP.save")
            xp = GameDataController.Load.loadNum("xp", os.path.join(currPath, "player"), "playerXP.save")
            levelCap = GameDataController.Load.loadNum("levelCap", os.path.join(currPath, "player"), "playerXP.save")

            xpp = XP(load=True, tXP=totalXP, lXP=levelXP, level=level, xp=xp, lCap=levelCap)

            return Player(name, load=True, attMod=weapon, defMod=armor, xp=xpp, inv=inv, money=money, maxHP=maxHP,
                          HP=HP)

        @staticmethod
        def loadShop(path):
            currPath = path
            name = GameDataController.Load.loadString("name", os.path.join(currPath, "shop"), "shopBasic.save")
            inv = GameDataController.Load.loadInv(path)
            return Shop(load=True, name=name, inv=inv)

        @staticmethod
        def loadInv(path):
            currPath = path

            items = list()
            (_, _, files) = next(os.walk(currPath))
            regex = re.compile('Effect[1-9]{1}([0-9]{0,})')
            for x in files:
                if not regex.search(x):
                    items.append(x)
            if len(files) == 0:
                return Inv()

            temp = Inv()

            for x in items:
                temp.addItem(GameDataController.Load.loadItem(path, x.split(".")[0], x.split(".")[1], solved=True))

            return temp

        @staticmethod
        def loadItem(path, itemName, itemExt, solved=False):
            currPath = path

            name = GameDataController.Load.loadString("name", currPath, itemName + "." + itemExt)
            desc = GameDataController.Load.loadString("desc", currPath, itemName + "." + itemExt)
            cost = [0, 0]
            if solved:
                cost = GameDataController.Load.loadNum("cost", currPath, itemName + "." + itemExt)
            else:
                GameDataController.Load.loadNumPair(cost, "cost", currPath, itemName + "." + itemExt)
            effects = GameDataController.Load.loadEffects(currPath, itemName, itemExt)
            if itemExt == "potion":
                return Potion(load=True, name=name, desc=desc, cost=cost, effects=effects)
            elif itemExt == "armor":
                return Armor(load=True, name=name, desc=desc, cost=cost, effects=effects)
            elif itemExt == "weapon":
                return Weapon(load=True, name=name, desc=desc, cost=cost, effects=effects)

        @staticmethod
        def loadEffects(path, objName, objExt):
            currPath = path
            (_, _, files) = next(os.walk(currPath))
            effects = list()

            temp = str(objName) + "Effect"
            regex = re.compile('^' + temp + '[1-9]{1}([0-9]{0,}).' + objExt + '$')
            for x in files:
                if regex.match(x):
                    temp = GameDataController.Load.loadString("type", currPath, x)
                    ran = [0, 0]

                    if GameDataController.Load.loadString("solved", currPath, x) == "true":
                        ran = GameDataController.Load.loadNum("range", currPath, x)
                    else:
                        GameDataController.Load.loadNumPair(ran, "range", currPath, x)

                    curEffect = Effect(Effect.getStringEffect(temp), ran, True)
                    effects.append(curEffect)
            return effects

        @staticmethod
        def loadString(key, path, fileName):
            f = open(os.path.join(path, fileName))
            for line in f:
                if line.startswith(key + ":"):
                    temp = line.split(":")
                    f.close()
                    return temp[1].rstrip()
            f.close()
            raise KeyError("Can not find key \"" + str(key) + "\"!")

        @staticmethod
        def loadNum(key, path, fileName):
            temp = GameDataController.Load.loadString(key, path, fileName)
            try:
                temp = int(temp)
            except ValueError:
                raise ValueError("Value is not a number!")
            return temp

        @staticmethod
        def loadNumPair(arr, key, path, fileName):
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
