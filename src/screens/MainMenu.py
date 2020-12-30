from src.screens.BaseScreen import BaseScreen
from src.SubWindow import SubWindow
from src.button.NormalButton import NormalButton
from src.Utils.Util import calcuateOffset,CenterModes
from src.Statics import Input
import pygame



class MainMenu(BaseScreen):
    def __init__(self, aParrent: SubWindow):
        x,y,l,h = aParrent.getSize()
        self._window = aParrent.newChildWindow(x,y,l,h)
        self._parrent = aParrent
        self._buttons = []
        xOffset = calcuateOffset(80,l,0,1,CenterModes.DOWN)
        yOffset = calcuateOffset(40,h,0,2,CenterModes.DOWN)
        self._buttons.append(NormalButton(self._window,1,(xOffset,yOffset),80,40,"START"))
        yOffset = calcuateOffset(40,h,1,2,CenterModes.DOWN)
        self._buttons.append(NormalButton(self._window, 2, (xOffset,yOffset), 80, 40, "QUIT"))
        self._isAlive = True
        self._returnWindow = None

    def onUpdate(self):
        if Input.mousEvent is not None:
            event = Input.mousEvent
            id = -1
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self._buttons:
                    if button.isOverButton(event.pos):
                        id = button.getId()
                        break
                if id == 1:
                    self._isAlive = False
                elif id == 2:
                    self._isAlive = False

    def onRender(self):
        for button in self._buttons:
            button.draw()

    def isAlive(self):
        return self._isAlive

    def onKill(self):
        return self._returnWindow
