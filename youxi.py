import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 400))

feichuan_image = pygame.image.load('jiantou.bmp')
feichuan_rect = feichuan_image.get_rect()
feichuan_rect.centerx = 270

print(feichuan_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(feichuan_image, feichuan_rect)

    pygame.display.flip()
