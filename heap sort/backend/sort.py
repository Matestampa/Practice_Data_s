from random import randint

#lista=[50,20,12,3,4,5]


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


def heapify(padre,hijo1,hijo2,maxim,fase):
    mayor=padre
    response=verify(hijo1,hijo2,maxim,len(lista)-1)
    
    if response=="paso lista":
        return fase

    elif response=="hijo1":
         mayor=hijo1
         lista[mayor],lista[padre]=lista[padre],lista[mayor]
         fase.append(mayor)
         return heapify(mayor,mayor*2+1,mayor*2+2,maxim,fase)
    
    else:
        if lista[hijo1]>lista[hijo2]:
            mayor=hijo1
        else:
            mayor=hijo2
       
        if lista[mayor]>lista[padre]:
           lista[mayor],lista[padre]=lista[padre],lista[mayor]
           fase.append(mayor)
           return heapify(mayor,mayor*2+1,mayor*2+2,maxim,fase)
        else:
            return fase


def heap_sort(l):
    global lista
    lista=[l[i] for i in range(len(l))]
    
    fases=dict()
    #fases[0]=[]

    largo=len(lista)
    f=largo-1
    while f>=0:
          index=largo-f-1
          fase=[f,0]
          
          if f>1:
             lista[0],lista[f]=lista[f],lista[0]
      
          top=0
          hijo1=1
          hijo2=2
      

          fases[index]=heapify(top,hijo1,hijo2,f,fase)
          f-=1

    return fases




