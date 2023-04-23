from constants import *
import pygame
pygame.init()


class Player:
    def __init__(self):
        self.up_sprites = []
        self.down_sprites = []
        self.left_sprites = []
        self.right_sprites = []

        self.sprite = None
        self.direction = "down"

        self.x = 0
        self.y = 0
        self.speed = 5

        self.setSprites()

    def setSprites(self):
        for sprite_num in range(4):
            sprite = pygame.image.load(f'./sprites/down{sprite_num + 1}.png')
            self.down_sprites.append(pygame.transform.scale(
                sprite, (TILE_SIZE, TILE_SIZE)))

        for sprite_num in range(4):
            sprite = pygame.image.load(f'./sprites/up{sprite_num + 1}.png')
            self.up_sprites.append(pygame.transform.scale(
                sprite, (TILE_SIZE, TILE_SIZE)))

        for sprite_num in range(4):
            sprite = pygame.image.load(
                f'./sprites/left{sprite_num + 1}.png')
            self.left_sprites.append(pygame.transform.scale(
                sprite, (TILE_SIZE, TILE_SIZE)))

        for sprite_num in range(4):
            sprite = pygame.image.load(
                f'./sprites/right{sprite_num + 1}.png')

            self.right_sprites.append(pygame.transform.scale(
                sprite, (TILE_SIZE, TILE_SIZE)))

    def update(self):
        # Movement system
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = "right"

        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = "down"

        # Adjusts the sprite to the direction of the player movement
        if self.direction == "down":
            self.sprite = self.down_sprites[0]
        elif self.direction == "up":
            self.sprite = self.up_sprites[0]
        elif self.direction == "left":
            self.sprite = self.left_sprites[0]
        elif self.direction == "right":
            self.sprite = self.right_sprites[0]

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
