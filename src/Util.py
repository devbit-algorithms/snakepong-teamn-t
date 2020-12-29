from enum import Enum


class Colors:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    darkBlue = (0, 0, 128)
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (255, 200, 200)


class CenterModes(Enum):
    CENTER = 0
    CORNER_RIGHT_UP = 1
    CORNER_RIGHT_DOWN = 2
    CORNER_LEFT_UP = 3
    CORNER_LEFT_DOWN = 4
    LEFT = 5
    RIGHT = 6
    UP = 7
    DOWN = 8


def calcuateOffset(aSize, aSizeTotal, aPos, aTotalPos, aMode: CenterModes = CenterModes.CENTER):#write test
    sizePer = int(aSizeTotal/aTotalPos)
    sizeOffset = sizePer * aPos
    offset = (sizePer >> 1) + sizeOffset
    if aMode == CenterModes.CENTER:
        return offset
    elif aMode == CenterModes.DOWN:
        innerOffset = aSize >> 1
        return offset - innerOffset
    elif aMode == CenterModes.UP:
        innerOffset = aSize >> 1
        return offset + innerOffset
    else:
        print("invalid CenterMode")
        return None
