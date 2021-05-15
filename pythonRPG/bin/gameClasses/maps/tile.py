from enum import Enum, unique

class Tile:
    __draw = None
    __cords = [-1,-1]
    __typee = None
    __data = None

    def __init__ (self, cords, typee, draw, data):
        self.__cords = cords
        if not(isinstance(typee, Type)):
            raise TypeError("Error: Type is not an instance of the Type class!")
        self.__typee = typee
        if not(isinstance(draw, Draw)):
            raise TypeError("Error: Draw is not an instance of the Draw class!")
        self.__draw = draw
        self.__data = data

    def getData(self):
        return self.__data

    def getDraw(self):
        return self.__draw

    def getType(self):
        return self.__typee

    def getCords(self):
        return self.__cords

    def update(self, up, down, left, right):
        if not(isinstance(up, Tile)):
            raise TypeError("Error: Up parm is not a tile!")
        if not(isinstance(down, Tile)):
            raise TypeError("Error: Down parm is not a tile!")
        if not(isinstance(left, Tile)):
            raise TypeError("Error: Left parm is not a tile!")
        if not(isinstance(right, Tile)):
            raise TypeError("Error: Up parm is not a tile!")
            
        if self.__Type == Type.ROAD:
            if not(up.getType() == Type.ROAD) and not(down.getType() == Type.ROAD) and not(left.getType() == Type.ROAD) and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_DEAD_END_NOWAY
            elif up.getType() == Type.ROAD and not(down.getType() == Type.ROAD) and not(left.getType() == Type.ROAD) and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_DEAD_END_UP
            elif not(up.getType() == Type.ROAD) and down.getType() == Type.ROAD and not(left.getType() == Type.ROAD) and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_DEAD_END_DOWN
            elif not(up.getType() == Type.ROAD) and not(down.getType() == Type.ROAD) and left.getType() == Type.ROAD and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_DEAD_END_LEFT
            elif not(up.getType() == Type.ROAD) and not(down.getType() == Type.ROAD) and not(left.getType() == Type.ROAD) and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_DEAD_END_RIGHT
            elif up.getType() == Type.ROAD and down.getType() == Type.ROAD and not(left.getType() == Type.ROAD) and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_STRAIGHT_DOWN
            elif not(up.getType() == Type.ROAD) and down.getType() == Type.ROAD and left.getType() == Type.ROAD and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_BOTTOM_LEFT
            elif not(up.getType() == Type.ROAD) and not(down.getType() == Type.ROAD) and left.getType() == Type.ROAD and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_STRAIGHT_SIDE
            elif up.getType() == Type.ROAD and not(down.getType() == Type.ROAD) and left.getType() == Type.ROAD and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_TOP_LEFT
            elif not(up.getType() == Type.ROAD) and down.getType() == Type.ROAD and not(left.getType() == Type.ROAD) and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_BOTTOM_RIGHT
            elif up.getType() == Type.ROAD and not(down.getType() == Type.ROAD) and not(left.getType() == Type.ROAD) and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_TOP_RIGHT
            elif up.getType() == Type.ROAD and down.getType() == Type.ROAD and left.getType() == Type.ROAD and not(right.getType() == Type.ROAD):
                self.__draw = Draw.ROAD_T_JUNC_LEFT
            elif not(up.getType() == Type.ROAD) and down.getType() == Type.ROAD and left.getType() == Type.ROAD and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_T_JUNC_DOWN
            elif up.getType() == Type.ROAD and down.getType() == Type.ROAD and not(left.getType() == Type.ROAD) and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_T_JUNC_RIGHT
            elif up.getType() == Type.ROAD and not(down.getType() == Type.ROAD) and left.getType() == Type.ROAD and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_T_JUNC_UP
            elif up.getType() == Type.ROAD and down.getType() == Type.ROAD and left.getType() == Type.ROAD and right.getType() == Type.ROAD:
                self.__draw = Draw.ROAD_FOUR_WAY
            
        else:
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
    ROAD_DEAD_END_NOWAY = "   \n + \n   "
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