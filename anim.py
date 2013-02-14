#!/usr/bin/env python2.7

import pygame
from modules.loadchar import *

pygame.init()

resolution = (800, 600)
screen = pygame.display.set_mode(resolution, pygame.DOUBLEBUF|pygame.HWSURFACE)
blue = (0,0,255)

mainwalkright = animation("mainchar", "walkright")

clock = pygame.time.Clock()

done = False
anim = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(8)
    screen.fill(blue)
    screen.blit(mainwalkright[anim], (100, 100))
    pygame.display.flip()
    anim = (anim + 1) % len(mainwalkright)

pygame.quit()
