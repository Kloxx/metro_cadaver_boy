#!/usr/bin/env python2.7

import ConfigParser

class config(object):
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.txt')
        self.fullscreen = bool(int(config.get('Screen', 'fullscreen')))
        self.width = int(config.get('Screen', 'width'))
        self.height = int(config.get('Screen', 'height'))
        self.soundfx = int(config.get('Sound', 'soundfx'))
        self.music = int(config.get('Sound', 'music'))

if __name__ == "__main__":
    cfg = config()
    print cfg.fullscreen
