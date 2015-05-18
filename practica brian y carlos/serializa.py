import json
import random
frases = {"001":"que asco un pantano","002":"hambre y mierda que mala combinacion","003":"wiii la playa",
          "004":"la playa y sin dinero","008":"me comeria un lagarto"}
dialogos = {"brian":[{"ubicacion":"pantano","id":"001"},{"ubicacion":"pantano","hambre":"50","id":"002"},
            {"ubicacion":"pantano","hambre":"50","id":"008"}],
            "jessica":[{"ubicacion":"playa","id":"003"},{"ubicacion":"playa","dinero":"65","id":"004"}]}
dialogosf=open("dialogos.txt",'a')
frasesf=open("fraces.txt",'a')
json.dump(dialogos, dialogosf)
json.dump(frases, frasesf)

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
