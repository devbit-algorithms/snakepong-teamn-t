from src.Entitys.BaseEntity import HitBoxCircle, HitBoxSquare
from math import sqrt


def colideSquairs(aHitBox1: HitBoxSquare, aHitBox2: HitBoxSquare):
    return (aHitBox1.X < aHitBox2.X < (aHitBox1.X + aHitBox1.L) or aHitBox2.X < aHitBox1.X < (
                aHitBox2.X + aHitBox2.L)) and (
                   aHitBox1.Y < aHitBox2.Y < (aHitBox1.Y + aHitBox1.H) or aHitBox2.Y < aHitBox1.Y < (
                       aHitBox2.Y + aHitBox2.H))


def colideCircils(aHitBox1: HitBoxCircle, aHitBox2: HitBoxCircle):
    dist = sqrt(((aHitBox1.X - aHitBox2.X) ** 2) + ((aHitBox1.Y - aHitBox2.Y) ** 2))
    return dist < aHitBox1.size or dist < aHitBox2.size


def colideCircleSquair(aCircle: HitBoxCircle, aSquair: HitBoxSquare):
    if aCircle.X < aSquair.X:
        offsetX = aSquair.X
    else:
        offsetX = aSquair.X + aSquair.L
    if aCircle.Y < aSquair.Y:
        offsetY = aSquair.Y
    else:
        offsetY = aSquair.Y + aSquair.H
    distX = aCircle.X - offsetX
    distY = aCircle.Y - offsetY
    distance = sqrt((distX ** 2) + (distY ** 2))
    return distance < aCircle.size
