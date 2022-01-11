import time
from random import randint

def proccess(lista,fase,nuevo):
    if nuevo<=0:
        return lista,fase

    if nuevo%2==0:
        padre=nuevo//2-1
    
    else:
        padre=nuevo//2
    
    if lista[nuevo]>lista[padre]:
        lista[nuevo],lista[padre]=lista[padre],lista[nuevo]
        fase.append(padre)
        return proccess(lista,fase,padre)

    else:
        return lista,fase

def max_heap(l):
    lista=l
    fases=dict()
    fases[0]=[lista[0],[0]]
    
    for i in range(len(lista)):
        if i>0:
           fases[i]=list()

           fases[i].append(lista[0:i+1])

           lista[0:i+1],fase=proccess(lista[0:i+1],[i],i)
           
           fases[i].append(fase)
           
        else:
           pass
    
    return lista,fases

