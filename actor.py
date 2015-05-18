import game

##
## Actor is the base class for dinamic elements in game
##
class Actor:
    # Creates a character
    #   x, y:       position
    #   collider:   pygame.Rect representing the actor collidable area
    #
    def __init__(self, x, y, collider):
        # Position
        self.x = x
        self.y = y
        
        # Collider
        self.collider = collider

    def update_events(self, events):
        pass

    def update(self): 
        pass

    def on_land(self):
        pass

    def on_peak(self):
        pass

    def on_air(self):
        pass

    def on_left(self):
        pass

    def on_right(self):
        pass

    def on_start(self):
        pass

    def draw(self, xcam, ycam):
        pass