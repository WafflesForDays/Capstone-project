import pygame
from variables import *
from player import *

#HP indicator

class HP(pygame.sprite.Sprite):
    def __init__(self, groups, hpCount, player) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((TILESIZE*2, TILESIZE*2))
        self.count = hpCount
        self.pos = (self.count*24, TILESIZE) #EDIT LATER
        # self.image.fill('red')
        self.image = pygame.image.load("Images/heart.png")
        self.image = pygame.transform.scale(self.image, (TILESIZE*4, TILESIZE*4))
        self.player = player
        self.rect = self.image.get_rect(topleft = self.pos)

        self.HPval = self.player.health
    def update(self):
        self.HPval = self.player.health
        if self.HPval < self.count:
            self.kill()
    def kill(self):
        self.rect.x = 999999