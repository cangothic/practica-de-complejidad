import game
import pygame
import random
from pygame import *
from constants import *
from resources import *
from player import *
from tile import *
from tilemap import *
from tileset import *
from camera import *
from gamelogic import *
from controlled_character import *

def evento(player,ai,ai2,ai3,camera,query):
    funciones = {"001":player.invertir,"002":ai.saltar,"003":ai2.colorear,"004":camera.vibrar}

    dialogos = [{"ai3playeriguales":True,"id":"001"},
                {"aiplayeriguales":True,"id":"002"},            
                {"aiai2iguales":True,"id":"003"},
                {"aiplayeriguales":True,"aiai2iguales":True,"id":"004"}
                ]
    validos = []
    tamano = 0
    for event in dialogos:
        if(esValida(event,query) and len(event)>tamano):
            validos.append(event)
    if len(validos)>0:
        tamano = len(validos[0])
        better = validos[0]
        for event in validos:
            if len(event)>tamano:
                tamano = len(event)
                better = event
            if len(event)==tamano:
                if(random.randint(0,2)==1):
                    better = event
        return funciones[better["id"]]

def esValida(reglasEvento,query):
    for regla in reglasEvento:
        if((regla!="id") and (regla not in query or reglasEvento[regla]!= query[regla])):
            return False
    return True
        
                
    

