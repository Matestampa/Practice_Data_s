"""#Reverse a Linked List-------Linked List-------------------------------------------
from data_s.linked_list import Linked_list


#a-> b-> c-> d-> e->none
#e-> d-> c-> b-> a->none


def traverse(head):
    #primero tratamos los primeros dos
    #--------------------------------
    first_head=head   #guardamo esta para el else final
    proxim=first_head.next
    proxim_2=proxim.next
    proxim.next=first_head

    prev=proxim
    head=proxim_2
    #--------------------------------
    #luego el resto. En este punto, head ya es el tercer elemento de la Linked List
    
    while True:
          if head.next!=None:
             proxim=head.next
             head.next=prev

             prev=head
             head=proxim
          
          else:
             head.next=prev
             first_head.next=None
             break
    
    return head
             

#creamos lista

lista=Linked_list("a")

lista.append("b")
lista.append("c")
lista.append("d")
lista.append("e")

lista.head=traverse(lista.head) #asignamos la nueva head
                                #pordriamos hacer una funcion dentro de la clase para llamar directo a "lista.traverse()"


lista.show()"""


#-------------------------------------------------------------------------------------------------------------------------------------
#simulacion del boton de atras y adelenate de Google, Firefox, etc.------Double Linked List------------------------------------

from data_s.linked_list import DoubleLinked_list, DoubleNode


class Navigation():
      def __init__(self,value):
          self.lista=DoubleLinked_list(value)
          self.actual=self.lista.head


      def back(self):
          prev=self.actual.prev
          self.actual=prev
          return self.actual

      def forward(self):
          next=self.actual.next
          self.actual=next
          return self.actual
      

      def new(self,value):#si hacemos uno nuevo estando adelante de todo no pasa nada(simplemente se agrega)
                          #pero si lo hacemos una vez que ya volvimos hacia atras, hay que borrar todos los que esten por delante

          if self.actual.next!=None: #si hay algo adelante
             actual=self.lista.last.prev

             while actual.next!=self.actual:
                   self.lista.pop(actual.next)
                   actual=actual.prev
          
          
          self.lista.append(value)
          
          return self.forward()


nav_hist=Navigation("esmikell")


res=""

while res!="c":
      res=input(":")

      if res=="b":
         actual=nav_hist.back()
      

      if res=="n":
         actual=nav_hist.forward()
      
      if res=="new":
         url=input("url:")
         actual=nav_hist.new(url)
      
      print(actual)