from src.Utils.Util import calcuateOffset,CenterModes

def test_calcuate_offset():
    offset = calcuateOffset(10,100,1,4)
    assert offset == 37
    offset = calcuateOffset(10,100,3,4,CenterModes.DOWN)
    assert offset == 82
