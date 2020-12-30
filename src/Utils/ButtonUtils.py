from src.button.BaseButton import BaseButton
from typing import List


class ButtonUtils:
    @staticmethod
    def getButtonById(aButtonList: List[BaseButton],aID):
        for button in aButtonList:
            if button.getId() == aID:
                return button
