from src.SubWindow import SubWindow

class Directions:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NONE = 4


class BaseEntity:
    def __init__(self,aX,aY):
        self._x = aX
        self._y = aY

    def draw(self):
        pass

    def update(self):
        pass

    def isAlive(self):
        return False

    def kill(self):
        pass

    def hasColision(self):
        return False

    def colide(self,aEntity):
        return -1

    def moveEntityDirection(self,aAmount,aDirection: Directions,aWindow: SubWindow=None):
        hasWindow = False
        if aWindow is not None:
            x,y,xMax,yMax = aWindow.getSize()
            hasWindow = True
            yOld = self._y
            xOld = self._x
        if aDirection == Directions.NORTH:
            self._y -= aAmount
            if hasWindow and self._y < 0:
                self._y = 0
                aAmount = abs(yOld)
            return aAmount
        elif aDirection == Directions.SOUTH:
            self._y += aAmount
            if hasWindow and self._y > yMax:
                self._y = yMax
                aAmount = abs(self._y-yOld)
            return aAmount
        elif aDirection == Directions.EAST:
            self._x += aAmount
            if hasWindow and self._x > xMax:
                self._x = xMax
                aAmount = abs(self._x-xOld)
            return aAmount
        elif aDirection == Directions.WEST:
            self._x -= aAmount
            if hasWindow and self._x < 0:
                self._x = 0
                aAmount = abs(xOld)
            return aAmount


class HitBox:
    def __init__(self):
        self.type = None
    SQUAIR = 0
    CIRCLE = 1


class HitBoxSquare(HitBox):
    def __init__(self,aX,aY,aL,aH):
        super().__init__(HitBox.SQUAIR)
        self.X = aX
        self.Y = aY
        self.L = aL
        self.H = aH


class HitBoxCircle(HitBox):
    def __init__(self,aX,aY,aSize):
        super().__init__(HitBox.CIRCLE)
        self.X = aX
        self.Y = aY
        self.size = aSize
