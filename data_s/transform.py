import string
import os
from binary_tree import Bst

abc=dict()
cont=1
for i in string.ascii_lowercase:
    abc[i]=cont
    cont+=1


def ABC_2_Number(lista):
    no_wanted=",.;!?¡¿()"
    new_list=[]
    for i in lista:
        #number=abc[i[0]] * 10
        number=0
        cont=1
        for j in reversed(i):
            char=j.lower()
            
            if char not in no_wanted:
               number+=abc[char] *cont
               cont+=1
            
            else:
                pass
        
        new_list.append(number)
    
    return new_list


def get_text(file):

    with open(file,"r") as archivo:
         text=archivo.read()
         archivo.close()
    
    text=text.split(" ")

    return text

def write_text(file,lista):
    with open(file,"w") as archivo:
         for i in lista:
             archivo.write(str(i)+" ")
         
         archivo.close()

words=get_text("hey.txt")

num_list=ABC_2_Number(words)

write_text("hey.txt",num_list)

