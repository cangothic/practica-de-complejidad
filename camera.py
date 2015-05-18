import game
from constants import *

class Camera:
    def __init__(self, x, y, focus, actors, tilemap, mode=False, offset=0.25):        
        self.x = x
        self.y = y
        self.focus = focus
        self.tilemap = tilemap
        self.offset = offset
        self.mode = mode
        self.x = self.focus.x - DISP_W / 2
        self.actors = [x for x in actors if x != focus]

    def update(self):
        if not self.mode:
            self.x = self.focus.x - DISP_W / 2
            self.y = self.focus.y - DISP_H * 3 / 4
        else:
            limit_x = int(self.offset * DISP_W)

            if self.focus.x < self.x + limit_x:                
                self.x -= (self.x + limit_x) - self.focus.x 
            elif self.focus.x > (self.x + DISP_W) - limit_x:
                self.x += self.focus.x - ((self.x + DISP_W) - limit_x)

            limit_y = int(self.offset * DISP_H)
            if self.focus.y < self.y + limit_y:                
                self.y -= (self.y + limit_y) - self.focus.y 
            elif self.focus.y > (self.y + DISP_H) - limit_y:
                self.y += self.focus.y - ((self.y + DISP_H) - limit_y)

    def draw(self):
        starting_x = (self.x - 1) / self.tilemap.tilew
        starting_y = (self.y - 1) / self.tilemap.tileh

        ending_x = (self.x + DISP_W + 1) / self.tilemap.tilew
        ending_y = (self.y + DISP_H + 1) / self.tilemap.tileh

        for i in range(starting_y, ending_y+1):
            if i < 0 or i >= self.tilemap.current_height:
                continue
            for j in range(starting_x, ending_x+1):
                if j < 0 or j >= self.tilemap.current_width:
                    continue

                tile_id = self.tilemap.current_map[i][j]
                if tile_id != 0:
                    tile = self.tilemap.gindex[tile_id]
                    tile.draw(j * tile.tileset.tilew - self.x,
                              i * tile.tileset.tileh - self.y)
                    if DEBUG:
                        game.debug_txt(str(i)+','+str(j), 
                                       (j * tile.tileset.tilew - self.x,
                                        i * tile.tileset.tileh - self.y), RED)           
                
        self.focus.draw(self.focus.x - self.x, self.focus.y - self.y)
        for actor in self.actors:
            actor.draw(actor.x - self.x, actor.y - self.y)
    

    
