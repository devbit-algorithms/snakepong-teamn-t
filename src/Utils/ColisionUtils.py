from src.Entitys.BaseEntity import HitBoxCircle, HitBoxSquare
from math import sqrt
import math


def colideSquairs(aHitBox1: HitBoxSquare, aHitBox2: HitBoxSquare):
    return (aHitBox1.X < aHitBox2.X < (aHitBox1.X + aHitBox1.L) or aHitBox2.X < aHitBox1.X < (
                aHitBox2.X + aHitBox2.L)) and (
                   aHitBox1.Y < aHitBox2.Y < (aHitBox1.Y + aHitBox1.H) or aHitBox2.Y < aHitBox1.Y < (
                       aHitBox2.Y + aHitBox2.H))


def colideCircils(aHitBox1: HitBoxCircle, aHitBox2: HitBoxCircle):
    dist = sqrt(((aHitBox1.X - aHitBox2.X) ** 2) + ((aHitBox1.Y - aHitBox2.Y) ** 2))
    return dist < aHitBox1.size or dist < aHitBox2.size


def clamp(aMin,aMax,aValue):
    return max(min(aValue, aMax), aMin)


def colideCircleSquair(aCircle: HitBoxCircle, aSquair: HitBoxSquare):

    xOffset = clamp(aSquair.X,(aSquair.X + aSquair.L),aCircle.X)
    yOffset = clamp(aSquair.Y,(aSquair.Y + aSquair.H),aCircle.Y)

    distX = aCircle.X - xOffset
    distY = aCircle.Y - yOffset
    distance = sqrt((distX ** 2) + (distY ** 2))
    return distance < aCircle.size

    # circleDistance.x = abs(circle.x - rect.x);
    # circleDistance.y = abs(circle.y - rect.y);
    #
    # if (circleDistance.x > (rect.width/2 + circle.r)) { return false; }
    # if (circleDistance.y > (rect.height/2 + circle.r)) { return false; }
    #
    # if (circleDistance.x <= (rect.width/2)) { return true; }
    # if (circleDistance.y <= (rect.height/2)) { return true; }
    #
    # cornerDistance_sq = (circleDistance.x - rect.width/2)^2 +
    #                      (circleDistance.y - rect.height/2)^2;
    #
    # return (cornerDistance_sq <= (circle.r^2));
