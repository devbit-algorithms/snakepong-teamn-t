import pygame
import time
from src.SubWindow import SubWindow
from src.screens.MainMenu import MainMenu
from src.Statics import Input
from src.screens import BaseScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self._running = True
        self.size = self.weight, self.height = 640, 400
        self._headDisplay = pygame.display.set_mode(self.size, pygame.SCALED)
        self._mainSubWindow = SubWindow(self._headDisplay, 0, 0, 640, 400)
        self._window: BaseScreen = MainMenu(self._mainSubWindow)

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            Input.mousEvent = event

    def onLoop(self):
        timeA = time.time()
        self._window.onUpdate()
        timeB = time.time()
        # print(timeB-timeA," logic time")
        Input.mousEvent = None
        Input.keyEvent = None

    def onRender(self):
        timeA = time.time()
        self._window.onRender()
        timeB = time.time()
        # print(timeB - timeA," render time")
        pygame.display.update()

    def onCleanup(self):
        pygame.quit()

    def checkAlive(self):
        if not self._window.isAlive():
            self._window = self._window.onKill()
            if self._window is None:
                self._running = False
        return self._running


def main():
    game = Game()
    while game.checkAlive():
        timeA = time.time()
        for event in pygame.event.get():
            game.onEvent(event)
        game.onLoop()
        game.onRender()
        timeB = time.time()
        timeTotal = timeB - timeA
        sleepTime = 0.016 - timeTotal
        if sleepTime > 0:
            time.sleep(sleepTime)
    game.onCleanup()


if __name__ == "__main__":
    main()
