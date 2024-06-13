import pygame
from variables import *
from projStats import *
from weapons import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, groups, pos = (0, 0), velocity = (0, 0), type = "", telegraph = 0, linger = 0, player = False, gravity = False, params = {}) -> None:
        super().__init__(groups)
        self.playerFlag = player
        self.check = False
        self.blockGroup = {}
        self.type = type
        self.temp = 0

        if "block" in params:
            self.blockGroup = params["block"]
        if 'player' in params:
            self.player = params['player']

        if self.playerFlag:
            self.Stats = getWeapon(weapons[self.player.currentWeapon])
            self.image = pygame.Surface((self.Stats[3]*TILESIZE, self.Stats[4]*TILESIZE))
        else:
            self.Stats = getStats(type)
            self.image = pygame.Surface((self.Stats[0], self.Stats[1]))
        self.telegraph = telegraph
        self.linger = linger
        self.damage = False
        self.gravity = gravity
        self.velocity = pygame.math.Vector2()
        self.velocity.x = velocity[0] * TILESIZE
        self.velocity.y = velocity[1] * TILESIZE
        if self.playerFlag:
            # self.velocity.x = self.Stats[8] * TILESIZE
            # self.velocity.y = self.Stats[9] * TILESIZE
            mousex, mousey = pygame.mouse.get_pos()
            self.velocity.x, self.velocity.y = 5*TILESIZE*(mousex-640)/math.sqrt(mousex**2+640**2), 5*TILESIZE*(mousey - 488)/math.sqrt(mousey**2+488**2)

        if type == "SHADOWBULLET":
            self.image = pygame.image.load("Images/shadowBullet.png")
            self.image = pygame.transform.scale(self.image, (self.Stats[0], self.Stats[1]))
        elif type == "SHADOWLASERWALL":
            self.image = pygame.image.load("Images/shadowLaserInactive.png")
            self.image = pygame.transform.scale(self.image, (self.Stats[0], self.Stats[1]))
        elif type == "SEEKER":
            self.image = pygame.image.load("Images/skullBullet.png")
            self.image = pygame.transform.scale(self.image, (self.Stats[0], self.Stats[1]))
        elif self.playerFlag:
            self.image = pygame.image.load("Images/playerBullet.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*2, TILESIZE*2))
            
        
        # if not self.playerFlag:
        #     if self.telegraph:
        #         pass
        #     else:
        #         self.image = pygame.image.load("Images/shadowLaserActive.png")
        #         self.image = pygame.transform.scale(self.image, (self.Stats[0], self.Stats[1]))
        self.rect = self.image.get_rect(topleft = pos)

    def move(self):
        if self.gravity:
            self.velocity.y += 2
            if self.velocity.y > 8:
                self.velocity.y = 8
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    def update(self):
        if self.blockGroup:
            self.checkCollision()
        self.move()
        if self.telegraph:
            self.telegraph -= 1
        elif self.type == "SHADOWLASERWALL" and not self.temp:
            self.image = pygame.image.load("Images/shadowLaserActive.png")
            self.image = pygame.transform.scale(self.image, (self.Stats[0], self.Stats[1]))
            self.temp = 1
        elif self.linger:
            self.damage = True
            # if not self.playerFlag:
            #     self.image.fill('red')
            self.linger -= 1
        else:
            self.kill()
    def kill(self):
        self.rect.x = 99999
        self.velocity.x = 0
        self.velocity.y = 0
    def checkCollision(self):
        for block in self.blockGroup:
            if block.rect.colliderect(self.rect):
                self.kill()