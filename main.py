from constants import *
from entities.Player import Player
import pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = Player()

pygame.display.set_caption("Aurelius")
exit = False

while not exit:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    screen.fill(BLACK)

    player.update()
    player.draw(screen)

    pygame.display.update()
