from constants import *

from entities.Player import Player
from entities.Tile import Tile
from objects.Page import Page

from KeyHandler import KeyHandler
import pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = Player()
floor = Tile('./sprites/tiles/floor.png')
wall = Tile('./sprites/tiles/wall.png')
book = Tile('./sprites/tiles/open-book.png')
page_tile = Tile('./sprites/tiles/page.png')
bed = Tile('./sprites/tiles/cama.png')
mesa = Tile('./sprites/tiles/mesa.png')
keyH = KeyHandler()
readBook = False

page = Page(page_tile)

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

    for row in range(SCREEN_ROWS):
        wall.draw(screen, 0, row)
        wall.draw(screen, 23, row)

    for col in range(SCREEN_COLUMNS):
        wall.draw(screen, col, 0)
        wall.draw(screen, col, 15)

    mesa.draw(screen, 12, 8)
    book.draw(screen, 12, 8)
    bed.draw(screen, 12, 1)

    player.update()
    player.draw(screen)

    if (keyH.getZ() and player.x > 11 * TILE_SIZE and player.x < 13 * TILE_SIZE and player.y > 7 * TILE_SIZE and player.y < 9 * TILE_SIZE):
        readBook = True

    if (keyH.getX() and readBook):
        readBook = False

    if readBook:
        page.draw(screen)

    pygame.display.update()
