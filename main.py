import pygame
import time
from src.SubWindow import SubWindow
from src.screens.MainMenu import MainMenu


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self._running = True
        self.size = self.weight, self.height = 640, 400
        self._headDisplay = pygame.display.set_mode(self.size, pygame.SCALED)
        self._mainSubWindow = SubWindow(self._headDisplay, 0, 0, 640, 400)
        self._window = MainMenu(self._mainSubWindow)

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            a = event.pos[0]
            b = event.pos[1]

    def onLoop(self):
        self._window.onUpdate()

    def onRender(self):
        self._window.onRender()
        pygame.display.update()

    def onCleanup(self):
        pygame.quit()


def main():
    game = Game()
    while game._running:
        for event in pygame.event.get():
            game.onEvent(event)
        game.onLoop()
        game.onRender()
        time.sleep(0.16)
    game.onCleanup()


if __name__ == "__main__":
    main()
