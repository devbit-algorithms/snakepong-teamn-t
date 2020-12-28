import pygame
import time



class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight,self.height = 640, 400

    
    def onInit(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size,pygame.SCALED)
        self._running = True
        size = pygame.display.Info()
        b = size.current_w
        a = 10

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            a = event.pos[0]
            b = event.pos[1]

    def onLoop(self):
        pass

    def onRender(self):
        pass

    def onCleanup(self):
        pygame.quit()





def main():
    game = Game()
    game.onInit()
    while game._running:
        for event in pygame.event.get():
            game.onEvent(event)
        game.onLoop()
        game.onRender()
        time.sleep(0.16)
    game.onCleanup()


if __name__=="__main__":
    main()

