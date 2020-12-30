import pygame
from pygame.font import Font

from src.Utils.Util import CenterModes


class SubWindow:
    def __init__(self, aScreen: pygame.Surface, aX, aY, aL, aH):
        self._x = aX
        self._y = aY
        self._l = aL
        self._h = aH
        self._screen = aScreen

    def setNewPos(self,aPos,aMode: CenterModes):# wtrie test
        if aMode == CenterModes.CENTER:
            self._x = aPos[0] - (self._l >> 1)
            self._y = aPos[1] - (self._h >> 1)
        elif aMode == CenterModes.CORNER_LEFT_UP:
            self._x = aPos[0]
            self._y = aPos[1]
        elif aMode == CenterModes.CORNER_LEFT_DOWN:
            self._x = aPos[0]
            self._y = aPos[1] - self._h
        elif aMode == CenterModes.CORNER_RIGHT_UP:
            self._x = aPos[0] - self._l
            self._y = aPos[1]
        elif aMode == CenterModes.CORNER_RIGHT_DOWN:
            self._x = aPos[0] - self._l
            self._y = aPos[1] - self._h

    def getTruePos(self):
        return self._x,self._y

    def drawRect(self, aColor, aX, aY, aL, aH, aW):
        x, y = self.getTrueValidCoords((aX, aY))
        h = self.getTrueValidCoords((aX + aL, aY + aH))
        if x is None or h is None:
            print("attempt to write square out of bounds")
            return
        pygame.draw.rect(self._screen, aColor, (x, y, aL, aH), aW)

    def drawLines(self, aColor, aPointList, aW, aConnect=False):
        validPointList = []
        for point in aPointList:
            tempPoint = self.getTrueValidCoords(point)
            if tempPoint is None:
                print("attempt to write line out of bounds")
                return
            validPointList.append(tempPoint)
        pygame.draw.lines(self._screen, aColor, aConnect, validPointList, aW)

    def drawBackGround(self, aColor):
        self.drawRect(aColor, 0, 0, self._l, self._h, 0)

    def drawText(self, aText, aFont: Font, aColor, aPos, aMode: CenterModes):
        aPos = self.getTrueValidCoords(aPos)
        img = aFont.render(aText, False, aColor)
        aPos = self.repositionImgPos(img,aPos,aMode)
        self._screen.blit(img, aPos)

    def drawBorder(self, aColor, aW):
        self.drawRect(aColor, 0, 0, self._l, self._h, aW)

    def getTrueValidCoords(self, aPos):  # write test
        BLPos = (self._x + self._l, self._y + self._h)
        x = aPos[0] + self._x
        if x > BLPos[0]:
            return None
        y = aPos[1] + self._y
        if y > BLPos[1]:
            return None
        return x, y

    def repositionImgPos(self, aImg: pygame.Surface, aPos, aMode):#write test
        if aMode == CenterModes.CENTER:
            xOffset = aImg.get_width() >> 1
            yOffset = aImg.get_height() >> 1
            return aPos[0]-xOffset, aPos[1] - yOffset
        elif aMode == CenterModes.CORNER_RIGHT_UP:
            xOffset = aImg.get_width()
            return aPos[0]-xOffset,aPos[1]
        elif aMode == CenterModes.CORNER_RIGHT_DOWN:
            xOffset = aImg.get_width()
            yOffset = aImg.get_height()
            return aPos[0]-xOffset,aPos[1]-yOffset
        elif aMode == CenterModes.CORNER_LEFT_UP:
            return aPos
        elif aMode == CenterModes.CORNER_LEFT_DOWN:
            yOffset = aImg.get_height()
            return aPos[0], aPos[1]-yOffset

    def newChildWindow(self, aX, aY, aL, aH):  # write test
        x, y = self.getTrueValidCoords((aX, aY))
        isValid = self.getTrueValidCoords((aX + aL, aY + aH))
        if x is None or isValid is None:
            return None
        return SubWindow(self._screen, x, y, aL, aH)

    def getSize(self):  # write test
        return self._x, self._y, self._l, self._h
