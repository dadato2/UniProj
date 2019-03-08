from Object import *
from Projectile import Tear

isaacImages = (pygame.image.load("assets/isaac.png"), pygame.image.load("assets/isaacR.png"),
               pygame.image.load("assets/isaacL.png"), pygame.image.load("assets/isaacU.png"))

class Isaac (Object):
    def __init__(self):
        ObjectLists.listAllObjects.append(self)
        self.spriteIndex = 0
        self.sprite = isaacImages[self.spriteIndex]
        self.rect = self.sprite.get_rect()

        self.ypos = 300
        self.xpos = 300
        self.speed = 6
        self.decel = self.speed / 1.5
        self.accel = self.speed / 1.5
        self.xAcc = 0.0
        self.yAcc = 0.0
        self.tempxAcc = 0.0
        self.tempyAcc = 0.0

        self.range = 7
        self.shotspeed = 6
        self.tearheight = 14
        self.tearDelay = 14
        self.tearDelayCounter = self.tearDelay
        self.tearOffset = 12

        self.isShooting = False
        self.pKey = pygame.key.get_pressed()

    def update(self):
        self.pKey = pygame.key.get_pressed()
        # walking:
        self.walk()
        # animate
        self.sprite = isaacImages[self.spriteIndex]
        # shooting:
        self.shooting()

    def shooting(self):
        if self.tearDelayCounter <= self.tearDelay:    # manage delay between tears, if you shoot a tear, the counter resets and regains value over time
            self.tearDelayCounter += Time.deltaTime * 30

        if self.pKey[K_RIGHT]:
            self.spriteIndex = 1
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Right)
                self.tearDelayCounter = 0
        elif self.pKey[K_LEFT]:
            self.spriteIndex = 2
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Left)
                self.tearDelayCounter = 0
        elif self.pKey[K_UP]:
            self.spriteIndex = 3
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Up)
                self.tearDelayCounter = 0
        elif self.pKey[K_DOWN]:
            self.spriteIndex = 0
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Down)
                self.tearDelayCounter = 0

    def walk(self):    # temporary xAcc and yAcc act as acceleration (will add a delay in future)
        self.isShooting = self.pKey[K_UP] or self.pKey[K_DOWN] or self.pKey[K_LEFT] or self.pKey[K_RIGHT]

        if self.pKey[K_d]:  # right
            if self.xAcc < 0:
                self.xAcc = 0
            if self.xAcc < self.speed:
                self.xAcc += self.accel/10
            if self.xpos > Constants.scr_width - 40 - Constants.playerWidth:
                self.xAcc = -0.1
            if not self.isShooting:          # change direction animation
                self.spriteIndex = 1

        if self.pKey[K_a]:  # left
            if self.xAcc > 0:
                self.xAcc = 0
            if self.xAcc > -self.speed:
                self.xAcc -= self.accel/10
            if self.xpos < 40:
                self.xAcc = 0.1
            if not self.isShooting:  # change direction animation
                self.spriteIndex = 2

        if self.pKey[K_w]:  # up
            if self.yAcc > 0:
                self.yAcc = 0
            if self.yAcc > -self.speed:
                self.yAcc -= self.accel/10
            if self.ypos < 40:
                self.yAcc = 0.1
            if not self.isShooting:  # change direction animation
                self.spriteIndex = 3

        if self.pKey[K_s]:  # down
            if self.yAcc < 0:
                self.yAcc = 0
            if self.yAcc < self.speed:
                self.yAcc += self.accel/10
            if self.ypos > Constants.scr_height - 40 - Constants.playerHeight:
                self.yAcc = +0.1
            if not self.isShooting:  # change direction animation
                self.spriteIndex = 0

        if not self.pKey[K_a] and not self.pKey[K_d]:   # manage deceleration for horizontal input
            for i in range(0, int(self.decel)):
                if self.xAcc > 0:
                    self.xAcc -= 0.1
                elif self.xAcc < 0:
                    self.xAcc += 0.1
            if -0.1 <= self.xAcc <= 0.1:
                self.xAcc = 0

        if not self.pKey[K_w] and not self.pKey[K_s]:    # manage deceleration for vertical input
            for i in range(0, int(self.decel)):
                if self.yAcc > 0:
                    self.yAcc -= 0.1
                elif self.yAcc < 0:
                    self.yAcc += 0.1
            if -0.1 <= self.yAcc <= 0.1:
                self.yAcc = 0

        if self.yAcc != 0 and self.xAcc != 0:
            self.tempyAcc = self.yAcc * 0.7071   # normalize diagonal movement
            self.tempxAcc = self.xAcc * 0.7071
        else:
            self.tempxAcc = self.xAcc   # if not diagonal set temp values to acceleration
            self.tempyAcc = self.yAcc   # the temp values are here only to normalize the diagonal movement btw

        self.xpos += int(self.tempxAcc)
        self.ypos += int(self.tempyAcc)

        # reset direction animation:
        if not self.pKey[K_a] and not self.pKey[K_d] and not self.pKey[K_s] and not self.pKey[K_w]:
            if not self.isShooting:
                self.spriteIndex = 0

    def shoot(self, direction):
        self.tearOffset = -self.tearOffset
        new_tear = Tear(direction, self)


    def draw(self, screen):
        screen.blit(self.sprite, (self.xpos, self.ypos))
