from constants import *

from entities.Player import Player
from entities.Tile import Tile
from KeyHandler import KeyHandler
import pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = Player()
floor = Tile('./sprites/tiles/floor.png')
book = Tile('./sprites/tiles/open-book.png')
page = Tile('./sprites/tiles/page.png')
keyH = KeyHandler()
readBook = False

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

    book.draw(screen, 12, 8)

    player.update()
    player.draw(screen)

    if (keyH.getZ() and player.x > 11 * TILE_SIZE and player.x < 13 * TILE_SIZE and player.y > 7 * TILE_SIZE and player.y < 9 * TILE_SIZE):
        readBook = True

    if (keyH.getX() and readBook):
        readBook = False

    if readBook:
        for col in range(3, 21):
            for row in range(3, 13):
                page.draw(screen, col, row)

    pygame.display.update()
