import sys
from os import system
import time
import random
system('cls')

# constants
action = ''
error = 'Command not available. You can type "help" for example options.'
listDirections = ("up", "down", "left", "right", "north", "south", "east", "west")
listYes = ("yes", "yep", "ya", "noice", "yas", "yaas", "yaaas", "yaaaas", "yaaaaas",
           "correct", "yee", "ye", "yuhuh", "y", "ok", "okey dokey","okie dokie","positive")
listNo = ("no", "nope", "n", "nuhuh", "newp", "negative", "nein", "nicht", "never")
listCheckINv = ("check inv", "inv", "check inventory", "inventory")
listOfItems = ["honey", "sheep", "flower", "cheese", "carrot", "angelic power"]
listItems = []
listMonsters = ("rabbit", "bee", "rat", "bear", "wolf", "devil")
weaknessDictionary = {"rabbit": "carrot", "bee": "flower", "rat": "cheese", "bear": "honey", "wolf": "sheep",
                      "devil": "angelic power"}
spriteDictionary = {"rabbit": 0, "bee": 1, "rat": 2, "bear": 3, "wolf": 4, "devil": 5}

listYouDoAction = ["You pass by", "You see", "You can smell", "You are imagining", "You have been spotted by",
                   "You think you saw", "Behind you there is", "You are fascinated by", "You have read in a book about",
                   "You really want to tell your friends about"]
listYouDoAdjective = ["an adorable", "an old", "a rustic", "a funny-looking", "a friendly", "a terrifying", "a haunted",
                      "the only existing", "a fake", "a gooey", "a dancing", "a floating", "a blue", "a red",
                      "a strangely shaped", "a green", "a transparent"]
listYouDoObject = ["donkey", "well", "rubick's cube", "picture of Mona Lisa", "thing", "knight", "monster", "friend",
                   "television", "cellphone", "pirate", "goop", "cloud", "grass", "sword", "youtube video", "card",
                   "card game", "rhetoric question", "smelly sock", "flamingo", "gaming console", "rock"]
listYouDoPlace = ["inside of", "right next to", "that looks like", "above", "that reminds you of", "under",
                  "studying about", "reading a book about", "talking to", "looking at you from",
                  "that your mother gave you when you both saw", "that you will remember as if it was"]
listYouDoNextObject = ["a mountain", "the sky", "a museum", "a cloud", "a video game", "you", "a gnome's hat",
                       "a cave", "a river", "the Milky Way", "a bird's nest", "the forest you were in just now",
                       "a peculiar mushroom", "a computer desk", "a deadly bomb", "a wizard", "a deck of cards"]
firstSling = True    # True


# difficulty
maxEnemyHP = 10
maxEnemyDamage = 1
maxEnemyDefence = 0

# Health and vitals
thirst = 10   # max 10
hunger = 10   # max 10
maxHealth = 10
health = 10
attackDamage = 4
attackDefence = 0
wins = 0
turn = True

# Resources
water = 2
food = 1
acorns = 1
sticks = 0
matches = 0
flowers = 0

# Monsters
monsterimages = {0: "             ,\\\n             \\\\\\,_\n              \\` ,\\\n         __,.-\" =__)\n       .\"        )\n    ,_/   ,    \\/\\_\n    \\_|    )_-\\ \\_-`\n       `-----` `--`\n",
                 1: "                .\' \'.            __\n       .        .   .           (__\_\n        .         .         . -{{_(|8)\n          ' .  . ' ' .  . '     (__/\n",
                 2: "              _..----.._    _\n            .\'  .--.    \"-.(0)_\n\'-.__.-\'\"\'=:|   ,  _)_ \\__ . c\\\'-..\n             \'\'\'------\'---\'\'---\'-\"\n",
                 3: "    .--.              .--.\n   : (\\ \". _......_ .\" /) :\n    \\'.    `        `    .\'\n     /\'   _        _   `\\\n    /     0}      {0     \\\n   |       /      \\       |\n   |     /\'        `\     |\n    \\   | .  .==.  . |   /\n     \'._ \\.\' \\__/ \'./ _.\'\n     /  ``\'._-\'\'-_.\'``  \\\n",
                 4: "                        ,     ,\n                        |\\---/|\n                       /  , , |\n                  __.-\'|  / \\ /\n         __ ___.-\'        ._O|\n      .-\'  \'        :      _/\n     / ,    .        .     |\n    :  ;    :        :   _/\n    |  |   .\'     __:   /\n    |  :   /\'----\'| \\  |\n    \\  |\\  |      | /| |\n     \'.\'| /       || \\ |\n     | /|.\'       \'.l \\\\_\n     || ||             \'-\'\n     \'-\'\'-\'\n",
                 5: "\n  ,/         \\.\n" " ((           ))\n" "   )')     (`(\n" " ,'`/       \\,`.\n" " \\-'\\,-'*`-./`-/\n" "  \\-')     (`-/\n" "  /`'       `'\\\n" " (   _      _  )\n" " |  `.\\   /,'  |\n" " |    `\\ /'    |\n" "  \\           /\n" "   \\         /\n" "    `.     ,'\n" "      `-.-'\n",
                 6: ""}
