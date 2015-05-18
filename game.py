import pygame
from pygame import *

def start(w,h):
    print 'One second, we are awakening the character.'
    pygame.init()
    pygame.display.set_mode((w, h))
    print 'Lets go!'

def apply_alpha(image, colorkey):
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

def load_image(path, colorkey = None):
    image = pygame.image.load(path).convert()
    apply_alpha(image, colorkey)
    return image

def load_sprite(sheet, rectangle, colorkey = None):    
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    apply_alpha(image, colorkey)
    return image#pygame.transform.scale2x(image)
     
def load_sprites(sheet, rects, colorkey = None):
    return [load_sprite(sheet, rect,(0,0,0)) for rect in rects]

def flip_sprites(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    
def clear():
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0,0))

def draw(image, xy):
    screen = pygame.display.get_surface()
    screen.blit(image, xy)

def draw_tile(sheet, xy, rect, colorkey=None):
    screen = pygame.display.get_surface()
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    apply_alpha(image, colorkey)
    screen.blit(image, xy)

def draw_rect(rect):
    screen = pygame.display.get_surface()
    pygame.draw.rect(screen, (255,0,0), rect)

def debug_txt(txt,xy,color):
    font = pygame.font.Font(None, 12)
    text = font.render(txt, 1, color)
    screen = pygame.display.get_surface()
    screen.blit(text, xy)


def update():
    screen = pygame.display.get_surface()
    screen.blit(pygame.transform.scale2x(screen), (0,0))
    pygame.display.flip()

def get_events():
    eventos = {}
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            eventos[evento.key] = True
        if evento.type == KEYUP:
            eventos[evento.key] = False
        elif evento.type == QUIT:
            eventos['QUIT'] = True
    return eventos
     

def quit_game():
    pygame.quit()

def clock():
    return pygame.time.Clock()


def new_rect(x,y,size):
    return pygame.Rect(x, y, size[0], size[1])

def to_rgb(color):
    return (0,0,0)


        
