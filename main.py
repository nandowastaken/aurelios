from constants import *

from entities.Player import Player
from entities.Tile import Tile
import pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = Player()
floor = Tile('./sprites/tiles/floor.png')

pygame.display.set_caption("Aurelius")
exit = False

while not exit:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    screen.fill(BLACK)

    # Draw floor
    for col in range(SCREEN_COLUMNS):
        for row in range(SCREEN_ROWS):
            floor.draw(screen, col, row)

    player.update()
    player.draw(screen)

    pygame.display.update()
