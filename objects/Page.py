from constants import *
import pygame
pygame.init()


class Page:
    def __init__(self, tile):
        self.tile = tile

    def draw(self, screen):
        for col in range(3, 21):
            for row in range(3, 13):
                self.tile.draw(screen, col, row)
