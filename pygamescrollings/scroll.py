import sys, pygame

pygame.init()

width = 1280
height = 720
colour = 200, 0, 0

pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
boop = pygame.mixer.Sound("boop.wav")

pygame.mixer.Sound("nokia.wav").play()

bg = pygame.image.load("background.jpg")

maxlives = 5
lives = 5

xpos = 400
ypos = 400
xsiz = 100
ysiz = 200


class Background():
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.xSize = 1022
        self.speed = 1

    def update(self):
        self.xpos -= 1
        if self.xpos <= -self.xSize:
            self.xpos = self.xSize

    def draw(self):
        screen.blit(bg, (self.xpos, self.ypos))


time = pygame.time.Clock()
bg1 = Background(0, 0)
bg2 = Background(1022, 0)
pKey = pygame.key.get_pressed()
while 1:
    time.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    bg1.update()
    bg2.update()
    bg1.draw()
    bg2.draw()

    pygame.draw.rect(screen, (255, 0, 0), (xpos, ypos, xsiz, ysiz))

    pKey = pygame.key.get_pressed()
    if pKey[pygame.K_RIGHT]:
        if xpos < width:
            xpos += 3
        else:
            xpos = -xsiz
            lives -= 1
            boop.play()
    if pKey[pygame.K_LEFT]:
        if xpos > -xsiz:
            xpos -= 3
        else:
            xpos = width
            lives -= 1
            boop.play()
    if pKey[pygame.K_DOWN]:
        if ypos < height:
            ypos += 3
        else:
            ypos = -ysiz
            lives -= 1
            boop.play()
    if pKey[pygame.K_UP]:
        if ypos > -ysiz:
            ypos -= 3
        else:
            ypos = height
            lives -= 1
            boop.play()
    if lives < 0:
        lives =0
    pygame.draw.rect(screen, (255-lives/maxlives*255, lives/maxlives*255, 0), (0, 0, (lives/maxlives*400), 30))
    pygame.display.update()
