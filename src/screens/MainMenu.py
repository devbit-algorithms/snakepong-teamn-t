from src.screens.BaseScreen import BaseScreen
from src.SubWindow import SubWindow
from src.button.NormalButton import NormalButton
from src.Util import calcuateOffset,CenterModes


class MainMenu(BaseScreen):
    def __init__(self, aParrent: SubWindow):
        x,y,l,h = aParrent.getSize()
        self._window = aParrent.newChildWindow(x,y,l,h)
        self._parrent = aParrent
        self._Buttons = []
        xOffset = calcuateOffset(80,l,0,1,CenterModes.DOWN)
        yOffset = calcuateOffset(40,h,0,2,CenterModes.DOWN)
        self._Buttons.append(NormalButton(self._window,1,(xOffset,yOffset),80,40,"START"))
        yOffset = calcuateOffset(40,h,1,2,CenterModes.DOWN)
        self._Buttons.append(NormalButton(self._window, 2, (xOffset,yOffset), 80, 40, "QUIT"))

    def onRender(self):
        for button in self._Buttons:
            button.draw()
