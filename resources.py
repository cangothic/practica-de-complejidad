import game
import pygame
from pygame.locals import *

class Resources:
    def __init__(self):
        # Carga de imagenes
        sheet = game.load_image('graphics/arc22.png')
        #rects = [#pygame.Rect(514,8,24,34),
        #        pygame.Rect(550,8,30,34),
        #         pygame.Rect(582,8,28,34),
        #         pygame.Rect(550,8,30,34)]
        rects = [pygame.Rect(112,2,26,40),
                 pygame.Rect(112,2,26,40),
                 pygame.Rect(112,2,26,40),
                 pygame.Rect(4,4,30,38),
                 pygame.Rect(4,4,30,38),
                 pygame.Rect(4,4,30,38)]
                 
        caminando_der = game.load_sprites(sheet, rects, (0,0,0))
        caminando_izq = game.flip_sprites(caminando_der)

        rects = [pygame.Rect(76,2,26,40),
                 pygame.Rect(112,2,24,40)]
        quieto_der = game.load_sprites(sheet, rects, (0,0,0))
        quieto_izq = game.flip_sprites(quieto_der)

        rects = [pygame.Rect(4,4,30,38),
                 pygame.Rect(38,4,30,36)]
        saltando_der = game.load_sprites(sheet, rects, (0,0,0))
        saltando_izq = game.flip_sprites(saltando_der)
        self.player = [
            [quieto_der, quieto_izq],
            [caminando_der,caminando_izq],            
            [saltando_der, saltando_izq]]

        
        sheet = game.load_image('graphics/blocks11.png')
        suelo = game.load_sprite(sheet, pygame.Rect(444,104,32,32))
        subsuelo = game.load_sprite(sheet, pygame.Rect(172,138,32,32))
        self.tiles = [suelo, subsuelo]
    
        
