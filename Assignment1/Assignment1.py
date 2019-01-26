import sys
from os import system
import time
import random
system('cls')

# constants
action = ''
error = 'Command not available. You can type "help" for example options.'
listYes = ("yes", "yep", "ya", "noice", "yas", "yaas", "yaaas", "yaaaas", "yaaaaas",
           "correct", "yee", "ye", "yuhuh", "y", "ok", "okey dokey","okie dokie","positive")
listNo = ("no", "nope", "n", "nuhuh", "newp", "negative", "nein", "nicht", "never")
listCheckINv = ("check inv", "inv", "check inventory", "inventory")
listItems = ["honey", "sheep", "flower", "cheese", "carrot"]
listMonsters = ("rabbit", "bee", "rat", "bear", "wolf")
weaknessDictionary = {"rabbit": "carrot", "bee": "flower", "rat": "cheese", "bear": "honey", "wolf": "sheep"}
spriteDictionary = {"rabbit": 0, "bee": 1, "rat": 2, "bear": 3, "wolf": 4}
firstSling = False    # True


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
monster1 = "\n  ,/         \\.\n" " ((           ))\n" "   )')     (`(\n" " ,'`/       \\,`.\n" " \\-'\\,-'*`-./`-/\n" "  \\-')     (`-/\n" "  /`'       `'\\\n" " (   _      _  )\n" " |  `.\\   /,'  |\n" " |    `\\ /'    |\n" "  \\           /\n" "   \\         /\n" "    `.     ,'\n" "      `-.-'\n"


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
    if monsterSprite == 0:
        print(monster1)
    else:
        print(monster1)
    if turn:
        newprint("You have attacked the wild " + name + "!")
    elif not turn:
        newprint("A wild " + name + " has attacked you!")

    while True:
        if health <=0:
            doomScreen()
        if hp <= 0:
            wins += 1
            newprint("You have defeated  the " + name + "!")
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
            time.sleep(1.5)
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
                    elif water == 0 and food == 0:
                        newprint("You don't have any healing items.")
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
                        for item in listItems:
                            itemsstring = itemsstring + item + ", "
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
                    if boolforsuccessfulitem:
                        break

                elif action == 'slingshot':
                    if acorns <= 0:
                        newprint("You don't have any acorns!")
                        break
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
                            damageYouDo = attackDamage - defence + random.randrange(0, attackDamage*2+1)
                            if damageYouDo > attackDamage:
                                newprint("BULLSEYE!")
                            elif damageYouDo == attackDamage:
                                newprint("Whew!")
                            elif damageYouDo == 0:
                                newprint("Oh,no! You missed!")
                                turn = False
                                break
                            else:
                                newprint("Agh...")
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
                turn = False

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

"""
Here you will give commands such as 'up', 'down', etc. There will be a random event on every movement
You can't get lost and there is no significance whatsoever to where you chose to go.

Random events include:
Find Acorns      - 15% (1-5)
Find water       - 15% (1)
Find Food        - 15% (1)
Find Item        - 10% (1)
Monster Attack   - 15% (1)
Nothing          - 30%
"""