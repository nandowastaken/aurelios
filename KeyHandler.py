import pygame
pygame.init()


class KeyHandler:
    def __init__(self):
        self.keys = None

    def getZ(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_z]:
            return True
        else:
            return False

    def getX(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_x]:
            return True
        else:
            return False
