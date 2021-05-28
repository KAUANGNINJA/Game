import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/nave.png")
        self.image = pygame.transform.scale(self.image, [120, 120])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 1
        self.acceleration = 0.1

    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        else:
            self.speed *= 1

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 1


        if keys[pygame.K_UP]:
            self.speed -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed += self.acceleration
        else:
            self.speed *= 0.95

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 1
