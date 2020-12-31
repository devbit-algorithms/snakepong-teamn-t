from src.button.BaseButton import BaseButton
from src.SubWindow import SubWindow


def test_is_over_button():
    window = SubWindow(None,0,0,100,100)
    button = BaseButton(window,0,(10,10),10,10)
    assert button.isOverButton((12,14))
    assert not button.isOverButton((12,21))
