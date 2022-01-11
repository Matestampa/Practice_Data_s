# Breadth First Search-----------------------------


#Especificamente pata path finding:

#Pasamos un valor de inicio(s) y uno de final (f)

#Hcemos bfs con root en s, y solo lo hacemos hasta encontrar f:
        #result=Bfs(S)

from data_s.grafos import Graph
from data_s.stack_queue import Queue

def BFS(graph,s,f):
    cola=Queue()
    repes={}
    nodes=[]

    cola.push(s)
    repes[s]=1
    
    curr=graph.get_vertex(s)
    
    while cola.is_empty()!=True:
          
          key=cola.pop() #saca de la cola y devuelve el valor
          nodes.append(key) #agregamos a los nodos visitados

          curr=graph.get_vertex(key)

          neighs=curr.get_neighs()

          for i in neighs:
              try:
                  repes[i.value]+=1
              
              except KeyError:
                     repes[i.value]=1
                     cola.push(i.value)
          
    return nodes


def short_path(nodes,f): #le pasamos los nodos que devuelve el BFS, y el vertice al que queremos llegar
    strings=[str(nodes[0])]
    actual=0
    later=1

    while later<=len(nodes)-1:#mientras estemos en la lista
          
          curr=grafo.get_vertex(nodes[actual])

          if curr.has(nodes[later]):#si esta en sus vecinos
             
             #hacer linked list parra guardar path
             new_string=strings[actual]+","+str(nodes[later]) #En este caso pa hacerla mas facil generamos un string del path de cada elmento
                                                              #Sin embargo, ocupa mas memoria
             strings.append(new_string)
             
             if nodes[later]==f:#si damos con el que buscabamos
                
                return strings[later] 
             
             else:
                later+=1
          
          else:
             actual+=1
    
    return "No hay path"
                   
         



#------------Dijkstras Algorith-------------------------------------------------------------------------

#Sirve para encontrar shortest path en weightes grafo(edges tienen valor)

#Pasos:
     #Tomamos un vertice
     #a los vecinos les asignamos el valor de los edges que los conectan + el valor del vertice actual(aparte de su valor por defecto que lo identifica)
     #elegimos el vecino con valor mas bajo y nos movemos a ese
     #le ponemos que apunte al vertice de donde vino
     #repetir


class Remember_Node():
      def __init__(self,value,prev=None):
          self.value=value
          self.prev=prev


def path(vertex):
    lista=[]
   
    actual=vertex
    while actual!=None:
          
          lista.insert(0,actual.value)

          actual=actual.prev
    
    return lista



def DJS(graph,s,f):
    previous={}
    distances={}
    actual=Remember_Node(s)
    actual_height=0
    prev=s
    
    previous[actual.value]=Remember_Node(None)
    distances[actual.value]=1000
    cont=0
    while cont<15:
          
          if actual.value==f:
             return path(actual),actual_height
          
          updated=[]

          curr=graph.get_vertex(actual.value)

          neighs=curr.get_neighs()
          
          #updatear los valores de distancia-------------------
          for i in neighs:
              try:
                  test=previous[i.value]
              
              except KeyError:
                     previous[i.value]=actual.value
                     distances[i.value]=1000

              
              
              if i.value==prev or i.value==previous[actual.value].value: #si es igual a de los posibles de donde venia
                 pass
              else:

                 curr_dist=distances[i.value]

                 if (i.height+actual_height)<=curr_dist: #no funk
                                                        #hay que separar los heights, de las distancias acumuladas(lo del infinito x default y eso)
                     curr_dist=i.height+actual_height
                     previous[i.value]=actual
                     distances[i.value]=curr_dist
                     i.curr_dist=curr_dist
                 
                 updated.append(i)
           
          
          
          #--------------------seleccionar el menor y para elegir a donde movernos----------------------
          menor=updated[0]
           
          for i in range(1,len(updated)):
              if updated[i].curr_dist<menor.curr_dist:
                 menor=updated[i]
           
           
          prev=actual.value
          actual=Remember_Node(value=menor.value,prev=previous[menor.value])#con este objeto mantenemos un track del path
          actual_height=distances[menor.value]
          
          #print(menor.value,previous[menor.value].value)

          cont+=1
          
                  


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


path,long=DJS(grafo,"a","f")

print(path)
print(long)



#cada vez que actualizamos poemos: