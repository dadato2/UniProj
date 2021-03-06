import sys, pygame, random, math
from pygame.locals import *

scr_width = 820
scr_height = 560

cloudImage = "cloud.png"
umbrellaImage = ("umbrella.png", "umbrella2.png")
umbrellaImageIndex = 0
newintforumbrellathing = 0

dotSize = 4
# xpos = random.randrange(dotSize, scr_width-dotSize)
# ypos = -dotSize
sortoftimepassed = 0

listAllObjects = []
listOfSnowFlakes = []
listOfClouds = []


class Color:
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    yellow = 255, 255, 0
    green = 0, 255, 0
    cyan = 0, 255, 255
    blue = 0, 0, 255
    water = 90, 240, 255
    magenta = 255, 0, 255
    gray_very_light = 200, 200, 200
    gray_light = 175, 175, 175
    gray_dark = 75, 75, 75
    gray_very_dark = 50, 50, 50

class Object:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw (self):
        pass


class Cloud (Object):
    def __init__(self):
        self.cloud = pygame.image.load(cloudImage)
        self.cloudRect = self.cloud.get_rect()
        self.xpos = random.randrange(-self.cloudRect.width, scr_width-self.cloudRect.width)
        self.ypos = random.randrange(-100, -10)
        self.speed = random.randrange(1, 2)
        self.sizeX = 100

    def update(self):
        if self.xpos > scr_width:
            self.xpos = -self.cloudRect.width
        self.xpos += self.speed

    def draw(self):
        screen.blit(self.cloud, (self.xpos, self.ypos))


class Snowflake (Object):
    def __init__(self):
        self.timepassed = random.randrange(0, 180)
        self.dotSize = random.randrange(1, 5)
        self.speedy = round(dotSize/2)
        self.xpos = random.randrange(0, scr_width)
        self.ypos = random.randrange(-self.dotSize, scr_height)
        self.rect = pygame.Rect(self.xpos, self.ypos, self.dotSize, self.dotSize)

    def update(self):
        self.timepassed += 0.1
        if self.ypos >= scr_height + self.dotSize or umbrellaCollision(self.xpos+self.dotSize/2, self.ypos+self.dotSize/2):
            self.newCloud = listOfClouds[random.randrange(0, len(listOfClouds))]
            self.xpos = random.randrange(self.newCloud.xpos, self.newCloud.xpos+self.newCloud.cloudRect.width)
            self.ypos = -self.dotSize
        self.ypos += self.speedy
        self.xpos += round(math.sin(self.timepassed))
        self.rect = pygame.Rect(self.xpos, self.ypos, self.dotSize, self.dotSize)

    def draw(self):
        pygame.draw.circle(screen, Color.white, (self.xpos, self.ypos), self.dotSize, self.dotSize)


class Umbrella (Object):
    def __init__(self):
        global umbrellaRect
        self.ypos = 300
        self.xpos = 300
        self.umbrella = pygame.image.load(umbrellaImage[umbrellaImageIndex])
        umbrellaRect = self.umbrella.get_rect()

    def update(self):
        global pKey, newintforumbrellathing, umbrellaImageIndex
        if newintforumbrellathing<=0:
            umbrellaImageIndex = 1
        self.umbrella = pygame.image.load(umbrellaImage[umbrellaImageIndex])
        if pKey[K_RIGHT]:
            self.xpos += 2
        if pKey[K_LEFT]:
            self.xpos -= 2
        self.xpos += int(math.sin(sortoftimepassed)*10)

    def draw(self):
        screen.blit(self.umbrella, (self.xpos, self.ypos))


def umbrellaCollision(xpos, ypos):
    global umbcentX, umbcentY, umbrellaImageIndex, newintforumbrellathing
    umbcentX = imbrella.xpos + 130
    umbcentY = imbrella.ypos + 118
    distfromcent = int(math.sqrt(((math.fabs(umbcentX-xpos))*(math.fabs(umbcentX-xpos)))+((math.fabs(umbcentY-ypos))) * (math.fabs(umbcentY-ypos))))
    if distfromcent < 130:
        umbrellaImageIndex = 0
        newintforumbrellathing = 100
    if distfromcent < 120:
        return True
    else:
        return False


def createUmbrella():
    global imbrella
    imbrella = Umbrella()
    listAllObjects.append(imbrella)


pygame.init()
time = pygame.time.Clock()
pygame.display.set_caption("Neverending Stories")
screen = pygame.display.set_mode((scr_width, scr_height))
a = pygame.image.load('icon.png')
pygame.display.set_icon(a)
for a in range(0, 200):
    newFlake = Snowflake()
    listAllObjects.append(newFlake)
    listOfSnowFlakes.append(newFlake)

for a in range(0, 1):
    newCloud = Cloud()
    listAllObjects.append(newCloud)
    listOfClouds.append(newCloud)
createUmbrella()
while True:                 # M A I N
    time.tick(60)
    if newintforumbrellathing > 0:
        newintforumbrellathing -= 1
    pKey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    screen.fill(Color.gray_dark)
    for item in listAllObjects:
        item.update()
        item.draw()

    # screen.blit(logo, logoBox)
    pygame.display.flip()
    sortoftimepassed += 0
