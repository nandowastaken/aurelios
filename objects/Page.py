from constants import *
import pygame
import json
pygame.init()

with open('jsons/stories.json', encoding="utf-8") as f:
    data = json.load(f)

words = data["historia"].split()


class Page:
    def __init__(self, tile):
        self.tile = tile
        self.x_text = 144
        self.y_text = 144

    def draw_text(self, screen):
        self.y_text = 144
        self.x_text = 144

        for word in words:
            text = INCONSOLATA_SMALL_FONT.render(word, True, BLACK)

            if (self.x_text + text.get_width() > 964):
                self.x_text = 144
                self.y_text += 21

            screen.blit(text, (self.x_text, self.y_text))

            self.x_text += text.get_width() + GAP_WORD

        return True

    def draw(self, screen):
        for col in range(3, 21):
            for row in range(3, 13):
                self.tile.draw(screen, col, row)

        self.draw_text(screen)
