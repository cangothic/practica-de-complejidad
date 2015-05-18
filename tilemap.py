import game
import pygame
import json
from tile import *
from tileset import *

class Tilemap:
    def __init__(self):
        self.gindex = {}  
        self.tilesets = []
        self.current_map = None
        self.current_width = 0
        self.current_height = 0
        self.tilew = 0
        self.tileh = 0
        self.no_collision = {0: True}

    def load_tilesets(self, path):
        json_data = open(path)
        data = json.load(json_data)    
        self.tilew = data['tilewidth']    
        self.tileh = data['tileheight']

        for t in data['tilesets']:
            tileset = Tileset(t['image'], t['imagewidth'], t['imageheight'],
                              t['tilewidth'], t['tileheight'], 
                              t['margin'], t['spacing'],
                              t['firstgid'], t['transparentcolor'])
            self.tilesets.append(tileset)

            if 'tileproperties' in t:
                for tile_id in t['tileproperties']:
                    if 'NoCollide' in t['tileproperties'][tile_id] and t['tileproperties'][tile_id]['NoCollide'] == '1':
                        self.no_collision[int(tile_id) + tileset.firstgid] = True

        self.index_gid()
        json_data.close()
        print self.no_collision
         
    def index_gid(self):
        for tileset in self.tilesets:
            gid = tileset.firstgid

            for i in range(0, tileset.h/(tileset.tileh + tileset.spacing)):
                for j in range(0, tileset.w/(tileset.tilew + tileset.spacing)):
                    x = j * (tileset.tilew + tileset.spacing) + tileset.margin
                    y = i * (tileset.tileh + tileset.spacing) + tileset.margin 
                    self.gindex[gid] = Tile(x, y, tileset)
                    gid += 1

    def load_map(self, path):
        json_data = open(path)
        data = json.load(json_data)
        self.current_height = data['height']
        self.current_width = data['width']
        
        self.current_map = []
        map_data = data['layers'][0]['data']#CHANGE THIS!
        for i in range(self.current_height):
            row = []
            for j in range(self.current_width):
                row.append(map_data[i * self.current_width + j])    
            self.current_map.append(row)
        
    

    
