from src.SubWindow import SubWindow
from src.screens.BaseScreen import BaseScreen
from src.button.NormalButton import NormalButton


class LevelScreen(BaseScreen):
    def __init__(self, aParrent: SubWindow):
        x,y,l,h = aParrent.getSize()
        self._alive = True
        self._buttons = []
        self._buttons.append(NormalButton(aParrent,1,(l-100,h-60),80,40,"MENU"))

    def onRender(self):
        for button in self._buttons:
            button.draw()

    def isAlive(self):
        return self._alive
