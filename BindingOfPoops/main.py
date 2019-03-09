import sys, operator
from Player import *
from Enemy import *
from Debug import *

lastTime = 0
nowTime = 0

caption = "The Binding of Poops"
iconImage = "icon.png"
roomImage = pygame.image.load("assets/room.png")


pygame.init()
pygame.mixer.init()
time = pygame.time.Clock()
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((Constants.scr_width, Constants.scr_height))
gameIcon = pygame.image.load(iconImage)
pygame.display.set_icon(gameIcon)
Debug = debug()
Global.Sounds = sounds()

player = Isaac()
Global.player = player

for i in range(10, 20):
    enemy = Enemy(random.randrange(40, Constants.scr_width - 40), random.randrange(40, Constants.scr_height - 40))
    Constants.enemycount += 1

while True:                 # M A I N   L O O P
    nowTime = pygame.time.get_ticks()
    Time.deltaTime = (nowTime-lastTime) / 1000
    lastTime = nowTime
    time.tick(Constants.fps)
    pKey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    screen.blit(roomImage, (0, 0))
    if pKey[K_ESCAPE]:
        sys.exit()

    if Constants.enemycount <= 0:
        Debug.Log("YOU WIN!")
    else:
        Debug.Log(Constants.enemycount)

    ObjectLists.listAllObjects.sort(key=operator.attrgetter('order'))

    for item in ObjectLists.listAllObjects:
        item.update()
        item.draw(screen)

    screen.blit(Debug.debugtextsurface, (10, 10))
