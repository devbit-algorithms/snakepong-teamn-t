import pygame
import time



class Game:
    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.weight,self.height = 640, 400

    
    def onInit(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size,pygame.SCALED)
        self._running = True

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            a = event.pos[0]
            b = event.pos[1]

    def onLoop(self):
        pass

    def onRender(self):
        pygame.draw.rect(self._screen,(255,255,255),(100,100,100,100),1)
        pygame.display.update()


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

