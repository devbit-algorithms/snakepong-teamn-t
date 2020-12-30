from src.Entitys.BaseEntity import BaseEntity
from src.SubWindow import SubWindow
from src.Utils.Util import Colors


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


class EntityColisionWall(BaseEntity):
    def __init__(self,aX,aY,aL,aH):
        self._x = aX
        self._y = aY
        self._l = aL
        self._h = aH

    def colide(self,aEntity):
