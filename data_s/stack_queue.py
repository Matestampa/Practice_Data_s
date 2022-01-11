

"""#el stack es basicamente: "El primero que entra, el ultimo que se va"
#es decir, solo podemos agrgar al principio, y deleteamos uno, es el del final

---------------------------------------------------
operaciones:
       insertar-------->O(1)
       delete----------O(1)
       buscar---------->O(1)

---------------------------------------------------

ejemplos:
      el stack se podria construir con una linked list
      por eso tambien aplicaria el ejemplo del editor de texto o el navegador
      para dar vuelta una palabra tambien es util
      para chequear si se cierran parentesis, llaves, etc en un texto


------------------------------------------


"""

#como seria

class Stack():
      def __init__(self):
          self.lista=[]
          self.pointer=0
      

      def push(self,value):#agregar al final
          self.lista.append(value)
          self.pointer+=1
      

      def pop(self): #sacar al final
          del self.lista[self.pointer-1]
          self.pointer-=1
      
      def get_last(self):
          return self.lista[self.pointer-1]
      
      def is_empty(self):
          if self.pointer==0:
             return True
          
          return False
      

      def show(self):
          print(self.lista)



#------------------------------- QUEUE ---------------------------------------

""" el queue es basicamenet: el primero que entra, es el primero que sale
   es decir, solo podemos insertar al final, y deletear al principio


------------------------------------------------------------------
operaciones:
     insertar--------->O(1)
     delete----------->O(1)
     buscar----------->O(n)

----------------------------------------------------------------

ejemplo:
      el queue tambien se podria construir con una linked list
      se podria usar para handlear los requests del servidor en orden



---------------------------------------------------------


"""

#asi seria

class Queue():
      def __init__(self):
          self.lista=[]
          self.pointer=0
      

      def push(self,value): #agregar al final
          self.lista.append(value)
          self.pointer+=1
      

      def pop(self): #sacar al principio
          to_delete=self.lista[0]
          del self.lista[0]
          self.pointer-=1

          return to_delete
      
      def get_first(self):
          if self.pointer==0:
              return None
          return self.lista[0]
      
      def is_empty(self):
          if self.pointer==0:
             return True
          
          return False
      

      def show(self):
          print(self.lista)



"""Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"""