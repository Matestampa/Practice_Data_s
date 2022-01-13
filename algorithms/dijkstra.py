from data_s.grafos import Graph
from dijk_help import P_Queue

import time

#el poped, es el objeto que contiene los datos de distancia, y trackea el anteriro(es independiente del grafo)
#el actual es el objeto concreto del vertice (corresponde directamente al grafo)

class First():
      def __init__(self):
          self.value="finish"
          self.prev=None


def path(vertex):
    lista=[]

    actual=vertex
    while actual!=None:
          
          lista.insert(0,actual.value)
          actual=actual.prev
     
    return lista
          
    
def DJS(grafo,s,f):
    
    cola=P_Queue()
    
    cola.add(value=s)
    cola.update(s,distance=0,prev=First()) #como es el primero, y hay una parte(1er if despues del for) donde verficamos el prev,
                                           #le ponemos como un prev, que tenga un valor cualquiera, y a ese si le ponemos en el prev un None

    while True:
          poped=cola.pop() #elimina del queue y devuelve objeto
          actual=grafo.get_vertex(poped.value)

          if poped.value==f:
             return (path(poped),poped.distance)

          for i in actual.get_neighs():#recorremos los vecinos
        
              if i.value==poped.prev.value: #si es igual al del que venia, no hacemos nada con ese
                 pass

              else:
                 curr=cola.get(i.value)

                 if curr==None: #verificamos si estan o no en el queue
                    curr=cola.add(value=i.value,send_back=True) #sino, lo agregamos y el p_queue se encarga de ordenarlo

                 if (i.height+poped.distance)<curr.distance: #si se cumple la regla de la distancia menor y eso:
       
                    cola.update(i.value,distance=i.height+poped.distance,prev=poped) #actualizamos(tambien el p_queue se encarga de ordenar nuevamente)


grafo=Graph()

grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_vertex("c")
grafo.add_vertex("d")
grafo.add_vertex("e")
grafo.add_vertex("f")


grafo.add_edge("a","b",7)
grafo.add_edge("a","c",12)

grafo.add_edge("b","c",2)
grafo.add_edge("b","d",9)

grafo.add_edge("c","e",10)

grafo.add_edge("e","d",4)
grafo.add_edge("e","f",5)

grafo.add_edge("d","f",1)

start=time.time()

result=DJS(grafo,"a","f")

finish=time.time()

print(result)
print(finish-start)
