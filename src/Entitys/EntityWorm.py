from src.Entitys.BaseEntity import BaseEntity, HitBox, HitBoxSquare, HitBoxCircle
from src.SubWindow import SubWindow
from src.Utils.Util import Colors
from src.Utils.ColisionUtils import colideCircleSquair, colideSquairs


class Directions:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NONE = 4


class EntityWorm(BaseEntity):
    def __init__(self,aParrent,id):
        self._parrent = aParrent
        self._alive = True
        self._bodyParts = []
        self._direction = Directions.NONE

    def isAlive(self):
        return self._alive

    def moveWorm(self,aAmount):
        pass


class EntityWormBody(BaseEntity):
    def __init__(self,aParrent: SubWindow,aX,aY,aL,aH,aColorBody=Colors.white):
        super().__init__(aX,aY)
        self._l = aL
        self._h = aH
        self._parrent = aParrent
        self._window = aParrent.newChildWindow(aX,aY,aL,aH)
        self._collisionWalls = []
        self._colorBody = aColorBody

    def draw(self):
        self._window.drawBackGround(self._colorBody)

    def reSize(self,aL,aH):
        pass

    def setNewPos(self,aPos):
        pass

    def colide(self,aHitBox):
        hetBoxSelf = HitBoxSquare(self._x, self._y, self._l, self._h)
        type = aHitBox.type
        if type == HitBox.SQUAIR:
            return 270 if colideSquairs(aHitBox,hetBoxSelf) else -1
        elif type == HitBox.CIRCLE:
            return 270 if colideCircleSquair(aHitBox,hetBoxSelf) else -1
        else:
            return -1
