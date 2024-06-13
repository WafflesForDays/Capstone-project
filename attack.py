import pygame
from variables import *
from weapons import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, groups, pos = (0, 0), params = {}) -> None:
        super().__init__(groups)
        self.player = params['player']
        self.currentWeapon = weapons[self.player.currentWeapon]
        self.projectile = False
        if self.currentWeapon in projWeapons:
            self.projectile = True
        self.stats = getWeapon(self.currentWeapon)
        self.image = pygame.Surface((TILESIZE*self.stats[3], TILESIZE*self.stats[4]))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pos
        self.frames = 0
        self.cool = 0
        self.shoot = False
        self.check = True

        self.player = params['player']

        self.rotation = 0
    def triggerAtk(self):
        if weapons[self.player.currentWeapon] == self.currentWeapon:
            self.image = pygame.Surface((TILESIZE*self.stats[3], TILESIZE*self.stats[4]))
            self.image.fill('yellow')
            if self.shoot:
                self.shoot = False
            if not self.cool:
                keys = pygame.key.get_pressed()
                mouseInput = pygame.mouse.get_pressed(num_buttons=3)

                if (mouseInput[0] or keys[pygame.K_q]) and not self.frames:
                    self.frames = self.stats[0]
                    self.cool = self.stats[1] + self.stats[0]
                    if self.projectile:
                        self.shoot = True

            if self.frames:
                if not self.projectile:
                    self.gotoPlayer()
                self.frames -= 1
            else:
                self.rect.x, self.rect.y = 99999, 0
            if self.cool:
                self.cool -= 1
    def gotoPlayer(self):
        if self.player.facing == 1:
            self.rect.x = self.player.rect.x - TILESIZE*self.stats[5]
        else:
            self.rect.x = self.player.rect.x - TILESIZE*-2
        self.rect.y = self.player.rect.y + TILESIZE*self.stats[6]
    def update(self):
        self.triggerAtk()