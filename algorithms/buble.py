#-------------buble sort-----una verga-------------------------------------------
from random import randint
import time

lista=


inicio=time.time()
for i in range(len(lista)):
    
    for j in range(len(lista)-1,i,-1):
        if lista[j]<lista[j-1]:
            mayor=lista[j-1]
            lista[j-1]=lista[j]
            lista[j]=mayor
print(lista)
final=time.time()
print(final-inicio)

2 3 20 19 40 50 