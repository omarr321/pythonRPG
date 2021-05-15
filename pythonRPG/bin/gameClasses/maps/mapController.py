from map import Map
from tile import Tile
from tile import Draw
from tile import Type

#class MapController:
#    pass

print("Creating map...", end="")
temp = Map(0, 0, 10, None)
print("Done!")

print("Setting tiles...", end="")
for x in range(1, 11):
    for y in range(1, 11):
        temp.setTile(x, y, Tile([x, y], Type.PLAIN, Draw.NONE, None))
print("Done!")
print("\nMAP\n")

temp.updateMap(None, None, None, None)

#if __name__ == "__main__":
#    raise Exception("Class can not be run as main. Must be imported!")