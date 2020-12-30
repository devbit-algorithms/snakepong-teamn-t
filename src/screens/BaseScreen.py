class BaseScreen:
    def __init__(self):
        pass

    def onUpdate(self):
        pass
    
    def onRender(self):
        pass

    def isAlive(self):
        return False

    def onKill(self):
        return None


