from src.Entitys.BaseEntity import BaseEntity, HitBox, HitBoxSquare, Directions
from src.SubWindow import SubWindow,CenterModes
from src.Utils.Util import Colors
from src.Utils.ColisionUtils import colideCircleSquair, colideSquairs
import pygame


class EntityWormBody(BaseEntity):
    def __init__(self,aParrent: SubWindow,aX,aY,aL,aH,aDirection,aColorBody=Colors.white):
        super().__init__(aX,aY)
        self._l = aL
        self._h = aH
        self._parrent = aParrent
        self._window = aParrent.newChildWindow(aX,aY,aL,aH)
        self._collisionWalls = []
        self._colorBody = aColorBody
        self._direction: Directions = aDirection

    def draw(self):
        self._window.drawBackGround(self._colorBody)

    def reSize(self,aL,aH):
        self._l = aL
        self._h = aH
        self._window.reSize(aL,aH)

    def getDirection(self):
        return self._direction

    def setNewPos(self,aPos):
        x = aPos[0]
        y = aPos[1]
        self._x = x
        self._y = y
        x,y = self._parrent.getTrueValidCoords((x,y))
        self._window.setNewPos((x,y),CenterModes.CORNER_LEFT_UP)

    def getPos(self):
        return self._x,self._y

    def colide(self,aHitBox):
        hetBoxSelf = HitBoxSquare(self._x, self._y, self._l, self._h)
        tType = aHitBox.type
        if tType == HitBox.SQUAIR:
            return 270 if colideSquairs(aHitBox,hetBoxSelf) else -1
        elif tType == HitBox.CIRCLE:
            return 270 if colideCircleSquair(aHitBox,hetBoxSelf) else -1
        else:
            return -1

    def getLength(self):
        if self._direction == Directions.NORTH or self._direction == Directions.SOUTH:
            return self._h
        else:
            return self._l

    def setLength(self,aAmount):
        if self._direction == Directions.NORTH or self._direction == Directions.SOUTH:
            self.reSize(self._l, aAmount)
        else:
            self.reSize(aAmount, self._h)


class EntityWorm(BaseEntity):
    def __init__(self,aParrent,aX,aY,aWith,aSize,aSpeed):
        super().__init__(aX,aY)
        self._parrent = aParrent
        self._alive = True
        self._bodyParts = []
        self._speed = aSpeed
        self._direction = Directions.NORTH
        self._with = aWith
        self._bodyParts.append(EntityWormBody(aParrent,aX,aY,aWith,aSize,Directions.NORTH))

    def update(self):
        key = pygame.key.get_pressed()
        turnDirection = Directions.NONE
        if key[pygame.K_w]:
            turnDirection = Directions.NORTH
        elif key[pygame.K_d]:
            turnDirection = Directions.EAST
        elif key[pygame.K_s]:
            turnDirection = Directions.SOUTH
        elif key[pygame.K_a]:
            turnDirection = Directions.WEST
        if turnDirection != Directions.NONE:
            if self.canTurn(turnDirection):
                self._direction = turnDirection

        self.moveWorm(self._speed)

    def isAlive(self):
        return self._alive

    def canTurn(self, aDirection: Directions):
        direction = self._direction
        return direction != aDirection and (direction + 2) % 4 != aDirection

    def turnWorm(self,aDirection: Directions,initialSize, oldHead: EntityWormBody):
        newBody = None
        oldDirection = oldHead.getDirection()
        offset = 0
        if oldDirection == Directions.SOUTH or oldDirection == Directions.EAST:
            offset += 1
        if aDirection == Directions.NORTH:
            newBody = EntityWormBody(self._parrent, self._x + offset, self._y - initialSize, self._with,
                                     self._with + initialSize, aDirection)
        elif aDirection == Directions.SOUTH:
            newBody = EntityWormBody(self._parrent, self._x + offset, self._y, self._with,
                                     self._with + initialSize, aDirection)
        elif aDirection == Directions.EAST:
            newBody = EntityWormBody(self._parrent, self._x, self._y + offset, self._with + initialSize,
                                     self._with, aDirection)
        elif aDirection == Directions.WEST:
            newBody = EntityWormBody(self._parrent, self._x - initialSize, self._y + offset,
                                     self._with + initialSize, self._with, aDirection)
        self._bodyParts.insert(0,newBody)
        self._x, self._y = newBody.getPos()

    def moveWorm(self,aAmount):
        toMove = self.moveEntityDirection(aAmount,self._direction,self._parrent)
        firstBody = self._bodyParts[0]
        if firstBody.getDirection() != self._direction:
            self.turnWorm(self._direction,aAmount,firstBody)
        else:
            self.increaseSize(aAmount,firstBody)
        while toMove > 0:
            toMove = self.reduceBehind(toMove)

    def reduceBehind(self, aAmount):
        amountBodyIndex = len(self._bodyParts) - 1
        lastBody = self._bodyParts[amountBodyIndex]
        length = lastBody.getLength()
        if length < aAmount:
            aAmount -= length
            self._bodyParts.pop(amountBodyIndex)
            return aAmount
        else:
            lastBody.setLength(length-aAmount)
            return 0

    def increaseSize(self, aAmount, aBody: EntityWormBody):
        aBody.setLength(aBody.getLength() + aAmount)
        direction = aBody.getDirection()
        if direction == Directions.NORTH:
            x, y = aBody.getPos()
            aBody.setNewPos((x,y-aAmount))
        elif direction == Directions.WEST:
            x, y = aBody.getPos()
            aBody.setNewPos((x-aAmount,y))

    def draw(self):
        for body in self._bodyParts:
            body.draw()
