from src.SubWindow import SubWindow
from src.Utils.Util import CenterModes


def test_get_size():
    subWindow = SubWindow(None, 40, 60, 44, 66)
    x, y, l, h = subWindow.getSize()
    assert x == 40 and y == 60 and l == 44 and h == 66

def test_get_true_valid_coords():
    subWindow = SubWindow(None, 40, 60, 44, 66)
    x,y = subWindow.getTrueValidCoords((10,15))
    assert x == 50 and y == 75


def test_set_new_pos():
    subWindow = SubWindow(None, 40, 60, 40, 60)
    subWindow.setNewPos((100, 90), CenterModes.CORNER_RIGHT_DOWN)
    x, y, l, h = subWindow.getSize()
    assert x == 60 and y == 30


def test_new_child_window():
    subWindow = SubWindow(None, 40, 60, 44, 66)
    newWindow = subWindow.newChildWindow(10, 0, 15, 28)
    x, y, l, h = newWindow.getSize()
    assert x == 50 and y == 60 and l == 15 and h == 28
