import pygame

pygame.font.init()
debugFont = pygame.font.SysFont('Comic Sans MS', 30)

class debug:
    def __init__(self):
        self.arg = ""
        self.prevarg = ""
    def Log(self, argument):
        try:
            self.arg = str(argument)
        except:
            print("Debug error in class debug!")
        if self.arg != self.prevarg:
            global debugtextsurface
            debugtextsurface = debugFont.render(self.arg, False, (0, 0, 0))
        self.prevarg = self.arg
# debugtextsurface = debugFont.render("", False, (0, 0, 0))
# screen.blit(debugtextsurface, (0, 0))