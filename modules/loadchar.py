#!/usr/bin/env python2.7

import pygame
import glob

def animation(character, move):
    directory = "resources/animation/%s/%s*.png" % (character, move)
    anim_list = []
    for im in glob.glob(directory):
        sprite = pygame.image.load(im).convert()
        colorkey = sprite.get_at((0,0))
        sprite.set_colorkey(colorkey, pygame.RLEACCEL)
        anim_list.append(sprite)
    return anim_list
