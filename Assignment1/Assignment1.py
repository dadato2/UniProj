import sys
from os import system
import time
import random
system('cls')


# Functions
def newprint(a):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print("")


def attack(name, hp, damage, defence, turn, monsterSprite):
    system('cls')
    if monsterSprite == 0:
        print(monster1)
        newprint("A wild " + name + " has appeared!")
    while True:
        if hp <= 0:
            break
        #Player's Turn
        if turn == True:
            randomWaitMe = random.randrange(0, 10)
            if randomWaitMe == 0:
                newprint("The " + name + " looks like it wants to eat you.")
            elif randomWaitMe == 1:
                newprint("The " + name + " waits in anticipation.")
            elif randomWaitMe == 2:
                newprint("The " + name + " tells its family that the battle will be over soon.")
            elif randomWaitMe == 3:
                newprint("The " + name + " remembers all of its happy moments.")
            elif randomWaitMe == 4:
                newprint("The " + name + " gives out a chilling battlecry.")
            elif randomWaitMe == 5:
                newprint("The " + name + " looks pretty bored waiting for your turn.")
            elif randomWaitMe == 6:
                newprint("The " + name + " has never seen someone who looks as scared as you.")
            elif randomWaitMe == 7:
                newprint("The " + name + " will tell its friends how it defeated you.")
            elif randomWaitMe == 8:
                newprint("The " + name + " was about to open a small business before it stumbled into you.")
            elif randomWaitMe == 9:
                newprint("The " + name + " just remembered a joke its son said the other day.")
            elif randomWaitMe == 10:
                newprint("The " + name + " is eagerly awaiting your move.")
            action = input()

        #Enemy Turn
            enemyAction = random.randrange(0, 4)
            if enemyAction == 0:
                defence += 1




# constants
action = ''
error = 'Command not available. You can type "help" for example options.'
listYes = ("yes", "yep","ya","noice","yas","yaas","yaaas","yaaaas","yaaaaas","correct", "yee", "ye", "yuhuh", "y", "ok", "okey dokey","okie dokie","positive")
listNo = ("no","nope","n","nuhuh","newp","negative","nein","nicht","never")
listCheckINv = ("check inv", "inv","check inventory","inventory")

# Health and vitals
thirst = 10   # max 10
hunger = 10   # max 10
maxHealth = 10
health = 10
attack = 4

# Resources
water = 2
food = 1
acorns = 0
sticks = 0
matches = 0
flowers = 0

# Monsters
monster1 = "\n  ,/         \\.\n" " ((           ))\n" "   )')     (`(\n" " ,'`/       \\,`.\n" " \\-'\\,-'*`-./`-/\n" "  \\-')     (`-/\n" "  /`'       `'\\\n" " (   _      _  )\n" " |  `.\\   /,'  |\n" " |    `\\ /'    |\n" "  \\           /\n" "   \\         /\n" "    `.     ,'\n" "      `-.-'\n"

# Start of story.
newprint('You have been travelling for a long time. You have two water bottles and a sandwich.'
         '\nYou can not see the end of the road. '
         '\nYou are thirsty and hungry.')

while True:
    newprint("What do you do: ")
    action = str(input('- '))

    if action == "walk" or action == "run":
        newprint("You are hungry and thirsty. Walking seems difficult at the moment.")
        newprint("Available resources: ")
        print("water: ", water)
        print("food: ", food)

    elif action == 'drink' or action == 'drink water':
        newprint("You drink the water.")
        water -= 1
        break

    elif action == 'eat' or action == 'eat sandwich' or action == 'eat food':
        newprint("You eat the food.")
        food -= 1
        break

    elif action == 'rest' or action == 'sit' or action == 'sleep':
        newprint('You can\'t rest now. You have a long trip ahead of you.')

    elif action == 'help' or action == 'help me':
        newprint('Try eating some food or drinking some water\n' 
                 'to regain some energy.')
    else:
        newprint(error)
newprint("\nYou continue walking. along the way you find some acorns. You can shoot them with your slingshot.\nPick them up?")
while True:
    action = input('- ')
    isDone = False
    for a in listYes:
        if action == a:
            hence = random.randrange(5, 10)
            acorns += hence
            newprint("You picked up " + str(hence) + " acorns")
            isDone = True
    if isDone:
        break
    for a in listNo:
        if action == a:
            hence = random.randrange(5, 10)
            acorns += hence
            newprint("You remember that you already had " + str(hence) + " acorns.")
            isDone = True
    if isDone:
        break
    if action == "help":
        newprint("This is a yes or no question.")
    else:
        newprint(error)
newprint("\nWhile thinking about practicing your slingshot skills, you notice a presence around you.\n"
         "You look to your right and see a peculiar face watching you.")
attack("rabbit", 10, 0, 0, True, 0)


