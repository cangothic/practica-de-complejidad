import game
from actor import *
from constants import *

##
## Character is the base class for movable actors
##
## The intention of this class is to enable programmers to easily create basic characters,
## if you need complex behaviors, derive directly from Actor.
class Character(Actor):
    # Creates a character
    #   x, y:       position
    #   collider:   pygame.Rect representing the actor collidable area
    #   resources:  sprites to draw.
    #               [[IDLE_RIGHT(2 sprites), IDLE_LEFT(2 sprites)],
    #                [WALKING_RIGHT, WALKING_LEFT],
    #                [JUMPING_RIGHT, JUMPING LEFT]]
    #
    def __init__(self, x, y, collider, resources):        
        # Position
        self.x = x
        self.y = y

        # Custom attributes
        self.vy = 0
        self.frame = 0
        self.direction = True
        self.land = False
        self.right = False
        self.left = False
        self.jump  = False
        self.delta_frames = 0
        self.stop = False

        # Static collisions
        collider.x = x
        collider.y = y
        self.collider = collider
        
        # Actions
        self.idle = resources[0]
        self.walking = resources[1]
        self.jumping = resources[2]

    def update_events(self, events):
        return

    def update(self): 
        if self.stop:
            return
               
        # X movement
        if self.right:
            self.x += VEL_X            
        if self.left:
            self.x -= VEL_X           
                           
        # Y movement
        if self.land and self.jump:
            self.vy = -VEL_Y
            self.land = False
            
        self.y += self.vy            

    def on_land(self):
        self.land = True
        self.vy = 0

    def on_peak(self):
        if self.vy < 0:
            self.vy = 0

    def on_air(self):
        self.land = False
        self.vy = min(self.vy + GRAVITY, MAX_VY)  

    def on_left(self):
        pass

    def on_right(self):
        pass

    def on_start(self):
        pass


    def draw(self, xcam, ycam):
        if self.direction:
            anim_index = 0
        else:
            anim_index = 1
            
        if not self.land:
            if self.vy < 0:
                sprite = self.jumping[anim_index][1]
            else:
                sprite = self.jumping[anim_index][0]
        else:
            if self.right or self.left:
                sprite = self.walking[anim_index][self.frame]
                self.frame = (self.frame + 1) % len(self.walking[anim_index])                
            else:
                self.delta_frames = (self.delta_frames + 1) % 120                
                if self.delta_frames < 90:
                    sprite = self.idle[anim_index][0]
                else:
                    sprite = self.idle[anim_index][1]

        # Center image
        xoffset = -sprite.get_width()/2
        yoffset = -sprite.get_height()
        game.draw(sprite, (xcam + xoffset, ycam + yoffset))
        if DEBUG:
            game.draw_rect(pygame.Rect(xcam - self.collider.w/2, ycam - self.collider.h, self.collider.w, self.collider.h))