# all ascii art taken from https://www.asciiart.eu/

# Functions
def newprint(a):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print("")


def yesorno():
    while True:
        yesornope = input()
        if yesornope == "help":
            newprint("It's a yes or no question.")
            continue
        for itemyon in listYes:
            if itemyon == yesornope:
                return True
        for itemyon in listNo:
            if itemyon == yesornope:
                return False
        newprint(error)


def defenceatatart():
    if maxEnemyDefence > 3:
        return maxEnemyDefence - random.randrange(1, maxEnemyDefence/2)
    else:
        return 0


def showweakness(name):
    if name == "rabbit":
        newprint("You give the rabbit a carrot and it runs back to feed its family.")
    elif name == "bee":
        newprint("The bee gets intoxicated by the flower's beauty and leaves you alone.")
    elif name == "rat":
        newprint("The rat can't smell anything except for the smelly cheese and runs off to find a gas mask.")
    elif name == "bear":
        newprint("The bear puts its hand in the jar of honey and it gets all sticky. It runs off, embarrassed.")
    elif name == "wolf":
        newprint("The wolf doesn't understand how you took a sheep out of your pocket and runs off feeling scared.")
    elif name == "devil":
        newprint("The devil melts to the sight of the angelic power! Good thing you had one in handy!")


def doomScreen():
    system('cls')
    newprint("You have died..")
    time.sleep(3)
    sys.exit()


