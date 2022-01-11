#-------------HEAP SORT-----------vamos que se puede
#los metemos en el arbol
#hacemos que se ordenen
#intercambiamos la raiz por el ultimo. (queda el mas grande ultimo en la lista)
#ordenamos de nuevo
#intercambiamos la raiz de nuevo con el ultimo
#y asi

import time
from random import randint
from heap_2 import max_heap


#----------como saber quienes son los padres o los hijos---------------------
#estando en un hijo, su padre es:
#si el indice es par: la division entera del indice ,-1
#si el indice es impar: la division entera del indice

#estando en un padre,sus hijos son:
#el indice x 2 +1(hijo mas cercano)
#el indice x 2 + 2 (hijo mas lejano)

lista=[0,1,2,3,4,5,6,7,8,9,10]


def verify(hijo1,hijo2,maxim,lenght):
    
    if hijo1>=lenght or hijo1>=maxim:
        return "paso lista"
    
    elif hijo2>=maxim:
         if hijo1>=maxim:
            return "paso lista"
         else:
            return "hijo1"

    else:
        return "normal"



def heapify(padre,hijo1,hijo2,maxim):
    mayor=padre
    response=verify(hijo1,hijo2,maxim,len(lista)-1)
    
    if response=="paso lista":
        return 

    elif response=="hijo1":
         mayor=hijo1
         lista[mayor],lista[padre]=lista[padre],lista[mayor]
         return heapify(mayor,mayor*2+1,mayor*2+2,maxim)
    
    else:
        if lista[hijo1]>lista[hijo2]:
            mayor=hijo1
        else:
            mayor=hijo2
       
        if lista[mayor]>lista[padre]:
           lista[mayor],lista[padre]=lista[padre],lista[mayor]
           return heapify(mayor,mayor*2+1,mayor*2+2,maxim)
        else:
            return-1

start=time.time()

lista=max_heap(lista)


new_list=[]
f=len(lista)-1
while f>=0:
      lista[0],lista[f]=lista[f],lista[0]
      
      top=0
      hijo1=1
      hijo2=2
      
      new_list.append(lista[f])

      m=heapify(top,hijo1,hijo2,f)
      f-=1

end=time.time()
print("Time:",end-start)

print(new_list)




