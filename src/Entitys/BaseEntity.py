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