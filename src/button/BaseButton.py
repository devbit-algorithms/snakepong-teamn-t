from src.SubWindow import SubWindow


class BaseButton:
    def __init__(self, aParrent: SubWindow, aID, aPos, aL, aH):
        self._Pos = aPos
        self._l = aL
        self._h = aH
        self._id = aID
        self._parrent = aParrent
        self._window = aParrent.newChildWindow(aPos[0],aPos[1],aL,aH)
        self._selected = False

    def draw(self):
        pass

    def getId(self):
        return self._id

    def getSelected(self):
        return self._selected

    def setSelected(self,aStatus):
        self._selected = aStatus

    def isOverButton(self, aPos):#make test for this
        return self._Pos[0] < aPos[0] < (self._Pos[0] + self._l) and self._Pos[1] < aPos[1] < (self._Pos[1] + self._h)
