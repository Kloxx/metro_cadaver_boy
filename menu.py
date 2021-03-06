#!/usr/bin/env python2.7

import pygame
from modules import config

pygame.init()

# Import config
cfg = config.config()

fullscreen = cfg.fullscreen
width = cfg.width
height = cfg.height
resolution = (width, height)

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Set screen
screen = pygame.display.set_mode(resolution, pygame.DOUBLEBUF|pygame.HWSURFACE)

# Menus
class menu(object):
    def __init__(self, title, background, width, height, rect):
        self.title = title
        self.font_size = height / rect.height
        self.index = 0
        self.background = pygame.image.load("resources/menus/%s" % background).convert()
        self.position = (width / rect.left, height / rect.top)
        self.rect = rect
    def setParent(self, parent):
        self.parent = parent
    def getTitle(self):
        return self.title
    def getPos(self):
        return self.position
    def getSize(self):
        return self.rect.size

class main_menu(menu):
    def __init__(self, title, background, width, height, rect, children):
        super(main_menu, self).__init__(title, background, width, height, rect)
        self.children = children
    def choose(self, direction):
        self.index = (self.index + direction) % len(self.children)
    def print_titles(self, screen):
        screen.blit(self.background, (0,0))
        for num, child in enumerate(self.children):
            if num == self.index:
                color = (255,0,0)
            else:
                color = (255,255,255)
            text = pygame.font.Font(None, self.font_size).render(child.getTitle(), True, color)
            screen.blit(text, child.getPos())
    def select(self):
        current = self.children[self.index]
        return current
    def back(self):
        if self.title == 'MAIN':
            return 0
        else:
            return 1

class option_menu(menu):
    def __init__(self, title, background, width, height, rect, options):
        super(option_menu, self).__init__(title, background, width, height, rect)
        self.options = options
        self.option_choice = None
    def choose(self, direction):
        self.index = (self.index + direction) % len(self.options)
    def print_titles(self, screen):
        screen.blit(self.background, (0,0))
        for num, option in enumerate(self.options):
            if num == self.index:
                color = (255,0,0)
            else:
                color = (255,255,255)
            text = pygame.font.Font(None, self.font_size).render(option.getTitle(), True, color)
            screen.blit(text, (self.horizontal, position))
            option.print_option(screen)
    def select(self):
        self.option_choice = self.options[self.index]
        return self
    def back(self):
        if self.option_choice == None:
            return self.parent
        else:
            self.option_choice = None
            return self

class launch(object):
    def __init__(self, title, width, height, rect):
        self.title = title
        self.position = (width / rect.left, height / rect.top)
    def getTitle(self):
        return self.title
    def getPos(self):
        return self.position


# Init menus        
exit = launch('QUIT', width, height, pygame.Rect(10,10,10,10))
load = launch('LOAD', width, height, pygame.Rect(10,10,10,10))
start = launch('CONTINUE', width, height, pygame.Rect(10,10,10,10))
new_game = launch('NEW GAME', width, height, pygame.Rect(10,10,10,10))
controller = option_menu('CONTROLLER', 'options_in.png', width, height, pygame.Rect(10,10,10,10), [])
video = option_menu('VIDEO', 'options_in.png', width, height, pygame.Rect(10,10,10,10), [])
game = option_menu('GAME', 'options_in.png', width, height, pygame.Rect(10,10,10,10), [])
sound = option_menu('SOUND', 'options_in.png', width, height, pygame.Rect(10,10,10,10), [])
options = main_menu('OPTIONS', 'main_option.png', width, height, pygame.Rect(2, 2, 3.3, 12), [controller, video, game, sound])
main = main_menu('MAIN', 'main_menu.png', width, height, pygame.Rect(10,10,10,10), [new_game, start, load, options, exit])


# Main
current = main
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current.choose(-1)
            if event.key == pygame.K_DOWN:
                current.choose(1)
            if event.key == pygame.K_RETURN:
                current = current.select()
            if event.key == pygame.K_ESCAPE:
                option = current.back()
                if option == 0:
                    done = True
    current.print_titles(screen)
    pygame.display.flip()
pygame.quit()
