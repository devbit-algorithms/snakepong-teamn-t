class BaseButton:
    def __init__(self,aID,aPos,aL,aH):
        self._Pos = aPos
        self._l = aL
        self._h = aH
        self._id = aID

    def __draw__(self,screen):
        pass

    def getId(self):
        return self._id

    def isOverButton(self, aPos):#make test for this
        return self._Pos[0] < aPos[0] < (self._Pos[0] + self._l) and self._Pos[1] < aPos[1] < (self._Pos[1] + self._h)
