from enum import Enum, unique

class Tile:
    draw = None
    cords = [-1,-1]
    typee = None
    data = None

    def __init__ (self, cords, typee, draw, data):
        self.cords = cords
        if not(isinstance(typee, Type)):
            raise TypeError("Error: Type is not an instance of the Type class!")
        self.typee = typee
        if not(isinstance(draw, Draw)):
            raise TypeError("Error: Draw is not an instance of the Draw class!")
        self.draw = draw
        self.data = data

    def getData(self):
        return self.data

    def getDraw(self):
        return self.draw

    def getType(self):
        return self.typee

    def getCords(self):
        return self.cords

    def update(self, up, down, left, right):
        if not(isinstance(up, Tile) or up == None):
            raise TypeError("Error: Up parm is not a tile!")
        if not(isinstance(down, Tile) or up == None):
            raise TypeError("Error: Down parm is not a tile!")
        if not(isinstance(left, Tile) or up == None):
            raise TypeError("Error: Left parm is not a tile!")
        if not(isinstance(right, Tile) or up == None):
            raise TypeError("Error: Up parm is not a tile!")
        if self.Type == Type.ROAD:
            pass

@unique
class Type(Enum):
    ROAD = "road"
    PLAIN = "plain"
    BUILDING = "building"
    WILDERNESS = "wilderness"

@unique
class Draw(Enum):
    NONE = "   \n   \n   "
    PLAYER = " O \n/|\\\n ᐱ "
    SHOP = " _ \n/S\\\n|_|"
    TREE = " _ \n/|\\\n‾|‾"
    ROAD_DEAD_END_UP = " | \n | \n   "
    ROAD_DEAD_END_DOWN = "   \n | \n | "
    ROAD_DEAD_END_LEFT = "   \n-- \n   "
    ROAD_DEAD_END_RIGHT = "   \n --\n   "
    ROAD_STRAIGHT_DOWN = " | \n | \n | "
    ROAD_STRAIGHT_SIDE = "   \n---\n   "
    ROAD_TOP_LEFT = " | \n-| \n   "
    ROAD_TOP_RIGHT = " | \n |-\n   "
    ROAD_BOTTOM_LEFT = "   \n-| \n | "
    ROAD_BOTTOM_RIGHT = "   \n |-\n | "
    ROAD_T_JUNC_UP = " | \n-|-\n   "
    ROAD_T_JUNC_DOWN = "   \n-|-\n | "
    ROAD_T_JUNC_LEFT = " | \n-| \n | "
    ROAD_T_JUNC_RIGHT = " | \n |-\n | "
    ROAD_FOUR_WAY = " | \n-|-\n | "

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")