def attackmewith(name, hp, damage, defence, maxdefence, thisturn, monsterSprite):
    global health, attackDefence, attackDamage, water, food
    global action
    global firstSling
    global wins, acorns
    global listItems
    global maxEnemyDefence, maxEnemyDamage, maxEnemyHP
    global turn
    turn = thisturn
    baseattack = damage
    system('cls')

    print(monsterimages[spriteDictionary[name]])

    if turn:
        newprint("You have attacked a wild " + name + "!")
    elif not turn:
        newprint("A wild " + name + " has attacked you!")

    while True:
        if health <= 0:
            doomScreen()
        if hp <= 0:
            wins += 1
            newprint("You have defeated the " + name + "!")
            health = maxHealth
            benefit = random.randrange(0, 5)
            if benefit == 0:
                health += 1
                newprint("Your health goes up by one! Current health: " + str(health))
            benefit = random.randrange(0, 5)
            if benefit == 0:
                attackDefence += 1
                newprint("Your defence goes up by one! Current defence: " + str(attackDefence))
            benefit = random.randrange(0, 5)
            if benefit == 0:
                attackDamage += 1
                newprint("Your attack goes up by one! Current defence: " + str(attackDamage))
            hindrance = random.randrange(0, 5)
            if hindrance == 0 or hindrance == 3:
                maxEnemyHP += 1
            elif hindrance == 1:
                if maxHealth < maxEnemyDamage:
                    maxEnemyDamage += 1
            elif hindrance == 2:
                if attackDamage > maxEnemyDefence-3:
                    maxEnemyDefence += 1
            # print(maxEnemyHP, maxEnemyDamage, maxEnemyDefence)
            newprint("\nPress \"Enter\" to continue.")
            input()
            system('cls')
            break

        # Player's Turn
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

            while True:
                if turn == False:
                    break
                if hp <= 0:
                    break
                newprint("What do you do?")
                action = input()
                if action == 'help':
                    newprint("You can attack the monster, defend ,or heal yourself. "
                             "You can also use a special item or your slingshot."
                             "\n( Commands : 'attack', 'slingshot', 'defend', 'heal', 'item', 'status')")
                elif action == 'attack':
                    damageYouDo = attackDamage-defence + random.randrange(-1, 1)
                    hp -= damageYouDo
                    newprint("You do " + str(damageYouDo) + " points of damage. The " + name + "'s health: " + str(hp))
                    turn = False
                    break
                elif action == "defend":
                    if baseattack-damage > baseattack/3:
                        damage -= 1
                        newprint("You focus your mind a bit more and are more aware of the " + name + "'s attacks. Defence+")
                    else:
                        newprint("You can't focus more on the " + name + ".")
                    turn = False
                    break
                elif action == 'heal':
                    if health == maxHealth:
                        newprint("You are already at max health.")
                        break
                    elif water == 0 and food == 0:
                        newprint("You don't have any healing items.")
                        break
                    else:
                        newprint("You have " + str(water) + " water and " + str(food) +
                                 " food. How will you heal yourself?\n(\"cancel\" to go back)")
                        while True:
                            newaction = str(input())
                            if newaction == 'water':
                                turn = False
                                health += maxHealth/3
                                if health > maxHealth:
                                    health = maxHealth
                                water -= 1
                                newprint("You drink some water and regain energy. Your health: " + str(health))
                                break
                            elif newaction == 'food':
                                health += maxHealth / 2
                                if health > maxHealth:
                                    health = maxHealth
                                turn = False
                                break
                            elif newaction == "help":
                                newprint('Type "food" or "water". Food restores half of your health, '
                                         'while water heals one third.')
                            elif newaction == 'cancel':
                                newprint("You decide not to heal right now.")
                                break

                elif action == "debug.win":
                    hp = 0
                    break

                elif action == 'item':
                    boolforsuccessfulitem = False
                    if len(listItems) > 0:
                        itemsstring = ""
                        for itemy in listItems:
                            itemsstring = itemsstring + itemy + ", "
                        newprint("Available items: " + itemsstring)
                        boolforthis = True
                        while boolforthis:
                            newprint("Which item will you use?")
                            newaction = input()
                            if newaction == "help":
                                newprint("Type in the item to use it. \"cancel\" to go back.")
                            for listyitem in listItems:
                                if listyitem == newaction:
                                    if newaction == weaknessDictionary[name]:
                                        showweakness(name)
                                        templist = []
                                        for tempylistyitem in listItems:
                                            if newaction != tempylistyitem:
                                                templist.append(tempylistyitem)
                                            else:
                                                newaction = ""
                                        listItems = templist
                                        boolforthis = False
                                        boolforsuccessfulitem = True
                                        hp = 0
                                        break
                                    else:
                                        newprint("This item does not help in this battle.")
                                        turn = False
                                        boolforthis = False
                                        break
                    else:
                        newprint("You do not have any items right now.")
                        break
                    if boolforsuccessfulitem:
                        break

                elif action == 'slingshot':
                    if acorns <= 0:
                        newprint("You don't have any acorns!")
                        continue
                    while True:
                        if firstSling:
                            newprint("When you use your slingshot you have the chance to deal twice the ammount of damage\n"
                                     "you normally do. But you also have an equal chance to miss.\n"
                                     "You also need ammo which you can collect throughout your journey.\n"
                                     "Type \"help\" for more info.")
                            firstSling = False
                        newprint("You have " + str(acorns) + " acorns. What is your decision?")
                        newaction = input()
                        if newaction == "shoot" or newaction == "attack":
                            acorns -= 1
                            newprint("You aim with your slingshot, and")
                            for dothis in range(0, random.randrange(3, 6)):
                                print(".", end="")
                                time.sleep(0.2)
                            print()
                            damageYouDo = random.randrange(0, attackDamage*2+1)
                            if damageYouDo > attackDamage:
                                newprint("BULLSEYE!")
                            elif damageYouDo == attackDamage:
                                newprint("Whew!")
                            elif damageYouDo <= 0:
                                newprint("Oh,no! You missed!")
                                turn = False
                            else:
                                newprint("Agh...")
                            if damageYouDo<0:
                                damageYouDo = 0
                            hp -= damageYouDo
                            newprint(
                                "You do " + str(damageYouDo) + " points of damage. The " + name + "'s health: " + str(
                                    hp))
                            turn = False
                            break
                        elif newaction == "help":
                            newprint('Type "shoot" to shoot, or "cancel" to go back.')
                        elif newaction == "cancel":
                            break
                        else:
                            newprint(error)

                elif action == 'status':
                    newprint("Your health: " + str(health) + "\nThe " + name + "'s health: " + str(hp))


        # Enemy Turn
        print()
        if not turn and hp > 0:
            enemyAction = random.randrange(0, 4)
            if enemyAction == 0 and defence < maxdefence:
                newprint("The " + name + " defends. Its defence raises by one")
                defence += 1
            elif enemyAction == 0 and defence >= maxdefence:
                newprint("The " + name + " tries to defend, but it has already defended itself too much.")

            if enemyAction == 1 or enemyAction == 2:
                enemyDealsDamage = damage-attackDefence
                if enemyDealsDamage < 0:
                    enemyDealsDamage = 0
                health -= enemyDealsDamage
                newprint("The " + name + " deals " + str(enemyDealsDamage) + " points of damage. "
                                "Your health is now " + str(health) + ".")
            if enemyAction == 3:
                if damage <= attackDefence-2:
                    damage += 1
                    newprint("The " + name + " focuses to raise its attack by one.")
                else:
                    newprint("The " + name + " tries to gather up strength but fails.")
            if enemyAction == 4:
                pass
            if enemyAction == 5:
                pass
            turn = True

            # After Both Turns
            print()


