import game
import pygame
from pygame.locals import *

class Tile:
    def __init__(self, x, y, tileset):
        self.x = x
        self.y = y
        self.tileset = tileset

    def draw(self, x, y):
        game.draw_tile( self.tileset.sheet, (x, y), 
                        pygame.Rect(self.x, 
                                    self.y,
                                    self.tileset.tilew, 
                                    self.tileset.tileh), 
                        game.to_rgb(self.tileset.alpha_color))
        
    

    
