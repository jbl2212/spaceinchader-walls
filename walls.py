import pygame
pygame.init

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("spaceinchader")
class Wall:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (37, 194, 79),(self.xpos, self.ypos, 100, 20))
        
w1 = Wall (675, 650)
w2 = Wall (450, 650)
w3 = Wall (250, 650)
w4 = Wall (50, 650)

w1.draw()
w2.draw()
w3.draw()
w4.draw()
pygame.display.flip()

