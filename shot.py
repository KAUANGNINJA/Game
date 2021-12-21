import pygame
import math
import random


class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Data/shot.webp")
        self.image = pygame.transform.scale(self.image, [15, 15])
        self.rect = self.image.get_rect()

        self.speed = 9

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()