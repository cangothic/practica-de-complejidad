import game
import pygame
from character import *
from pygame.locals import *
from constants import *

class Player(Character):
    def update_events(self, events):
        if K_RIGHT in events:
            if not self.right:
                self.direction = True
                self.frame = 0
            self.right = events[K_RIGHT]
            
        if K_LEFT in events:
            if not self.left:
                self.direction = False
                self.frame = 0
            self.left = events[K_LEFT]
            
        if K_UP in events:
            self.jump = events[K_UP]
            self.frame = 0

        if K_SPACE in events:
            self.stop = events[K_SPACE]