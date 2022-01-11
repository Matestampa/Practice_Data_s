#---------------------------------- LINKDED LISTTT --------------------------------------------------

"""cada elemento de la estructura puede estar en un lugar diferente de memeoria
por eso cada uno de stos, ademas de el dato, contiene un pointer que indica la direccion del siguiente.


-------------------------------------------------------------------------
operaciones:

indexar---->salvo el primero los demas es O(n)
insertar y delete---------> tambien O(n) xq para hacer eso primero hay que buscarlo
insertar al principio---------> O(1)
delete al principio------------> O(1)

insertar al final-------------> O(1)
delete al final---------------> O(n)

para buscar un elemento, tenemos que pasar x todos los anteriores.


-----------------------------------------------------------------------------
ventajas:
     solo usa la memoria necesaria para los datos justos
     no como el array que aunque necesites 11, guarda espacio para 20.

------------------------------------------------------------------------------
#ejemplo:
      #se usa una linked list para el atras y adelante en el navegador
      #o para el atras y adelante en word, pptx, etc"""


#como seria

class Node():
      def __init__(self,dataval):
          self.value=dataval
          self.next=None



class Linked_list():
      def __init__(self,value):
          new_node=Node(value)
          self.head=new_node
          self.last=new_node
      
      def append(self,value): #metemos un nuevo nodo al final
          new_node=Node(value)
          self.last.next=new_node
          self.last=new_node
       
      def prepend(self,value):# metemos un nuevo nodo al principio
          new_node=Node(value)
          new_node.next=self.head

          self.head=new_node
      
      def insert(self,value,index): #para insertar en un determinado lado, hay que iterar hasta donde diga

          new_node=Node(value)

          actual=self.head
          cont=0

          while True:
                if cont==index:
                   prev.next=new_node
                   new_node.next=actual
                   
                   break

                else:
                    cont+=1
                    prev=actual
                    actual=actual.next

      
      def pop(self):#eliminamos el ultimo elemento. Mentira, no se puede. Solo estariamo eliminando el last dentro de la clase
                    #pero si le preguntamo el next, al anteultimo, seguiria apareciendo
                    #por ende para deletear al final,hay que iterar hasta el anteultimo
          del self.last


      def show(self):#mostramos toda la lista
          actual=self.head

          while actual!=None:
                print("{}-------->{}".format(actual,actual.next))
                actual=actual.next





###------------------------------Double Linked List---------------------------------------------------------####

class DoubleNode():
      def __init__(self,value,prev,next=None):
          self.value=value
          self.next=next
          self.prev=prev
      

      def __str__(self):
          return self.value




class DoubleLinked_list():
      def __init__(self,dataval):
          self.head=DoubleNode(value=dataval, prev=None)
          self.last=self.head

      
      def append(self,value):
          new_node=DoubleNode(value=value, prev=self.last)
          self.last.next=new_node
          self.last=new_node
      
      def prepend(self,value):
          new_node=DoubleNode(value=value, prev=None, next=self.head)
          self.head.prev=new_node
          self.head=new_node
      
      def pop(self,node):

          self.last=node.prev #le pasamos el nodo que queremos eliminar(siempre el ultimo), seteamos el last al anterior de dicho nodo
                                                                                            #y ademas lo deleteamos

          del node


      def show(self):
          actual=self.head

          while actual!=None:
                print("{}<----{}---->{}".format(actual.prev,actual,actual.next))
                actual=actual.next

