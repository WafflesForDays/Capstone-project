import pygame
from variables import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE*4, TILESIZE*6)), pos = (SCREENWIDTH//2, SCREENHEIGHT//2), params = {}) -> None:
        super().__init__(groups)
        self.image = image
        # self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.currentWeapon = 5
        self.dmgMulti = 0

        self.spritesheet = pygame.image.load('Images/mainCharacterSpriteSheet.png').convert_alpha()

        self.blockGroup = params['block']
        self.enemyGroup = params['enemy']
        self.projGroup = params['projectile']

        self.velocity = pygame.math.Vector2()
        self.mass = 5
        self.term = self.mass * TERMINALVELOCITY
        self.extraJumps = 0
        self.extraSpeed = 0
        self.extraAcceleration = 3
        self.jumping = False
        self.jumps = MAXJUMPS + self.extraJumps
        self.centerPos = 0
        self.facing = -1
        self.iFrames = 0
        self.frames = 0
        self.currentScene = -1
        self.swapScene = True
        self.parry = 0
        self.cooldown = 0

        self.health = 10
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        mouseInput = pygame.mouse.get_pressed(num_buttons=3)

        # Horizontal
        if keys[pygame.K_a]:
            self.velocity.x -= 1 + self.extraAcceleration
            self.facing = -1
            # if self.frames % 80 == 0:
            #     self.anim(3, 8, self.facing)
        elif keys[pygame.K_d]:
            self.velocity.x += 1 + self.extraAcceleration
            self.facing = 1
            # if self.frames % 80 == 0:
            #     self.anim(3, 8, self.facing)
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = 0
            # if self.frames % 20 == 0:
            #     self.anim(0, 2, self.facing)

        if keys[pygame.K_SPACE] and self.jumps and not self.jumping:
            self.velocity.y = -PLAYERJUMP
            self.jumps -= 1
            self.jumping = True
            # if self.frames % 80 == 0:
            #     self.anim(5, 8, self.facing)

        if mouseInput[0]:
            if mouse[0] > 640:
                self.facing = 1
            else:
                self.facing = -1

        #Parry
        if keys[pygame.K_e] and not self.cooldown:
            self.parry = 30
            self.cooldown = FPS*3

        self.swapScene = True
        for enemy in self.enemyGroup:
            if not enemy.dead:
                self.swapScene = False

        if self.swapScene:
            self.currentScene += 1
            self.iFrames = FPS*3
            if self.currentScene ==8:
                self.extraJumps += 1
            if self.currentScene ==15:
                self.extraSpeed += 2
        
        #Test if SPACE held
        if not keys[pygame.K_SPACE]:
            self.jumping = False
        self.frames += 1
    def move(self):

        self.anim(0, 1, self.facing)
        self.velocity.y += GRAVITY * self.mass

        if self.velocity.y > self.term:
            self.velocity.y = self.term
        if self.velocity.x > PLAYERSPEED + self.extraSpeed:
            self.velocity.x = PLAYERSPEED + self.extraSpeed
        if self.velocity.x < -PLAYERSPEED - self.extraSpeed:
            self.velocity.x = -PLAYERSPEED - self.extraSpeed

        self.rect.x += self.velocity.x
        self.checkCollisions('x')
        self.rect.y += self.velocity.y
        self.checkCollisions('y')
        self.centerPos = self.rect.centerx
    def checkCollisions(self, dir):
        if dir == 'x': #Blocks
            for block in self.blockGroup:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0:
                        self.rect.right = block.rect.left
                    if self.velocity.x < 0:
                        self.rect.left = block.rect.right
            for enemy in self.enemyGroup: # Enemy collision
                if enemy.rect.colliderect(self.rect) and not self.iFrames:
                    if not self.parry:
                        self.health -= 1
                        if self.frames % 20 == 0:
                            self.anim(1, 2, self.facing)
                        self.iFrames = FPS*2
                    else:
                        self.iFrames = FPS
            for proj in self.projGroup: # Projectile collision
                if proj.rect.colliderect(self.rect) and not self.iFrames and proj.damage and not proj.playerFlag:
                    if not self.parry:
                        self.health -= 1
                        if self.frames % 20 == 0:
                            self.anim(1, 2, self.facing)
                        self.iFrames = FPS
                    else:
                        self.iFrames = FPS*2
        elif dir == 'y':
            for block in self.blockGroup:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0:
                        self.rect.bottom = block.rect.top
                        self.jumps = MAXJUMPS + self.extraJumps
                    if self.velocity.y < 0:
                        self.rect.top = block.rect.bottom
                        self.velocity.y -= self.velocity.y
            if self.parry:
                self.parry -= 1
            #     self.image.fill((0, 0, 100))
            elif self.iFrames:
            #     self.image.fill('purple')
                self.iFrames -= 1
            # else:
            #     self.image.fill('blue')
            if self.cooldown:
                self.cooldown -= 1
    def update(self):
        self.move()
        self.input()
    def anim(self, layer, frameCount, facing):
        for i in range(frameCount*10):
            if self.frames % 10 == 0:
                self.image = self.getImage(self.spritesheet, i//10, layer, 32, 32, facing)
    def getImage(self, sprite, frame, layer, width, height, facing):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sprite, (0, 0), (frame * width, layer*height, width, height))
        image = pygame.transform.scale(image, (TILESIZE*6, TILESIZE*6))
        if facing == -1:
            image = pygame.transform.flip(image, True, False)
        image.set_colorkey((0, 255, 0))
        return image