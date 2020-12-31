from src.SubWindow import SubWindow
from src.screens.BaseScreen import BaseScreen
from src.button.NormalButton import NormalButton
from src.Statics import World
from src.Entitys.EntityWorm import EntityWorm


class LevelScreen(BaseScreen):
    def __init__(self, aParrent: SubWindow):
        x,y,l,h = aParrent.getSize()
        self._tick = 0
        self._window = aParrent.newChildWindow(x,y,l,h)
        self._alive = True
        self._buttons = []
        self._buttons.append(NormalButton(self._window,1,(l-100,h-60),80,40,"MENU"))
        World.addEnttity(EntityWorm(self._window,100,100,10,60,1))


    def onRender(self):
        for entity in World.livingEntityList:
            entity.draw()
        for button in self._buttons:
            button.draw()

    def onUpdate(self):
        self._tick += 1
        if self._tick > 200:
            if self._tick%4 == 0:
                for entity in World.livingEntityList:
                    entity.update()

    def isAlive(self):
        return self._alive
