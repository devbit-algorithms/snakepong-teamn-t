class BaseButton:
    def __init__(self,id,TRPos,BLPos):
        self._TRPos = TRPos
        self._BLPos = BLPos
        self._id = id

    def __draw__(self):
        pass

    def isOverButton(self,pos):#make test for this
        return (self._TRPos[0] < pos[0] and self._TRPos[1] < pos[1] and
                self._BLPos[0] > pos[0] and self._BLPos[1] > pos[1])

        
        