def attack(turn):
    monName = listMonsters[random.randrange(0, len(listMonsters))]
    attackmewith(monName, maxEnemyHP, maxEnemyDamage, defenceatatart(), maxEnemyDefence, turn, spriteDictionary[monName])#random.randrange(0, 0))


def nothingHappens():
    youdoaction = listYouDoAction[random.randrange(0, len(listYouDoAction))]
    youdoadjective = listYouDoAdjective[random.randrange(0, len(listYouDoAdjective))]
    youdoobject = listYouDoObject[random.randrange(0, len(listYouDoObject))]
    youdoplace = listYouDoPlace[random.randrange(0, len(listYouDoPlace))]
    youdonextobject = listYouDoNextObject[random.randrange(0, len(listYouDoNextObject))]
    newprint(youdoaction + " " + youdoadjective + " " + youdoobject + " " + youdoplace + " " + youdonextobject + ".")


def move():
    global food, water, acorns

    randomEvent = random.randrange(0, 101)

    if 0 <= randomEvent < 30:        # nothing
        print()
        nothingHappens()
    elif 30 <= randomEvent < 50:      # attack
        attack(random.getrandbits(1))
    elif 50 <= randomEvent < 65:        # item
        newitemgotten = listOfItems[random.randrange(0, len(listOfItems))]
        listItems.append(newitemgotten)
        newprint("You see something on the ground and pick it up. It appears to be a " + newitemgotten +
                 "! \nYou decide to put the " + newitemgotten + " in your pocket. It might come in handy")
    elif 65 <= randomEvent < 85:          # food or water
        newchoice = random.randrange(0, 3)
        if newchoice == 0 or newchoice == 1:
            water += 1
            newprint("You find some water! Your water bottles are now " + str(water))
        else:
            food += 1
            newprint("You have stumbled on a deserted sandwitch. You decide to pick it up.\n"
                     "Now you have " + str(food) + " food.")
    elif 85 <= randomEvent <= 100:        # acorns
        luckynumber = random.randrange(4, 11)
        acorns += luckynumber
        newprint("You got lucky! Some acorns were just lying around. Seems like there are\n"
                 "just about " + str(luckynumber) + " of them. Now you have a total of " + str(acorns) + " acorns.")

#
#
#                                Start of story.
#
#

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
newprint("\nYou continue walking. Along the way you find some acorns. "
         "You can shoot them with your slingshot.\nPick them up?")

if yesorno():
    hence = random.randrange(5, 10)
    acorns += hence
    newprint("You picked up " + str(hence) + " acorns")
else:
    hence = random.randrange(5, 10)
    acorns += hence
    newprint("You remember that you already had " + str(hence) + " acorns.")

newprint("\nWhile thinking about practicing your slingshot skills, you notice a presence around you.\n"
         "You look to your right and see a peculiar face watching you. It might be a monster!\n"
         "Do you attack it?")

attack(yesorno())

#
#
#     Now entering wander stage
#
#
newprint("You are not sure which way your home is and decide to leave it to fate.\n"
         "Type in directions to go that way. You may find items along your path, but you\n"
         "may also encounter enemies. It is all up to you now! Go, take the medicine to your\n"
         "sick mother!")
while True:
    if wins < 20:
        print()
        correctInput = False
        newprint("Which way do you go now?")
        action = input()

        if action == "debug.win":
            wins = 20

        if action == "help":
            newprint("Type in directions in order to proceed. You can use up/down/left/right, or north/south/east/west")
            correctInput = True
        for item in listDirections:
            if action == item:
                move()
                correctInput = True
        if correctInput == False:
            newprint(error)
            correctInput = True
    else:
        break
system('cls')
newprint("You have been here for hours, but finally, you have found you way back home!\n"
         "You give the medicine  to your mother and spend the rest of the day\n"
         "telling her the story of your brave adventure!")

newprint(" ____  _  _  ____    ____  __ _  ____ \n"
         "(_  _)/ )( \(  __)  (  __)(  ( \(    \\\n"
         "  )(  ) __ ( ) _)    ) _) /    / ) D (\n"
         " (__) \_)(_/(____)  (____)\_)__)(____/")