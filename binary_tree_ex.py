from data_s.binary_tree import Bst,Bst_search

"""#Find last common ancestor(encontrar el ultimo nodo compartido entre dos nodos)-------------------------------------------------------

def search_ancestors(node,root,lista):

    if node.data==root.data:
       return lista
    
    else:
       lista.append(root.data)
       if node.data<=root.data:
          return search_ancestors(node,root.left,lista)
       
       elif node.data>=root.data:
          return search_ancestors(node,root.right,lista)


def get_max(lista1,lista2):
    len1=len(lista1)
    len2=len(lista2)
    
    if len1>len2:
        return lista1,lista2
    
    elif len2>len1:
         return lista2,lista1
    
    else:
         return lista1,lista2
    

def Find_CM(root,value1,value2):
    #-----------buscamos los valores------------
    searcher=Bst_search(root,value1,response="node")
    node1=searcher.run()
    searcher.value=value2
    node2=searcher.run()
    
    #-----------buscamos los ancestros de cada uno--------------
    ancestors1=search_ancestors(node1,root,[])
    ancestors2=search_ancestors(node2,root,[])
    
    #-----------conseguimos la lista mas larga y corta(para poder comparar sin index error)---------------
    maxim,minim=get_max(ancestors1,ancestors2)
    
    #encontramos el comun
    for i in range(len(maxim)):
        try:
            if maxim[i]==minim[i]:
               ancestor=maxim[i]
        
            else:
                break
        except:
                break
    
    return ancestor
            
       

lista=[15, 10, 20, 8, 12, 16, 25]

bst=Bst()
bst.create(lista)

bst.show(bst.root)

common=Find_CM(bst.root,12,8)

print(common)

"""


# Find K smallest node(dado un indice k,tenemos que encontrar el menor en esa ubicacion)--------------------------------------------------
                      #(tenemos que recorrer el arbol en forma de menor a mayor(para eso lo hacemos el traverse in-order))

class Int_autoinc():
      def __init__(self,value):
          self.value=value
      
      def update_and_check(self): #cuando llamamaos a la funcion aumenta y devuelve el valor
                                  #nos ahorra tener que aumentar la variable manualmente dentro de la funcion
          self.value+=1
          return self.value



def K_smallest(root,k,cont=Int_autoinc(0)):
    if root==None:
       return
    
    
    left=K_smallest(root.left,k,cont)
    
    if cont.update_and_check()==k:
       print(cont.value,root)
       return root
    
    if left==None:
       left=K_smallest(root.right,k,cont)

    return left


lista=[15, 10, 20, 8, 12, 16, 25]

bst=Bst()
bst.create(lista)

small_k=K_smallest(bst.root,7)

print(small_k)

#--------------------------------------------------------------------------------------------------------------------------------