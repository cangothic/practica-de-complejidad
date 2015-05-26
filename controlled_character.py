import game
import pygame
from character import *
from pygame.locals import *
from constants import *
from resources import *

class ControlledCharacter(Character):
    def on_left(self):
        self.direction = True
        self.right = True
        self.left = False

    def on_right(self):
        self.direction = False        
        self.right = False
        self.left = True

    def on_start(self):
        self.direction = True
        self.right = True
        self.jump=False
        self.color=False

    def saltar(self):
        self.jump=not self.jump

    def colorear(self):
        resources = Resources('graphics/arc22.png')
        self.color=not self.color
        if(self.color):
            cambio=resources.cambiar('graphics/arc2.png')
            self.idle = cambio[0]
            self.walking = cambio[1]
            self.jumping = cambio[2]
        else:
            cambio=resources.cambiar('graphics/arc22.png')
            self.idle = cambio[0]
            self.walking = cambio[1]
            self.jumping = cambio[2]
            
            
    
