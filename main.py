from asteroid import Asteroid
from player import Player
from shot import Shot
import pygame
import random
import sys
import os


dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

# Initial configs
pygame.init()
display_resolution = pygame.display.set_mode([840,480])
pygame.display.set_caption("AstroGame")
clock = pygame.time.Clock()
gameloop = True
gameover = False
timer = 20

# Groups
objectgroup = pygame.sprite.Group()
asteroidgroup = pygame.sprite.Group()
shotgroup = pygame.sprite.Group()
explosiongroup = pygame.sprite.Group()

# Background
bg = pygame.sprite.Sprite(objectgroup)
bg.image = pygame.image.load("Data/universe.webp")
bg.image = pygame.transform.scale(bg.image, [840,480])
bg.rect = bg.image.get_rect()

# Player's
player = Player(objectgroup)

# Music
pygame.mixer.music.load("Data/music.flac")
pygame.mixer.music.play(-1)

# Sounds
shot = pygame.mixer.Sound("Data/shot.flac")

if __name__ == "__main__":
    while gameloop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shot.play()
                    newshot = Shot(objectgroup,shotgroup)
                    newshot.rect.center = player.rect.center
        # Update Logic
        if not gameover:
            objectgroup.update()

            timer += 1

            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newasteroid = Asteroid(objectgroup, asteroidgroup)
            
            collisions = pygame.sprite.spritecollide(player, asteroidgroup, False, pygame.sprite.collide_mask)

            if collisions:
                gameover = True
                pygame.QUIT()
            
            hits = pygame.sprite.groupcollide(shotgroup, asteroidgroup, True, True, pygame.sprite.collide_mask)

        # Draw
        display_resolution.fill([46,46,46])
        objectgroup.draw(display_resolution)
        pygame.display.update()