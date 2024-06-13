import pygame
from player import Player
from variables import *

class Camera(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
    def draw(self, target: Player, display: pygame.Surface):
        offset = pygame.math.Vector2()
        offset.x = display.get_width() / 2 - target.rect.centerx
        offset.y = display.get_height() / 2 - target.rect.centery + TILESIZE * 16

        for sprite in self.sprites():
            spriteOffset = pygame.math.Vector2()
            spriteOffset.x = offset.x + sprite.rect.x
            spriteOffset.y = offset.y + sprite.rect.y

            display.blit(sprite.image, spriteOffset)