import os
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
    def saveAll(self, saveName):
        pass
    
    def loadAll(self, saveName):
        return [self.Load().loadPlayer(saveName), self.Load().loadShop(saveName)]

    class Save:
        def savePlayer(self):
            pass

        def saveShop(self):
            pass
    
        def saveInv(self):
            pass
    
        def saveWeapon(self):
            pass

        def saveArmor(self):
            pass

        def savePotion(self):
            pass

        def saveEffect(self):
            pass

        def writeString(self):
            pass

        def writeRange(self):
            pass
    
    class Load:
        def loadPlayer(self, saveName):
            currPath = os.path.join(saveDir, saveName)
            
            name = self.loadString("name", os.path.join(currPath, "player"), "playerBasic.save")
            money = self.loadString("money", os.path.join(currPath, "player"), "playerBasic.save")
            maxHP = self.loadString("maxHP", os.path.join(currPath, "player"), "playerBasic.save")
            HP = self.loadString("HP", os.path.join(currPath, "player"), "playerBasic.save")


            inv = self.loadInv(saveName, os.path.join(currPath, "player", "playerInv"))
            
            try:
                armor = self.loadItem(saveName, os.path.join(currPath, "player", "playerArmor"), "armor", "armor", solved=True)
                inv.addItem(armor, True)
            except FileNotFoundError:
                armor = None
            
            try:
                weapon = self.loadItem(saveName, os.path.join(currPath, "player", "playerWeapon"), "weapon", "weapon", solved=True)
                inv.addItem(weapon, True)
            except FileNotFoundError:
                weapon = None

            totalXP = self.loadNum("totalXP", os.path.join(currPath, "player"), "playerXP.save")
            levelXP = self.loadNum("levelXP", os.path.join(currPath, "player"), "playerXP.save")
            level = self.loadNum("level", os.path.join(currPath, "player"), "playerXP.save")
            xp = self.loadNum("xp", os.path.join(currPath, "player"), "playerXP.save")
            levelCap = self.loadNum("levelCap", os.path.join(currPath, "player"), "playerXP.save")

            xpp = XP(load=True, tXP=totalXP, lXP=levelXP, level=level, xp=xp, lCap=levelCap)

            return Player(name, load=True, attMod=weapon, defMod=armor, xp=xpp, inv=inv, money=money, maxHP=maxHP, HP=HP)
        
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
                raise Exception("There are no files to choose from!")

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
                    self.loadNumPair(ran, "range", currPath, x)

                    curEffect = Effect(Effect.getStringEffect(temp), ran)
                    if self.loadString("solved", currPath, x) == "true":
                        curEffect.setRandom()
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
            raise Exception("Can not find key \"" + str(key) + "\"!")

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
            raise Exception("Can not find key \"" + str(key) + "\"!")