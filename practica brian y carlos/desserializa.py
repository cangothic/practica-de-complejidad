import json
import random

dialogosf=open("dialogos.txt",'r')
frasesf=open("fraces.txt",'r')
dialogos=json.load(dialogosf)
frases=json.load(frasesf)

def frase(rules):
    posibles = dialogos[rules["personaje"]]
    validos = []
    tamano = 0
    for dialogo in posibles:
        if(esValida(dialogo,rules) and len(dialogo)>tamano):
            validos.append(dialogo)
    if len(validos)>0:
        tamano = len(validos[0])
        better = validos[0]
        for  dialogo in validos:
            if len(dialogo)>tamano:
                tamano = len(dialogo)
                better = dialogo
            if len(dialogo)==tamano:
                if(random.randint(0,2) == 1):
                    better = dialogo
        print frases[better["id"]]
    
        
def esValida(reglasDialogo,query):
    
    for regla in reglasDialogo:
        if((regla!="personaje" and regla!="id") and (regla not in query or reglasDialogo[regla]!=query[regla])):
            return False
    return True

query = {"personaje":"brian","ubicacion":"pantano","hambre":"50"}
frase(query)
