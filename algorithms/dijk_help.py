
class First():
      def __init__(self):
          self.value="finish"
          self.prev=None

class Element():
      def __init__(self,value,distance,prev):
          self.value=value
          self.distance=distance
          self.prev=prev


#Los objetos completos los guardamos en una lista
#Pero guardamos aparte sus index en un dict cuya key es el object.value

#Esto nos sirve para no tener que iterar hasta encontrar el eleemento en la lista(ya que tenemos que hacer mucho esto)
#Con este sistema agarramos el index con el value (index=indexes[value]) y lo traemos directo de la lista (object=elements[index])

class P_Queue():
      def __init__(self):
          self.objects=[]
          self.indexes={}
          self.pointer=0 #siempre nos va a dar el index del ultimo eleemento
      
      def __re_order(self,index):
          
          for i in range(index,self.pointer-1): #sabemos que en el caso de Djs,solo se actualiza si es algo mas chico, por lo tanto es al pedo fijarse 
                                                #los que ya sabemos que son mas grandes
              value1=self.objects[i].value
              value2=self.objects[i+1].value

              if self.objects[i].distance < self.objects[i+1].distance:
       
                 self.objects[i],self.objects[i+1]=self.objects[i+1],self.objects[i]

                 self.indexes[value1]=i+1
                 self.indexes[value2]=i
              
              else:
                 break
          
      
      def add(self,value,send_back=False):
          new=Element(value,distance=1000,prev=None)
          self.indexes[value]=0

          self.objects.insert(0,new)

          self.__re_order(0)
          
          self.pointer+=1

          if send_back==True:
             return new
       
      def update(self,value,distance,prev): #esto se puede modificar, segun los atributos de cada objeto

          index=self.indexes[value]
          
          self.objects[index].distance=distance
          self.objects[index].prev=prev

          self.__re_order(index)


      def pop(self):
          to_delete=self.objects[self.pointer-1]
          
          del self.objects[self.pointer-1]
          del self.indexes[to_delete.value]
          
          self.pointer-=1
          
          return to_delete

          
          
      def get(self,value):
          try:
              index=self.indexes[value]
              return self.objects[index]
          
          except KeyError:
              return None



#arreglo 1:
         #hacer el queue al reves
         #al eliminar un elemento no se modifica ningun index
         #cuando se agrega se sigue modificando los indexes
         #cuando se actualiza tambien

#arreglo 2:
         #hacer el queue al reves
         #con cada comparasion en el reorder,cambiar tambien los indexes en caso de intercambiar lugar
         #al eliminar un elemento no se modifica ningun index
         #cuando se agrega todo seguiria normal
         #cuanso se hace update... vienen los problemas:
                 #hay que mover el objeto hasta el prijcipio, y compararlo hasta el final
                 #lo cual nos modifica indexes automaticamente, 

#arreglo 3:
         #en elements solo guardamos las keys
         #hacemos el queue al reves
        #al elimianr no hay problema
         #al añadir no hay problema
         #al updatear:
                   #insertamos el eleemento al principio
                   #deleteamos su antiguo index