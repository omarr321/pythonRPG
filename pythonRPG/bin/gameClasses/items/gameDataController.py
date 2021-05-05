
class GameDataController:
    def saveAll(self):
        pass
    
    def loadAll(self):
        pass

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
            pass
        
        def loadShop(self, saveName):
            pass

        def loadInv(self, saveName, path):
            pass

        def loadWeapon(self, saveName, path, weaponName):
            pass
        
        def loadArmor(self, saveName, path, armorName):
            pass

        def loadPotion(self, saveName, path, potionName):
            pass

        def loadEffects(self, saveName, path, objName):
            pass

        def loadString(self, key, path, fileName):
            f = open(os.path.join(path, fileName))
            for line in f:
                if line.startswith(key + ":"):
                    temp = line.split(":")
                    f.close()
                    return temp[1].rstrip()
            f.close()
            raise Exception("Can not find key \"" + str(key) + "\"!")

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