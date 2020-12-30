class Input:
    mousEvent = None
    keyEvent = None


class World:
    livingEntityList = []

    @staticmethod
    def addEnttity(aEntity):
        World.livingEntityList.append(aEntity)

    @staticmethod
    def removeEnttiy(aEntity):
        pass

    # BUTTON_LEFT = 1
    # BUTTON_MIDDLE = 2
    # BUTTON_RIGHT = 3
    # BUTTON_WHEELDOWN = 5
    # BUTTON_WHEELUP = 4
