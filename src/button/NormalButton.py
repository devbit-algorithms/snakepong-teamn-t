from src.button.BaseButton import BaseButton
from src.SubWindow import TextModes
from src.Util import Colors
import pygame


class NormalButton(BaseButton):
    def __init__(self,aParrent,aID,aPos,aL,aH,aText,aFontSize=24,aDrawBackground=False,aColorText=Colors.white,aColorBorder=Colors.black):
        super().__init__(aParrent,aID,aPos,aL,aH)
        self._font = pygame.font.SysFont('ubuntu',aFontSize)
        self._text = aText
        self._colorText = aColorText
        self._drawBackground = aDrawBackground
        self._colorBackground = aColorBorder
        self._textPos = (aL >> 1,aH >> 1)

    def draw(self):
        if self._drawBackground:
            self._window.drawBackGround(self._colorBackground)
        self._window.drawBorder(self._colorText,1,)
        self._window.drawText(self._text,self._font,self._colorText,self._textPos,TextModes.CENTER)
