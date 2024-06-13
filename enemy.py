import pygame
import random
from variables import *
from weapons import *
from attack import *
from enemyStats import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), pos = (0, TILESIZE*50), params = {}, enemyType = "") -> None:
        super().__init__(groups)
        self.Stats = getStats(enemyType)
        self.image = pygame.Surface((TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        # self.image.fill('red')
        if enemyType == "BOSS_GODSEEKER":
            self.spin = True
        self.rect = self.image.get_rect(topleft = pos)
        self.AItype = self.Stats[1]
        self.projectile = 0
        self.summoned = True
        self.dead = False
        if enemyType == "SHADOWSTARSUMMON":
            self.dead = True

        self.player = params['player']
        self.blockGroup = params['block']
        self.dmg = params['dmg']

        self.velocity = pygame.math.Vector2()
        self.dir = 1
        self.mass = 5
        self.gravity = 1
        if self.AItype in ["SHADOWSTARSUMMON", "BOSS_GODSEEKER"]:
            self.gravity = 0
        self.term = self.mass * TERMINALVELOCITY
        self.jumps = 1
        self.HP = self.Stats[0]
        self.iFrames = 0
        self.count = 0
        self.frameCount = 0
        self.atk = False
        self.summonFlag = True
        self.shadowStarSummon = 0
        self.rapidFire = False
        self.dash = 0
        self.floorCheck = 0
        self.floorChecked = 0
        self.weaponName = weapons[self.player.currentWeapon]
        self.weaponStats = getWeapon(self.weaponName)

        # Image
        if enemyType == "SLIME_GREEN":
            self.image = pygame.image.load("Images/greenSlime.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "SLIME_BLUE":
            self.image = pygame.image.load("Images/blueSlime.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "SLIME_PURPLE":
            self.image = pygame.image.load("Images/purpleSlime.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "SLIME_RED":
            self.image = pygame.image.load("Images/redSlime.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "ZOMBIE":
            self.image = pygame.image.load("Images/zombie.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "TROLL":
            self.image = pygame.image.load("Images/troll.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "TROLL_BULKY":
            self.image = pygame.image.load("Images/troll.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "BOSS_KINGSLIME":
            self.image = pygame.image.load("Images/kingSlime.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "BOSS_SHADOWGUARDIAN":
            self.image = pygame.image.load("Images/shadowKing.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "BOSS_GODSEEKER":
            self.image = pygame.image.load("Images/godSeeker.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
        elif enemyType == "SHADOWSTARSUMMON":
            self.image = pygame.image.load("Images/shadowStar.png")
            self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))

    def AI(self):
        if self.HP > 0:
            self.frameCount += 1
        if self.AItype == "ZOMBIE":
            if self.player.rect.x +TILESIZE*8 >= self.rect.x and self.player.rect.x -TILESIZE*8 <= self.rect.x and self.player.rect.y < self.rect.y and self.jumps:
                self.velocity.y = -14
                self.jumps -= 1

            if self.player.rect.x > self.rect.x:
                if self.dir == 1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = -1
                self.velocity.x = 1
            elif self.player.rect.x < self.rect.x:
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = 1
                self.velocity.x = -1
        if self.AItype == "SLIME":
            if self.player.rect.x > self.rect.x and self.frameCount >= (FPS) and self.jumps:
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = 1
                self.velocity.x = 5
                if self.count == 2 and self.jumps:
                    self.velocity.y = -8
                    self.jumps -= 1
                    self.count = 0
                    self.frameCount = -15
                elif self.jumps:
                    self.velocity.y = -5
                    self.jumps -= 1
                    self.count +=1 
                    self.frameCount = 0
            elif self.player.rect.x < self.rect.x and self.frameCount >= (FPS) and self.jumps:
                if self.dir == 1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = -1
                self.velocity.x = -5
                if self.count == 2:
                    self.velocity.y = -8
                    self.jumps -= 1
                    self.count = 0
                    self.frameCount = -15
                else:
                    self.velocity.y = -5
                    self.jumps -= 1
                    self.count +=1
                    self.frameCount = 0
        if self.AItype == "BOSS_KINGSLIME":
            if self.player.rect.x > self.rect.x and self.frameCount >= ((FPS//10)*((self.HP*10//self.Stats[0]) + 1)) and self.jumps and self.dash <= 0:
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = 1
                self.velocity.x = 5
                if self.count in {9}:
                    if self.HP <= 700:
                        self.dash = FPS #Allow Movement on Floor
                    else:
                        self.count = 0
                elif self.count in {2, 5, 8} and self.jumps and not self.dash:
                    self.velocity.y = -16
                    self.jumps -= 1
                    self.frameCount = -45
                    self.count +=1 
                else:
                    self.velocity.y = -8
                    self.jumps -= 1
                    self.count +=1 
                    self.frameCount = 0
            elif self.player.rect.x < self.rect.x and self.frameCount >= ((FPS//10)*(self.HP*10//self.Stats[0] + 1)) and self.jumps and self.dash <= 0:
                if self.dir == 1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = -1
                self.velocity.x = -5
                if self.count in {9}:
                    if self.HP <= 700:
                        self.dash = FPS #Allow Movement on Floor
                    else:
                        self.count = 0
                elif self.count in {2, 5, 8} and self.jumps and self.dash <= 0:
                    self.velocity.y = -16
                    self.jumps -= 1
                    self.frameCount = -45
                    self.count +=1 
                else:
                    self.velocity.y = -8
                    self.jumps -= 1
                    self.count +=1 
                    self.frameCount = 0
            elif self.player.rect.x < self.rect.x and self.dash > 0:
                if self.dash == FPS:
                    self.velocity.x = -15
                self.dash -= 1
                if not self.dash:
                    self.count = 0
            elif self.player.rect.x >= self.rect.x and self.dash > 0:
                if self.dash == FPS:
                    self.velocity.x = 15
                self.dash -= 1
                if not self.dash:
                    self.count = 0
        if self.AItype == "SHADOWSTARSUMMON":
            if self.frameCount % 50 == 0:
                self.projectile = 2
            if self.frameCount % 270 == 0:
                self.rapidFire = True
            if (self.frameCount - 30) % 270 == 0:
                self.rapidFire = False
            if self.rapidFire and not self.frameCount % 5:
                self.projectile = 2
            if (self.frameCount + 48) % 96 == 0:
                self.count += 1
            if self.count % 4 == 0:
                self.velocity.x = 4
                self.velocity.y = 0
            elif self.count % 4 == 1:
                self.velocity.x = 0
                self.velocity.y = 4
            elif self.count % 4 == 2:
                self.velocity.x = -4
                self.velocity.y = 0
            elif self.count % 4 == 3:
                self.velocity.x = 0
                self.velocity.y = -4
            if self.rect.x > self.player.rect.x + TILESIZE*24:
                self.rect.x = self.player.rect.x + TILESIZE*24
            elif self.rect.x < self.player.rect.x - TILESIZE*24:
                self.rect.x = self.player.rect.x - TILESIZE*24
        if self.AItype == "BOSS_SHADOWGUARDIAN":
            if self.summonFlag and self.HP < 4300:
                self.shadowStarSummon = 1
                self.summonFlag = False
            if self.frameCount < 200:
                if self.player.rect.x > self.rect.x:
                    if self.velocity.x < 5:
                        self.velocity.x += 0.2
                elif self.player.rect.x < self.rect.x:
                    if self.velocity.x > -5:
                        self.velocity.x -= 0.2
            elif self.frameCount == 200:
                self.velocity.x = 0
                self.atk = 1
            if self.count >= 3:
                self.projectile = 1
                self.count = 0
                if self.frameCount >= 300 + 30*(self.HP//self.Stats[0]) and self.frameCount < 330 + 20*(self.HP//self.Stats[0]):
                    if self.player.rect.x > self.rect.x:
                        self.velocity.x = 20
                    else:
                        self.velocity.x = -20
                elif self.frameCount >= 330 + 20*(self.HP//self.Stats[0]):
                    self.velocity.x = 0
                    self.frameCount = 0
            else:
                if self.atk == 1:
                    self.count += 1
                    self.atk = 2
                if self.frameCount >= 250 + 40*(self.HP//self.Stats[0]) and self.frameCount < 270 + 40*(self.HP//self.Stats[0]) and self.atk == 2:
                    if self.player.rect.x > self.rect.x:
                        self.velocity.x = 20
                    else:
                        self.velocity.x = -20
                    self.atk = 0
                elif self.frameCount >= 270 + 40*(self.HP//self.Stats[0]):
                    self.velocity.x = 0
                    self.frameCount = 0
            if self.velocity.x > 0:
                if self.dir == 1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = -1
            else:
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.dir = 1
        if self.AItype == "BOSS_GODSEEKER":
            if self.spin:
                if self.frameCount % 3 == 0:
                    self.image = self.rot_center(self.image, 45)
            else:
                self.image = pygame.image.load("Images/godSeeker.png")
                self.image = pygame.transform.scale(self.image, (TILESIZE*self.Stats[2], TILESIZE*self.Stats[3]))
            
            if self.HP <= 2000:
                if not self.count:
                    self.frameCount = 0
                    self.count = 1
                    self.rect.x = self.player.rect.x - TILESIZE*64
                    self.rect.y = self.player.rect.y
                    self.velocity.x = 0
                    self.velocity.y = 0
                    self.spin = False
                self.projectile = 4
                if self.frameCount == 5000:
                    self.HP = 0
                    self.projectile = 0
            elif 2000 <= self.frameCount <= 2801:
                self.velocity.y = 0
                self.velocity.x = 0
                self.spin = False
                self.rect.x = self.player.rect.x
                self.rect.y = self.player.rect.y - TILESIZE*72
                if self.frameCount % 80 == 0:
                    self.projectile = 2
            elif self.frameCount >= 5000:
                self.velocity.x = 0
                self.velocity.y = 0
                self.spin = False
                if self.frameCount == 5000:
                    self.rect.x = self.player.rect.x - TILESIZE*64
                    self.rect.y = self.player.rect.y
                    self.projectile = 3
                if self.frameCount >= 6000:
                    self.projectile = 0
                    self.frameCount = 0
                    self.spin = True
            elif self.frameCount % 50 == 0:
                self.velocity.x, self.velocity.y = self.findplayer()
                self.velocity.x *= TILESIZE*2
                self.velocity.y *= TILESIZE*2
                self.spin = True
            elif self.frameCount % 250 == 1:
                self.projectile = 1

            
            
    def move(self):
        if self.gravity:
            self.velocity.y += GRAVITY * self.mass

            if self.velocity.y > self.term:
                self.velocity.y = self.term

        if self.AItype == "ZOMBIE":
            self.rect.x += self.velocity.x
            self.checkCollisions('x')
            self.rect.y += self.velocity.y
            self.checkCollisions('y')
            if self.floorCheck:
                self.jumps = 1
        elif self.AItype == "SLIME":
            self.rect.x += self.velocity.x
            self.checkCollisions('x')
            self.rect.y += self.velocity.y
            self.checkCollisions('y')
            if self.floorCheck:
                self.jumps = 1
                self.velocity.x = 0
        elif self.AItype == "BOSS_KINGSLIME":
            self.rect.x += self.velocity.x
            self.checkCollisions('x')
            self.rect.y += self.velocity.y
            self.checkCollisions('y')
            if self.floorCheck:
                self.jumps = 1
                if not self.dash:
                    self.velocity.x = 0
        elif self.AItype == "SHADOWSTARSUMMON":
            self.rect.y += self.velocity.y
            self.rect.x += self.velocity.x
        elif self.AItype == "BOSS_SHADOWGUARDIAN":
            self.rect.x += self.velocity.x
            self.checkCollisions('x')
            self.rect.y += self.velocity.y
            self.checkCollisions('y')
        elif self.AItype == "BOSS_GODSEEKER":
            self.rect.x += self.velocity.x
            self.rect.y += self.velocity.y
            self.checkCollisions('dmg')
    def checkCollisions(self, dir):
        if dir == 'x':
            for block in self.blockGroup: # Block collision x
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0:
                        self.rect.right = block.rect.left
                    if self.velocity.x < 0:
                        self.rect.left = block.rect.right
        elif dir == 'y':
            for block in self.blockGroup: # Block collision y
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0:
                        self.rect.bottom = block.rect.top
                        self.floorChecked = 1
                        self.floorCheck = True
                    if self.velocity.y < 0:
                        self.rect.top = block.rect.bottom
                        self.velocity.y -= self.velocity.y
                elif not self.floorChecked:
                    self.floorCheck = False
            self.floorChecked = 0
        for dmg in self.dmg: # Weapon collision
            if dmg.rect.colliderect(self.rect) and not self.iFrames:
                self.HP -= self.weaponStats[7] * (self.player.dmgMulti + 1)
                self.iFrames = self.weaponStats[2]
        if self.iFrames:
        #     self.image.fill('pink')
            self.iFrames -= 1
        # else:
            # self.image.fill('red')
    def death(self):
        if self.HP <= 0:
            self.HP = 0
            self.projectile = 0
            self.rect.x = -99999 # Kill
            self.dead = True
    def update(self):
        if self.HP:
            self.AI()
            self.move()
            self.death()
    def killAll(self):
        self.HP = 0
    def findplayer(self, offsetX = 0, offsetY = 0):
        temp = ((self.player.rect.x + offsetX) - self.rect.x) ** 2 + ((self.player.rect.y + offsetY) - self.rect.y) ** 2
        dx = 1
        dy = 1
        if self.player.rect.x < self.rect.x:
            dx = -1
        if self.player.rect.y < self.rect.y:
            dy = -1
        return (dx*((self.player.rect.x + offsetX) - self.rect.x) ** 2) / temp, (dy*((self.player.rect.y + offsetY) - self.rect.y) ** 2) / temp
    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image