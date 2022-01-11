from random import randint,choice
import time
from sys import exit
import os

#-----------------merge sort---------------------------------------------

lista=[33, 9, 28, 9, 18, 31, 26, 30,21,11]


def mostrar(lista):
	for i in range(len(lista)):
		print("*" * lista[i])



def merge(a,b):
    lista1=a
    lista2=b
    new_list=[]
    i=0
    j=0
    while True:
          
          if lista1[i]<lista2[j]:
             new_list.append(lista1[i])
             i+=1

          else:
             new_list.append(lista2[j])
             j+=1

          if i==len(lista1):
             new_list.append(lista2[j])
             break

          if j==len(lista2):
             new_list.append(lista1[i])
             break 
    
    mostrar(new_list)
    time.sleep(2)
    os.system("cls")
    return new_list

def partir(lista,s,f):
    
      
   if len(lista[s:f+1])<=1:
      return lista[s:f+1]
      
   else:
      mitad=len(lista[s:f+1])//2
      mitad=s+mitad
      return merge(partir(lista,s,mitad-1), partir(lista,mitad,f))

#print(lista)
print(partir(lista,0,9))






