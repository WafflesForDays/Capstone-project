import pygame
from variables import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image = (0, 0), pos = (0,0), params = {}, color = (0,0,0)) -> None:
        super().__init__(groups)
        self.image = pygame.Surface(image)
        self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.image.load("Images/stoneFloorTexture.png")
        self.image = pygame.transform.scale(self.image, (image[0], image[1]))
    def update(self):
        pass