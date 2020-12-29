import pygame


class SubWindow:
    def __init__(self,aScreen,aX,aY,aL,aH):
        self._x = aX
        self._y = aY
        self._l = aL
        self._h = aH
        self._screen = aScreen

    def rect(self,aColor,aX,aY,aH,aL,aW):
        x,y = self.getTrueValidCoords((aX,aY))
        h = self.getTrueValidCoords((aX+aL,aY+aH))
        if x is None or h is None:
            print("attempt to write square out of bounds")
            return
        pygame.draw.rect(self._screen,aColor,(x,y,aL,aH),aW)

    def lines(self,aColor,aPointList,aW,aConnect=False):
        validPointList = []
        for point in aPointList:
            tempPoint = self.getTrueValidCoords(point)
            if tempPoint is None:
                print("attempt to write line out of bounds")
                return
            validPointList.append(tempPoint)
        pygame.draw.lines(self._screen,aColor,aConnect,validPointList,aW)

    def getTrueValidCoords(self,aPos):#write test
        BLPos = (self._x + self._l,self._y + self._h)
        x = aPos[0] + self._x
        if x > BLPos[0]:
            return None
        y = aPos[1] + self._y
        if y > BLPos[1]:
            return None
        return x,y

    def newChildWindow(self,aX,aY,aL,aH):#write test
        x,y = self.getTrueValidCoords((aX,aY))
        isValid = self.getTrueValidCoords((aX+aL,aY+aH))
        if x is None or isValid is None:
            return None
        return SubWindow(self._screen,x,y,aL,aH)

    def getSize(self):
        return self._x, self._y, self._l, self._h