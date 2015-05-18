import game
import pygame
from constants import *
from resources import *
from player import *
from tile import *
from tilemap import *
from tileset import *
from camera import *
from gamelogic import *
from controlled_character import *


# Game starts!
game.start(DISP_W*2, DISP_H*2)

resources = Resources()

player = Player(40, 40, pygame.Rect(0,0,15,35), resources.player)
ai = ControlledCharacter(100, 40, pygame.Rect(0,0,15,35), resources.player)
tilemap = Tilemap()
tilemap.load_tilesets('map1.json')
tilemap.load_map('map1.json')
camera = Camera(0, 0, player, [player,ai], tilemap, True, 0.25)
gamelogic = Gamelogic([player,ai], tilemap)

clock = game.clock()

#pygame.mixer.init()
#pygame.mixer.music.load("sound/hyperfun.mp3")
#pygame.mixer.music.play(100)

sheet = game.load_image('graphics/blocks1.png')


# Gameloop
gamelogic.start()
while True:
    events = game.get_events()
    if 'QUIT' in events:
        game.quit_game()
        break
    
    game.clear()

    gamelogic.update(events)
    camera.update()
    camera.draw()

    clock.tick(30)
    game.debug_txt('FPS: '+str(clock.get_fps())[:4], (540,380),RED) 
    
    game.update()
    
    
