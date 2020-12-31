from typing import List
from pygame.event import Event

from src.Entitys.BaseEntity import BaseEntity

class Input:
    mousEvent: Event = None
    keyEvent: Event = None


class World:
    livingEntityList: List[BaseEntity] = []

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
