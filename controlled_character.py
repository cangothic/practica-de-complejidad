import game
import pygame
from character import *
from pygame.locals import *
from constants import *


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