from Object import *
from Projectile import Tear

tmpisaacHead = makeSprite("assets/isaacHead.png", 8)
isaacHead = tmpisaacHead.images
tmpisaacBody = makeSprite("assets/isaacBody.png", 30)
isaacBody = tmpisaacBody.images

class Isaac (Object):
    def __init__(self):
        ObjectLists.listAllObjects.append(self)
        self.spriteIndexHead = 0
        self.spriteHead = isaacHead[self.spriteIndexHead]
        self.spriteIndexBody = 0
        self.spriteIndexAddTen = 0
        self.spriteBody = isaacBody[self.spriteIndexBody]
        self.spriteIndexBodyDelay = 0
        
        self.rect = self.spriteHead.get_rect()
        self.Sound_tear_1 = Global.Sounds.player_tear_1

        self.ypos = 300
        self.xpos = 300
        self.squareSize = 66
        self.order = self.ypos + self.squareSize
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
        self.tearAnimTimer = 0

        self.isShooting = False
        self.pKey = pygame.key.get_pressed()

    def update(self):
        self.pKey = pygame.key.get_pressed()
        # reset sprite
        if self.tearAnimTimer > 0:
            self.tearAnimTimer -= Time.deltaTime

        if self.spriteIndexHead % 2 != 0 and self.tearAnimTimer <= 0:
            self.spriteIndexHead -= 1
        # walking:
        self.walk()
        # shooting:
        self.shooting()
        # set sprite
        self.animateBody()
        self.spriteHead = isaacHead[self.spriteIndexHead]
        if 0 <= self.spriteIndexBody + self.spriteIndexAddTen < 30:
            self.spriteBody = isaacBody[self.spriteIndexBody + self.spriteIndexAddTen]
        else:
            if self.spriteIndexBody + self.spriteIndexAddTen < 0:
                self.spriteBody = isaacBody[0]
            if self.spriteIndexBody + self.spriteIndexAddTen >= 30:
                self.spriteBody = isaacBody[29]

    def animateBody(self):
        if self.spriteIndexBodyDelay > 0:
            self.spriteIndexBodyDelay -= Time.deltaTime

        if self.spriteIndexBodyDelay <= 0:
            if not self.yAcc < 0:
                self.spriteIndexBody = (self.spriteIndexBody+1) % 10
            else:
                if self.spriteIndexBody > 0:
                    self.spriteIndexBody -= 1
                else:
                    self.spriteIndexBody = 10
        if self.spriteIndexBody > 10:
            self.spriteIndexBody = 10
        if -0.05 < self.tempxAcc <= 0.05 and -0.05 < self.tempyAcc <= 0.05:
            self.spriteIndexAddTen = 0
            self.spriteIndexBody = 0

        if math.fabs(self.tempxAcc) > math.fabs(self.tempyAcc):
            if self.tempxAcc < 0:
                self.spriteIndexAddTen = 20
                if self.spriteIndexBodyDelay <= 0:
                    self.spriteIndexBodyDelay = 0.1-(math.fabs(self.tempxAcc) / self.accel)/100
            if self.tempxAcc > 0:
                self.spriteIndexAddTen = 10
                if self.spriteIndexBodyDelay <= 0:
                    self.spriteIndexBodyDelay = 0.1-(math.fabs(self.tempxAcc) / self.accel)/100
        else:
            self.spriteIndexAddTen = 0
            if self.spriteIndexBodyDelay <= 0:
                self.spriteIndexBodyDelay = 0.1-(math.fabs(self.tempyAcc) / self.accel)/100

        if self.spriteIndexBody > 10:
            self.spriteIndexBody = 10
        if self.spriteIndexBody < 0:
            self.spriteIndexBody = 0

    def walk(self):    # temporary xAcc and yAcc act as acceleration (will add a delay in future)
        self.isShooting = self.pKey[K_UP] or self.pKey[K_DOWN] or self.pKey[K_LEFT] or self.pKey[K_RIGHT]

        if self.pKey[K_d]:  # right
            if self.xAcc < 0:
                self.xAcc = 0
            if self.xAcc < self.speed:
                self.xAcc += self.accel/10
            if self.xpos > Constants.scr_width - 40 - Constants.playerWidth:
                self.xAcc = -0.01
            if not self.isShooting and self.tearAnimTimer <=0:          # change direction animation
                self.spriteIndexHead = 2

        if self.pKey[K_a]:  # left
            if self.xAcc > 0:
                self.xAcc = 0
            if self.xAcc > -self.speed:
                self.xAcc -= self.accel/10
            if self.xpos < 40:
                self.xAcc = 0.1
            if not self.isShooting and self.tearAnimTimer <= 0:  # change direction animation
                self.spriteIndexHead = 6

        if self.pKey[K_w]:  # up
            if self.yAcc > 0:
                self.yAcc = 0
            if self.yAcc > -self.speed:
                self.yAcc -= self.accel/10
            if self.ypos < 40:
                self.yAcc = 0.1
            if not self.isShooting and self.tearAnimTimer <= 0:  # change direction animation
                self.spriteIndexHead = 4

        if self.pKey[K_s]:  # down
            if self.yAcc < 0:
                self.yAcc = 0
            if self.yAcc < self.speed:
                self.yAcc += self.accel/10
            if self.ypos > Constants.scr_height - 40 - Constants.playerHeight:
                self.yAcc = +0.1
            if not self.isShooting and self.tearAnimTimer <= 0:  # change direction animation
                self.spriteIndexHead = 0

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
            if not self.isShooting and self.tearAnimTimer <= 0:
                self.spriteIndexHead = 0
            self.spriteIndexBody = 0

    def shooting(self):
        if self.tearDelayCounter <= self.tearDelay:    # manage delay between tears, if you shoot a tear, the counter resets and regains value over time
            self.tearDelayCounter += Time.deltaTime * 30

        if self.pKey[K_RIGHT]:
            if self.tearAnimTimer <= 0:
                self.spriteIndexHead = 2
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Right)
                self.tearDelayCounter = 0

        elif self.pKey[K_LEFT]:
            if self.tearAnimTimer <= 0:
                self.spriteIndexHead = 6
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Left)
                self.tearDelayCounter = 0

        elif self.pKey[K_UP]:
            if self.tearAnimTimer <= 0:
                self.spriteIndexHead = 4
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Up)
                self.tearDelayCounter = 0

        elif self.pKey[K_DOWN]:
            if self.tearAnimTimer <= 0:
                self.spriteIndexHead = 0
            if self.tearDelayCounter >= self.tearDelay:
                self.shoot(directions.Down)
                self.tearDelayCounter = 0

    def shoot(self, direction):
        self.tearOffset = -self.tearOffset
        self.Sound_tear_1.play()
        if self.spriteIndexHead % 2 == 0:
            self.spriteIndexHead += 1
            self.tearAnimTimer = 0.2
        new_tear = Tear(direction, self)


    def draw(self, screen):
        screen.blit(self.spriteBody, (self.xpos+10, self.ypos+39))
        screen.blit(self.spriteHead, (self.xpos, self.ypos))
