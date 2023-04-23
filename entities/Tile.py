from constants import *
import pygame
pygame.init()


class Tile:
    def __init__(self, path):
        self.tile = pygame.image.load(path)
        self.tile = pygame.transform.scale(self.tile, (TILE_SIZE, TILE_SIZE))

    def draw(self, screen, col, row):
        screen.blit(self.tile, (col * TILE_SIZE, row * TILE_SIZE))
