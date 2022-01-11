#tenemos los nodos(vertices) y las aristas(edges) que los conectan

#los edges pueden tener un peso. Es decir un valor que asignamos dependiendo
#para que estemos usando el grafo.
#por ejemplo si es para distancia, a cada edge le vamos a poner los kilometros


#Clasificacion segun tipos de edges:
     
     #-undirected: el grafo por defecto,donde la conexion es bidireccional  a<--->b

     #-directed: la conexion entre vertices es unidirectional      a---->b

#---------------------------------------------------------------------------------------------------------

#Tipos de representacion como Data Structure:
     
     #-adjacency Matrix: 
       #Hacemos una matriz poniendo los vertices, tanto en las filas como columnas.
       #Si hay un edge que conecta dos vertices, ponemos un 1 en Matrix[i][j]. Sino un 0

       #Pros:
          #mas util si hay muchos edges,y menos vertices
       
       #Cons:
          #Ocupa mucha memoria al pedo
          
     
     
     #-adjacency list:
       #Guardamos todos los vertices en un array. A cada uno lo linkemaos a una linked list con sus vecinos
       
       #Pros:
           #Sirve cuando hay muchos verices, pero pocos edges
       
       #Cons:
           #Cuando eliminemos un vertice va a ser un quilombo, xq hay que eliminarlo en todos lados que aprezca



#Implementacion usando adjacency list.

class Edge():
      def __init__(self,value,height):
          self.value=value
          self.height=height
          self.curr_dist=0

          self.next=None
      
      def __str__(self):

          return self.value+"/"+str(self.height)


class Edges_list():
      def __init__(self):
          self.head=None
          self.last=None
      
      def append(self,value,height):
          new_node=Edge(value,height)
          if self.head==None:
             self.head=new_node
             self.last=new_node
          
          else:
             self.last.next=new_node
             self.last=new_node
      
      def remove(self,value):
          prev=None
          actual=self.head

          while True:
                if actual.value==value:
                   
                   if prev==None: #si es el primero
                      if actual.next!=None: #y tiene uno adelante
                         self.head=actual.next
                      
                      else:#si es el unico(xq tampoco tiene uno adelante)
                          self.head=None
                   
                   elif actual.next==None:#si es el ultimo
                        prev.next=None
                   
                   else:#si esta en el medio de dos
                        prev.next=actual.next
                   
                   del actual
                   break
                        
                else:
                    prev=actual
                    actual=actual.next
                   
      def get_all(self):
          lista=[]
          actual=self.head

          while actual!=None:
                lista.append(actual)
                actual=actual.next
          
          return lista
      
      def search(self,value):
          actual=self.head

          while actual!=None:
                if actual.value==value:
                   return True
                
                actual=actual.next
          
          return False
                
      
      def show(self):
          actual=self.head
          string=""
          while actual!=None:
                string+="--->{}".format(actual)
                actual=actual.next
          
          return string



class Vertex():
      def __init__(self,value):
          self.value=value
          self.neighs=Edges_list()
      
      def connect(self,value,height):
          self.neighs.append(value,height)
      
      def disconnect(self,value):
          self.neighs.remove(value)
      
      def get_neighs(self):#devulve lista con sus conexiones
          
          return self.neighs.get_all()
      
      def has(self,value): #devuelve True or False si encuentra la conexion con ese vertex o no

          return self.neighs.search(value)
      
      def show(self):
          print(self.value+":"+self.neighs.show())

          
#Falta comprobar si los vertex que pasamos en las funciones, existen en nuestro grafo
class Graph():
      def __init__(self):
          self.vertexs={}
      
      def add_vertex(self,value):
          self.vertexs[value]=Vertex(value)
      
      def remove_vertex(self,value):
          
          neighs=self.vertexs[value].get_neighs()

          for i in neighs:
              self.vertexs[i.value].disconnect(value)
          
          del self.vertexs[value]

          
      def add_edge(self,v1,v2,height=0):#lo hacemos bidireccional por defecto. Si lo quisieramos uni solo lo hariamos con el que pasen primero
          self.vertexs[v1].connect(v2,height)
          self.vertexs[v2].connect(v1,height)

      def remove_egde(self,v1,v2):
          self.vertexs[v1].disconnect(v2)
          self.vertexs[v2].disconnect(v1)
      
      def get_vertex(self,value):

          return self.vertexs[value]
      
      def show(self):
          for i in self.vertexs.keys():
              self.vertexs[i].show()