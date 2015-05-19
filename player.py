import game
import pygame
from character import *
from pygame.locals import *
from constants import *

class Player(Character):
    def __init__(self, x, y, collider, resources):
	Character.__init__(self,x,y,collider,resources)
        self.invertido = False
    def update_events(self, events):
        if K_RIGHT in events:
            
            self.frame = 0
            if(self.invertido==True):
                self.direction = False
                self.left = events[K_RIGHT]
            else:
                self.direction = True
                self.right = events[K_RIGHT]
            
        if K_LEFT in events:
            self.frame = 0
            if(self.invertido==True):
                self.direction = True
                self.right = events[K_LEFT]
            else:
                self.direction = False
                self.left = events[K_LEFT]
		
        if K_UP in events:
            self.jump = events[K_UP]
            self.frame = 0

        if K_SPACE in events:
            self.stop = events[K_SPACE]
    def invertir(self):
        self.invertido = not self.invertido
