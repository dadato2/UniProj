from Object import *
import random

enemyImage = (pygame.image.load("assets/fly1.png"), pygame.image.load("assets/fly2.png"),
              pygame.image.load("assets/fly3.png"), pygame.image.load("assets/fly4.png"))


class Enemy (Object):
    def __init__(self, x, y):
        ObjectLists.listAllObjects.append(self)
        ObjectLists.listOfEnemies.append(self)

        self.imageIndex = random.randrange(0, 4)
        self.animationTimer = 0.0
        self.animationDelay = 0.04
        self.sprite = enemyImage[self.imageIndex]
        self.enemyBuzz = Global.Sounds.insect_swarm

        self.hp = 10
        self.maxSpeed = 2.5
        self.speed = 0
        self.xpos = x
        self.ypos = y
        self.directionPlayer = 0
        self.distancePlayer = 0
        self.dirx = 0
        self.diry = 0
        self.canMove = 1
        self.soundLooper = random.random()

        self.squareSize = 33
        self.order = self.ypos + self.squareSize * 2 - 22
        self.offsetXpos = self.xpos
        self.offsetYpos = self.ypos

        self.hitByTear = False
        self.rect = Rect(self.xpos, self.ypos+10, 24, 24)

    def update(self):
        if self.soundLooper > 0:
            self.soundLooper -= Time.deltaTime
        else:
            pygame.mixer.Channel(1).play(self.enemyBuzz)
            # self.enemyBuzz.play()
            self.soundLooper = 0.6

        self.distancePlayer = math.sqrt(math.fabs((self.xpos - Global.player.xpos) * (self.xpos - Global.player.xpos) + (
                    self.ypos - Global.player.ypos) * (self.xpos - Global.player.xpos)))

        if self.speed < self.maxSpeed:
            self.speed += Time.deltaTime
        if self.canMove > 0:
            self.canMove -= Time.deltaTime
        if self.hp <= 0:
            Constants.enemycount -= 1
            self.enemyBuzz.stop()
            ObjectLists.listOfEnemies.remove(self)
            ObjectLists.listAllObjects.remove(self)
        self.rect = Rect(self.xpos, self.ypos, self.squareSize, self.squareSize)
        self.animate()

        if self.canMove <= 0 and self.distancePlayer >=30:
            self.moveTowardPlayer()


    def buzz(self):
        self.offsetXpos = self.xpos + random.randrange(-3, 3)
        self.offsetYpos = self.ypos + random.randrange(-3, 3)

    def moveTowardPlayer(self):
        self.directionPlayer = GlobalMath.AnglePlayer(self)
        self.dirx = math.sin(self.directionPlayer) * self.speed
        self.diry = math.cos(self.directionPlayer) * self.speed

        self.xpos = int(self.xpos + self.dirx)
        self.ypos = int(self.ypos + self.diry)

        self.enemyCollision()

    def enemyCollision(self):
        for fly in ObjectLists.listOfEnemies:
            if self.rect.colliderect(fly.rect):
                if fly.ypos <= self.ypos <= fly.ypos + fly.squareSize/2 and fly.xpos < self.xpos <= fly.xpos + fly.squareSize:
                    self.ypos += self.speed
                    fly.ypos -= fly.speed
                elif fly.ypos + fly.squareSize/2 > self.ypos >= fly.squareSize and fly.xpos < self.xpos <= fly.xpos + fly.squareSize:
                    self.ypos -= self.speed
                    fly.ypos += fly.speed
                if fly.xpos <= self.xpos <= fly.xpos + fly.squareSize/2 and fly.ypos < self.ypos <= fly.ypos + fly.squareSize:
                    self.xpos += self.speed
                    fly.xpos -= fly.speed
                elif fly.xpos + fly.squareSize/2 > self.xpos >= fly.squareSize and fly.ypos < self.ypos <= fly.ypos + fly.squareSize:
                    self.xpos -= self.speed
                    fly.xpos += fly.speed

    def animate(self):
        self.animationTimer += Time.deltaTime
        if self.animationTimer >= self.animationDelay:
            if self.imageIndex < len(enemyImage)-1:
                self.imageIndex += 1
                self.buzz()
            else:
                self.imageIndex = 0
                self.buzz()
            self.animationTimer = 0
        self.sprite = enemyImage[self.imageIndex]

    def draw(self, screen):
        screen.blit(self.sprite, (self.offsetXpos, self.offsetYpos))
