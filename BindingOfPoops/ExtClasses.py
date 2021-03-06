from enum import Enum
import Player, math, pygame



class globalMath:
    def __init__(self):
        self.temp = 0

    def Angle(self, originObject, targetObject):
        return math.atan2((originObject.ypos - targetObject.ypos), (targetObject.xpos - originObject.xpos)) + math.pi / 2

    def AnglePlayer(self, origin):
        return math.atan2((origin.ypos - Global.player.ypos), (Global.player.xpos - origin.xpos)) + math.pi/2


GlobalMath = globalMath()

class Global:
    player = None
    Sounds = None

class Constants:
    scr_width = 1080
    scr_height = 720
    fps = 60
    caption = "The Binding of Poops"
    iconImage = "icon.png"

    debugMessage = ""

    playerWidth = 56
    playerHeight = 66

    enemycount = 0

class ObjectLists:
    listAllObjects = []
    listOfTears = []
    listOfEnemies = []

class Time:
    deltaTime = 0.0

class Colors:
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

class directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

class sounds:
    def __init__(self):
        self.player_tear_1 = pygame.mixer.Sound("assets/sfx/tear_fire_2.wav")
        self.tear_destroy = pygame.mixer.Sound("assets/sfx/tear_fire_1.wav")
        self.insect_swarm = pygame.mixer.Sound("assets/sfx/insect_swarm.wav")
