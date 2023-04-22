import pygame

pygame.init()

# screen
originalTileSize = 16
SCALE = 3
TILE_SIZE = originalTileSize * SCALE

SCREEN_COLUMNS = 24
SCREEN_ROWS = 16

SCREEN_WIDTH = SCREEN_COLUMNS * TILE_SIZE
SCREEN_HEIGHT = SCREEN_ROWS * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 255, 255)

# Player
direction = None
x = 0
y = 0
player_speed = 4

pygame.display.set_caption("Aurelius")
exit = False

while not exit:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= player_speed
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        x += player_speed
        direction = "right"

    if keys[pygame.K_UP]:
        y -= player_speed
        direction = "up"
    elif keys[pygame.K_DOWN]:
        y += player_speed
        direction = "down"

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, pygame.Rect(x, y, 60, 60))

    pygame.display.update()
