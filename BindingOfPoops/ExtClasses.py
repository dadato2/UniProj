from enum import Enum

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
