from src.screens.BaseScreen import BaseScreen
from src.SubWindow import SubWindow
from src.button.NormalButton import NormalButton


class MainMenu(BaseScreen):
    def __init__(self, aParrent: SubWindow):
        x,y,l,h = aParrent.getSize()
        self._window = aParrent.newChildWindow(x,y,l,h)
        self._parrent = aParrent
        self._Buttons = []
        self._Buttons.append(NormalButton(self._window,1,(10,10),80,40,"test"))

    def onRender(self):
        for button in self._Buttons:
            button.draw()
