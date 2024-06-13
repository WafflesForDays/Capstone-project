import pygame
import sys
from variables import *
from scene import Scene

class main:
    def __init__(self) -> None: # Initiallizing
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.running = True

        self.scene = Scene(self)

    def run(self): # Game Loop
        while self.running:
            self.update()
            self.draw()
        self.close()
    def update(self): # Logic Updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.scene.stop:
                self.running = False

        self.scene.update()
        pygame.display.update()
        self.clock.tick(FPS)
    def draw(self): # Graphic Updates
        self.scene.draw()
    def close(self): # End of Game 
        pygame.quit()
        sys.exit

if __name__ == "__main__":
    game = main()
    game.run()