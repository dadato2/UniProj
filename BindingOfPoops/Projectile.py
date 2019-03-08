from Object import *

tearSprite = pygame.image.load("assets/tear.png")
class Tear (Object):
    def __init__(self, direction, player):

        ObjectLists.listAllObjects.append(self)
        ObjectLists.listOfTears.append(self)

        self.xpos = player.xpos + 16
        self.ypos = player.ypos + 40
        self.sprite = tearSprite
        self.rect = Rect(self.xpos, self.ypos, 24, 24)
        self.tearHeight = player.tearheight       # tear height will affect how high the tear is drawn and also determines how much time left it has
        self.range = player.range
        self.shotspeed = player.shotspeed
        self.shotSpeedOffset = 3
        self.offsetMultiplier = 1.5
        self.lifeEnded = False
        if direction == directions.Up:
            self.xpos += player.tearOffset
            self.speedx = (player.xAcc / self.shotSpeedOffset) * self.offsetMultiplier
            self.speedy = -self.shotspeed + player.yAcc / self.shotSpeedOffset

        elif direction == directions.Down:
            self.xpos += player.tearOffset
            self.speedx = (player.xAcc / self.shotSpeedOffset) * self.offsetMultiplier
            self.speedy = self.shotspeed + player.yAcc / self.shotSpeedOffset

        elif direction == directions.Left:
            self.ypos += player.tearOffset
            self.speedx = -self.shotspeed + player.xAcc / self.shotSpeedOffset
            self.speedy = (player.yAcc / self.shotSpeedOffset) * self.offsetMultiplier

        elif direction == directions.Right:
            self.ypos += player.tearOffset
            self.speedx = self.shotspeed + player.xAcc / self.shotSpeedOffset
            self.speedy = (player.yAcc / self.shotSpeedOffset) * self.offsetMultiplier

    def update(self):
        self.rect = Rect(self.xpos, self.ypos, 24, 24)
        self.tearHeight -= (10/(self.tearHeight / (20-self.range)))/100
        self.xpos += self.speedx
        self.ypos += self.speedy
        if self.xpos < 40 or self.xpos > Constants.scr_width - 40 or self.ypos < 40 or self.ypos > Constants.scr_height - 40:
            self.tearHeight = 0.01
        if self.tearHeight <= 0.01:
            ObjectLists.listAllObjects.remove(self)     # test and see if it does sth. if not, do the other way (loop through all objects and remove the ones that are dead)
            ObjectLists.listOfTears.remove(self)

    def draw(self, screen):
        screen.blit(self.sprite, (self.xpos, self.ypos - int(self.tearHeight*2)))
