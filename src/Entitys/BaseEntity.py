class BaseEntity:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def isAlive(self):
        return False

    def kill(self):
        pass

    def hasColision(self):
        return False

    def colide(self,aEntity):
        return -1

    def getHitBox(self):
        return None


class HitBox:
    def __init__(self):
        self.type = None
    SQUAIR = 0
    CIRCLE = 1


class HitBoxSquare(HitBox):
    def __init__(self,aX,aY,aL,aH):
        super().__init__(HitBox.SQUAIR)
        self.X = aX
        self.Y = aY
        self.L = aL
        self.H = aH
