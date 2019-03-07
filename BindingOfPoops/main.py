import sys
from Player import *

scr_width = 1080
scr_height = 720
fps = 60

lastTime = 0
nowTime = 0

caption = "The Binding of Poops"
iconImage = "icon.png"
roomImage = pygame.image.load("assets/room.png")
# enemyImage = ("enemy.png")


pygame.init()
time = pygame.time.Clock()
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((scr_width, scr_height))
gameIcon = pygame.image.load(iconImage)
pygame.display.set_icon(gameIcon)

player = Isaac()
while True:                 # M A I N

    nowTime = pygame.time.get_ticks()
    Time.deltaTime = (nowTime-lastTime) / 1000
    lastTime = nowTime
    time.tick(fps)
    pKey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    screen.blit(roomImage, (0, 0))

    for item in ObjectLists.listAllObjects:
        item.update()
        item.draw(screen)
