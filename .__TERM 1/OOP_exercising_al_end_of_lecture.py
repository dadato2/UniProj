from os import system
system('cls')

charachter = '@'
posx = 3
posy = 2
map_origin = [['#','#','#','#','#','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#',' ',' ',' ',' ','#'],
              ['#','#','#','#','#','#']]
class Collectables():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
def moveme(direction):
    global posx, posy
    if direction == "up":
        if map_origin[posx-1][posy] != '#':
            posx -= 1
    if direction == "down":
        if map_origin[posx+1][posy] != '#':
            posx += 1
    if direction == "left":
        if map_origin[posx][posy-1] != '#':
            posy -= 1
    if direction == "right":
        if map_origin[posx][posy+1] != '#':
            posy += 1

def printmap(that):
    for a in that:
        print(a)


mapp = map_origin
system('cls')
mapp[posx][posy] = charachter
printmap(mapp)
while True:
    mapp = map_origin
    mapp[posx][posy] = charachter
    printmap(mapp)

    move = input('move: ')
    moveme(move)

    system('cls')
