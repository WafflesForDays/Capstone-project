import pygame
import random
from variables import *
from sprite import Entity
from player import *
from camera import Camera
from enemy import Enemy
from attack import Attack
from projectile import Projectile
from hp import HP

class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.frames = 0
        self.spawns = 0
        self.shadowStar = 0
        self.stop = False
        self.bg = pygame.image.load("Images/gameBG.png")
        self.bg = pygame.transform.scale(self.bg, (1280, 720))

        self.sprites = Camera()
        self.gui = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.swing = pygame.sprite.Group()
        self.proj = pygame.sprite.Group()
        
        for i in range(10):
            self.floor = Entity([self.sprites, self.blocks], (TILESIZE*32, TILESIZE*32), pos = (-1280 + i * 256, TILESIZE*64), color = (0,255,0)) #FLOOR
        self.wall1 = Entity([self.sprites, self.blocks], (TILESIZE, TILESIZE*64), pos = (-1280, TILESIZE*16), color = (0,255,0))
        self.wall2 = Entity([self.sprites, self.blocks], (TILESIZE, TILESIZE*64), pos = (1280, TILESIZE*16), color = (0,255,0))

        self.player = Player([self.sprites, self.player], params = {'enemy': self.enemy,'block':self.blocks, 'projectile':self.proj})
        self.atk = Attack([self.sprites, self.swing], params= {'player': self.player, 'enemy': self.enemy})

        self.weapon = self.player.currentWeapon

        for i in range(self.player.health):
            HP([self.gui], i+1, self.player)
    def update(self):
        self.sprites.update()
        self.gui.update()
        self.currentScene = self.player.currentScene
        #Switch Weapons
        if not self.weapon == self.player.currentWeapon:
            self.weapon = self.player.currentWeapon
            self.atk = Attack([self.sprites, self.swing], params= {'player': self.player, 'enemy': self.enemy})
        
        #Switching scenes
        if self.player.swapScene:
            for enemy in self.enemy:
                enemy.rect.x = -99999
                enemy.HP = 0
            if self.player.currentScene == 0:
                Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN")
                Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN", pos = (-TILESIZE*4, TILESIZE*50))
            elif self.player.currentScene == 1:
                for i in range(10):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN", pos = (-TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 2:
                for i in range(6):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN", pos = (TILESIZE*32-TILESIZE*i*30, TILESIZE * 50))
            elif self.player.currentScene == 3:
                for i in range(15):
                    if i % 2 == 0:
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN", pos = (-TILESIZE*i*6, TILESIZE*50))
                    else:
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (-TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 4:
                Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_RED", pos = (-TILESIZE*32, TILESIZE*50))
            elif self.player.currentScene == 5:
                for i in range(25):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 6:
                for i in range(10):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_PURPLE", pos = (-TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 7:
                self.slimeBoss = Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="BOSS_KINGSLIME")
            elif self.player.currentScene == 8:
                for i in range(3):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (-TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 9:
                for i in range(18):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 10:
                for i in range(5):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (1200-TILESIZE*i*6, TILESIZE*50))
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (-1200+TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 11:
                Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL", pos = (0, TILESIZE*50))
            elif self.player.currentScene == 12:
                for i in range(8):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (-TILESIZE*i*16, TILESIZE*50))
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (1280-TILESIZE*i*6, TILESIZE*50))
            elif self.player.currentScene == 13:
                for i in range(5):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL", pos = (1000-TILESIZE*i*20, TILESIZE*50))
            elif self.player.currentScene == 14:
                self.shadowBoss = Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="BOSS_SHADOWGUARDIAN")
            elif self.player.currentScene == 15:
                for i in range(10):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL", pos = (1000-TILESIZE*i*20, TILESIZE*50))
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_PURPLE", pos = (1000-TILESIZE*i*20, TILESIZE*50))
            elif self.player.currentScene == 16:
                for i in range(16):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (1000-TILESIZE*i*8, TILESIZE*50))
                for i in range(10):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (1000-TILESIZE*i*8, TILESIZE*50))
            elif self.player.currentScene == 17:
                for i in range(2):
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL_BULKY", pos = (-TILESIZE*i*20, TILESIZE*50))
            elif self.player.currentScene == 18:
                for i in range(24):
                    if i%4 == 0:
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_GREEN", pos = (-1000+TILESIZE*i*8, TILESIZE*50))
                    elif i%4 == 1 :
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_BLUE", pos = (-1000+TILESIZE*i*8, TILESIZE*50))
                    elif i%4 == 1 :
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_RED", pos = (-1000+TILESIZE*i*8, TILESIZE*50))
                    elif i%4 == 1 :
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SLIME_PURPLE", pos = (-1000+TILESIZE*i*8, TILESIZE*50))
            elif self.player.currentScene == 19:
                for i in range(9):
                    if i%2 == 0 :
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="ZOMBIE", pos = (1000-TILESIZE*i*16, TILESIZE*50))
                    else: 
                        Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL", pos = (1000-TILESIZE*i*16, TILESIZE*50))
                    Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="TROLL_BULKY", pos = (0, TILESIZE*50))
            elif self.player.currentScene == 20:
                self.finalBoss = Enemy([self.sprites, self.enemy], params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="BOSS_GODSEEKER")
            self.player.swapScene = False
        
        #BOSS_02 functionality
        elif self.player.currentScene == 14:
            if self.shadowBoss.projectile:
                if self.player.currentScene == 14:
                    if self.shadowBoss.projectile == 1:
                        for i in range(30):
                            Projectile([self.sprites, self.proj], pos = (self.player.rect.x + i*TILESIZE*5, -TILESIZE*32), type = 'SHADOWLASERWALL', telegraph = 50 + 20*(self.shadowBoss.HP//5600), linger = 30)
                            Projectile([self.sprites, self.proj], pos = (self.player.rect.x - i*TILESIZE*5, -TILESIZE*32), type = 'SHADOWLASERWALL', telegraph = 50 + 20*(self.shadowBoss.HP//5600), linger = 30)
                        self.shadowBoss.projectile = 0
            if self.shadowBoss.shadowStarSummon and not self.shadowStar:
                self.shadowStar = Enemy([self.sprites, self.enemy], pos = (self.player.rect.x,self.player.rect.y - TILESIZE*24), params = {'player': self.player,'block':self.blocks, 'dmg': self.swing}, enemyType="SHADOWSTARSUMMON")
                self.shadowBoss.shadowStarSummon = 0
            if self.shadowStar:
                if self.shadowStar.projectile == 2:
                    Projectile([self.sprites, self.proj], pos = (self.shadowStar.rect.x, self.shadowStar.rect.y), velocity = self.findplayerpos(target = self.shadowStar),  type = 'SHADOWBULLET', linger = 300)
                    self.shadowStar.projectile = 0
        #BOSS_03 functionality
        elif self.player.currentScene == 20:
            if self.finalBoss.projectile:
                if self.finalBoss.projectile == 1:
                    for i in range(10):
                        if self.finalBoss.rect.x < self.player.rect.x:
                            Projectile([self.sprites, self.proj], pos = (-128*TILESIZE+self.player.rect.x, self.player.rect.y+180*(5-i)), velocity = self.findplayerpos(coords = (-128*TILESIZE+self.player.rect.x, self.player.rect.y+180*(5-i)), multi = (2, 10)),  type = 'SHADOWBULLET', linger = 300)
                        else:
                            Projectile([self.sprites, self.proj], pos = (128*TILESIZE+self.player.rect.x, self.player.rect.y+180*(5-i)), velocity = self.findplayerpos(coords = (128*TILESIZE+self.player.rect.x, self.player.rect.y+180*(5-i)), multi = (2, 10)),  type = 'SHADOWBULLET', linger = 300)
                    self.finalBoss.projectile = 0
                elif self.finalBoss.projectile == 2:
                    gap = random.randint(17, 33)
                    for i in range(50):
                        if i not in {gap-1, gap, gap+1}:
                            Projectile([self.sprites, self.proj], pos = (self.player.rect.x+16*(25-i), self.player.rect.y - TILESIZE*64), velocity = (0, 1),  type = 'SHADOWBULLET', linger = 1000)
                    self.finalBoss.projectile = 0
                elif self.finalBoss.projectile == 3:
                    extra = random.randint(-64, 64)
                    Projectile([self.sprites, self.proj], pos = (self.finalBoss.rect.x + random.randint(-8, 8), self.finalBoss.rect.y + random.randint(-8, 8)), velocity = (4, 1),  type = 'SHADOWBULLET', linger = 1000)
                    Projectile([self.sprites, self.proj], pos = (self.finalBoss.rect.x + random.randint(-8, 8), self.finalBoss.rect.y + random.randint(-8, 8)), velocity = (4, -1),  type = 'SHADOWBULLET', linger = 1000)
                    if self.finalBoss.frameCount % 5 == 0:
                        Projectile([self.sprites, self.proj], pos = (self.player.rect.x + TILESIZE*128, self.player.rect.y+extra*TILESIZE), velocity = (-2, 0),  type = 'SHADOWBULLET', linger = 1000)
                elif self.finalBoss.projectile == 4:
                    randy = random.randint(-64, 64)
                    randx = random.randint(-128, 128)
                    if self.finalBoss.frameCount % 12 == 0:
                        Projectile([self.sprites, self.proj], pos = (self.player.rect.x - TILESIZE*128, self.player.rect.y + TILESIZE*randy), velocity = (0.3, 0),  type = 'SEEKER', linger = 1000)
                    elif self.finalBoss.frameCount % 12 == 3:
                        Projectile([self.sprites, self.proj], pos = (self.player.rect.x + TILESIZE*randx, self.player.rect.y - TILESIZE*64), velocity = (0, 0.3),  type = 'SEEKER', linger = 1000)
                    elif self.finalBoss.frameCount % 12 == 6:
                        Projectile([self.sprites, self.proj], pos = (self.player.rect.x + TILESIZE*128, self.player.rect.y + TILESIZE*randy), velocity = (-0.3, 0),  type = 'SEEKER', linger = 1000)
                    elif self.finalBoss.frameCount % 12 == 9:
                        Projectile([self.sprites, self.proj], pos = (self.player.rect.x + TILESIZE * randx, self.player.rect.y + TILESIZE*64), velocity = (0, -0.3),  type = 'SEEKER', linger = 1000)


        #Player Projectile Functionality
        for weapon in self.swing:
            if weapon.check:
                if weapon.shoot:
                    Projectile([self.sprites, self.proj, self.swing], pos = (self.player.rect.x+self.player.facing*TILESIZE*-2, self.player.rect.y+random.randrange(1, 16)), telegraph = 0, linger = 500, player = True, gravity = True, params={'block':self.blocks, 'player':self.player})
        #Game Over
        if self.player.health <= 0:
            self.stop = True
    def draw(self):
        self.app.screen.blit(self.bg, (0, 0))
        self.sprites.draw(self.player, self.app.screen)
        self.gui.draw(self.app.screen)
    def findplayerpos(self, target = None, coords = None, multi = (1, 1)):
        if target:
            startPos = (target.rect.x, target.rect.y)
        if coords:
            startPos = coords
        temp = (self.player.rect.x - startPos[0]) ** 2 + (self.player.rect.y - startPos[1]) ** 2
        dx = 1
        dy = 1
        if self.player.rect.x < startPos[0]:
            dx = -1
        if self.player.rect.y < startPos[1]:
            dy = -1
        return multi[0] * (dx*(self.player.rect.x - startPos[0]) ** 2) / temp, multi[1]*(dy*(self.player.rect.y - startPos[1]) ** 2) / temp