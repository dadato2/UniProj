from Object import *

tearSprite = pygame.image.load("assets/tear.png")
class Tear (Object):
    def __init__(self, direction, player):

        self.xpos = player.xpos + 20
        self.ypos = player.ypos + 40
        self.sprite = tearSprite
        self.rect = self.sprite.get_rect()
        self.tearHeight = player.tearheight       # tear height will affect how high the tear is drawn and also determines how much time left it has
        self.shotSpeedOffset = 5
        self.range = player.rangeof
        self.shotspeed = player.shotspeed
        self.lifeEnded = False
        if direction == directions.Up:
            self.speedx = 0
            self.speedy = -self.shotspeed + player.yAcc / self.shotSpeedOffset
        elif direction == directions.Down:
            self.speedx = 0
            self.speedy = self.shotspeed + player.yAcc / self.shotSpeedOffset
        elif direction == directions.Left:
            self.speedx = -self.shotspeed + player.xAcc / self.shotSpeedOffset
            self.speedy = 0
        elif direction == directions.Right:
            self.speedx = self.shotspeed + player.xAcc / self.shotSpeedOffset
            self.speedy = 0

    def update(self):
        self.tearHeight -= (10/(self.tearHeight / (20-self.range)))/100
        self.xpos += self.speedx
        self.ypos += self.speedy
        if self.tearHeight <= 0.01:
            ObjectLists.listAllObjects.remove(self)     # test and see if it does sth. if not, do the other way (loop through all objects and remove the ones that are dead)
            ObjectLists.listOfTears.remove(self)

    def draw(self, screen):
        screen.blit(self.sprite, (self.xpos, self.ypos - int(self.tearHeight*2)))
