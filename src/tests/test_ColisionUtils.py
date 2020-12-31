from src.Utils.ColisionUtils import *


def test_colide_squairs():
    hitBox1 = HitBoxSquare(10, 10, 5, 5)
    hitBox2 = HitBoxSquare(12, 12, 5, 5)
    assert colideSquairs(hitBox1, hitBox2)
    hitBox2 = HitBoxSquare(8, 8, 16, 2)
    assert not colideSquairs(hitBox1, hitBox2)
    hitBox2 = HitBoxSquare(8, 8, 3, 3)
    assert colideSquairs(hitBox1, hitBox2)


def test_colide_circils():
    hitBox1 = HitBoxCircle(10, 10, 5)
    hitBox2 = HitBoxCircle(11, 11, 3)
    assert colideCircils(hitBox1, hitBox2)
    hitBox2 = HitBoxCircle(16, 16, 8)
    assert not colideCircils(hitBox1, hitBox2)


def test_colide_circle_squair():
    hitBox1 = HitBoxSquare(10,10,10,10)
    hitBox2 = HitBoxCircle(8,8,3)
    assert colideCircleSquair(hitBox2,hitBox1)
