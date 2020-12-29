from src.button.BaseButton import BaseButton


class NormalButton(BaseButton):
    def __init__(self,aID,aPos,aL,aH,aText):
        super().__init__(aID,aPos,aL,aH)
        self._text = aText
