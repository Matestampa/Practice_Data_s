###--------------------------Binary Search Tree-----------------------------------------------###

#creacion--------- O(n**2),O(n.log(n))
#insertar(no se puede elegir donde)--------- O(log(n))
#delete----------- O(log(n))
#buscar----------- O(log(n))

class Node():
      def __init__(self,data,root):
          self.data=data
          self.root=root
          self.left=None
          self.right=None
      
      def __str__(self):

          return str(self.data)

class Bst_search():
      def __init__(self,root,value,response):
          options=["node","pos"]
          
          self.root=root
          self.value=value
          self.response=response
          
          if self.response not in options:
             raise TypeError(f"Response argument {self.response} not in the options")
      
      def run(self):
          if self.response=="node":
             return self.node_search(self.root,self.value)
          
          elif self.response=="pos":
             return self.pos_search(self.root,self.value)

      def node_search(self,dad,value):
           if dad==None:
             return False

           if value==dad.data:
             
              return dad
          
           elif value<=dad.data:
              return self.node_search(dad.left,value)
    
           elif value>=dad.data:
                return self.node_search(dad.right,value)  
      
      def pos_search(self,dad,value):
          if dad==None:
             return False

          if value==dad.data:
             
             if value<dad.root.data:
                pos="left"
             elif value>dad.root.data:
                 pos="right"
             
             return dad,pos
          
          elif value<=dad.data:
             return self.pos_search(dad.left,value)
    
          elif value>=dad.data:
             return self.pos_search(dad.right,value)

          
class Bst_getdata():#formas en las que se puede devolver la data del arbol
      def __init__(self,root,method):
          self.root=root
          self.method=method
      
      def get(self):
          if self.method=="pre_order":
             return self.pre_order(self.root)
          
          if self.method=="in_order":
             return self.in_order(self.root)
          
          if self.method=="post_order":
             return self.post_order(self.root)
      
      
      def in_order(self,root):
          if root==None:
             return []

          return self.in_order(root.left) + [root.data] + self.in_order(root.right)
          
          


class Bst():
      def __init__(self):
          self.cant_nodes=0
          self.depth=0
          self.root=None
      

      def create(self,lista):#creamos el arbol a partir de  un array

          self.root=Node(lista[0],None)

          for i in range(1,len(lista)):#no sirve
              self.__add(value=lista[i],root=self.root,dad_root=None)
              
      
      def append(self,value):
          self.__add(value,self.root,dad_root=None)#llamamos individualmente y funciona igual
      
      
      def __add(self,value,root,dad_root):#necesitamos el valor, la root y el papa de la root(root.root)

          if root==None:
             root=Node(value,dad_root)#si no tuvieramos el dad_root, y le pasaramos solo root; estariamos poiendo nen_node.root=None
             self.cant_nodes+=1      #aumentamos nodos generales
          
          else:
             
             if value<root.data: #si es menor
                root.left=self.__add(value,root.left,root) #vamos por la izquierda
             
             if value>root.data: #si es mayor
                root.right=self.__add(value,root.right,root) #vamos por la derecha
          
          return root
             
      
      def delete(self,value):
          searcher=Bst_search(root=self.root,value=value,response="pos")#indicamos que nos devuelva la posicion
          d_node,pos=searcher.run()#devuelve el obj Node encontrado, y en que posicion estaba respecto de su root(left,right)
      

          if d_node.left==None and d_node.right==None: #si no tieen hijos
             case="nothing"
             if pos=="left":
                d_node.root.left=None
             
             elif pos=="right":
                d_node.root.right=None
          
          elif d_node.left==None: #si no tiene el hijo left
               case="no left"
               if pos=="left":
                  d_node.root.left=d_node.right
               
               elif pos=="right":
                    d_node.root.right=d_node.left
               
               d_node.right.root=d_node.root

          
          elif d_node.right==None:#si no tiene el hijo right
               case="no right"
               if pos=="left":
                  d_node.root.left=d_node.left
               
               elif pos=="right":
                  d_node.root.right=d_node.left

               d_node.left.root=d_node.root
          
          else:                  #si tiene ambos(mas largo)
               case="both"
               pos="right"
               actual=d_node.right #definimos un actual(siempre el de la derecha)
               
               if actual.left==None: #si a su izquierda no hay nada
                  pos="right"
               
               else: #si a su izquierda hay algo, buscamos el minimo de alli
                  pos="left"
                  while actual.left!=None: #vamos todo para la izquierda
                        actual=actual.left
               
               d_node.data=actual.data #le asignamos el valor al delete_node, del nodo que hayamos encontrado optimo

               if pos=="left":
                  actual.root.left=None #separamos el optimo del arbol, asignando a su root.left=None
               
               elif pos=="right":
                    d_node.right=actual.right #separamos el optimo, asignando a su root(el delete_node), su hijo derecho
                    d_node.right.root=actual.root #a su hijo derecho le ponemos como root el delete_node

         
          print("deleted",case)
             
          
       
      def show(self,method):
          
          cursor=Bst_getdata(self.root,method)

          print(cursor.get())



#formas de traverse el arbol

#pre order: root-left-right (nos da todos los subtres con el padre al principio (cada conjunto de 3))

#in_order:  left-root-right (nos da el arbol ordenado de menor a mayor)

#post_order: left-right-root (nos da todos los subtres con el padre al final (cada conjunto de 3))







          
