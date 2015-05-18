import game

class Tileset:
    def __init__(self, path, w, h, tilew, tileh, margin, spacing, firstgid, alpha_color):
        self.path = path
        self.w = w
        self.h = h
        self.tilew = tilew
        self.tileh = tileh
        self.margin = margin
        self.spacing = spacing
        self.firstgid = firstgid
        self.alpha_color = alpha_color
        self.sheet = game.load_image(self.path)