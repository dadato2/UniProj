from Object import *
import random

# """

enemyImage = (pygame.image.load("assets/fly1.png"), pygame.image.load("assets/fly2.png"),
              pygame.image.load("assets/fly3.png"), pygame.image.load("assets/fly4.png"))

class Enemy (Object):
    def __init__(self, x, y):
        ObjectLists.listAllObjects.append(self)
        ObjectLists.listOfEnemies.append(self)

        self.imageIndex = 0
        self.animationTimer = 0.0
        self.animationDelay = 0.08
        self.sprite = enemyImage[self.imageIndex]

        self.hp = 10
        self.xpos = x
        self.ypos = y
        self.offsetXpos = self.xpos
        self.offsetYpos = self.ypos

        self.hitByTear = False
        self.rect = Rect(self.xpos, self.ypos+10, 24, 24)
        self.speed = 3

    def update(self):
        if self.hp <= 0:
            ObjectLists.listOfEnemies.remove(self)
            ObjectLists.listAllObjects.remove(self)
        self.rect = Rect(self.xpos, self.ypos, 24, 24)
        self.animate()
        # follow Player
        self.collide()

    def buzz(self):
        self.offsetXpos = self.xpos + random.randrange(-3, 3)
        self.offsetYpos = self.ypos + random.randrange(-3, 3)

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

    def collide(self):
        for tear in ObjectLists.listOfTears:
            if self.rect.colliderect(tear.rect):
                tear.tearHeight = 0.1
                self.hp -= 5

    def draw(self, screen):
        screen.blit(self.sprite, (self.offsetXpos, self.offsetYpos))
# """
