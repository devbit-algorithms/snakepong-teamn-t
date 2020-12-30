from src.button.BaseButton import BaseButton
from src.SubWindow import CenterModes
from src.Utils.Util import Colors
import pygame


class NormalButton(BaseButton):
    def __init__(self,aParrent,aID,aPos,aL,aH,aText,aFontSize=24,aDrawBackground=False,
                 aColorText=Colors.white,aColorBorder=Colors.black):
        super().__init__(aParrent,aID,aPos,aL,aH)
        self._font = pygame.font.SysFont('ubuntu',aFontSize)
        self._text = aText
        self._colorText = aColorText
        self._drawBackground = aDrawBackground
        self._colorBackground = aColorBorder
        self._textPos = (aL >> 1,aH >> 1)

    def draw(self):
        if self._drawBackground or self._selected:
            self._window.drawBackGround(self._colorText if self._selected else self._colorBackground)
        if not self._selected:
            self._window.drawBorder(self._colorText,1)
        self._window.drawText(self._text, self._font, self._colorBackground if self._selected else self._colorText,
                              self._textPos, CenterModes.CENTER)
