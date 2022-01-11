from data_s.stack_queue import Stack,Queue

"""#First non-repeating character--------------Queue-------------------------------------------------------------
   #apartir de un string, por cada caracter hay que devolver el primer no repetido de la cadena

def fn_repeated(string):
    
    queue=Queue()
    rev_string=""
    repes=""

    queue.push(string[0])
    rev_string+=string[0]
    
    for i in range(1,len(string)):
        
        char=string[i]
        
        first=queue.get_first()
        
        if char in repes:
           if first==None: #si esta vacio
              rev_string+="#"
           
        
        else:
           if char==first:
              repes+=char
              queue.pop()
              
              new_first=queue.get_first()

              if new_first==None: #si esta vacio
                 rev_string+="#"
              else:
                  rev_string+=new_first
           
           else:
               queue.push(char)
               rev_string+=queue.get_first()

        
    return rev_string

        
string="abcabc"

print(fn_repeated(string))"""

#----------------------------------------------------------------------------------------------------------------

"""#verificar que los brackets esten bien cerrados, u colocados-----------Stack--------------------------

from stack_queue import Stack

bracks="([])[)())"

forwards="(["

equals={"(":")","[":"]"}

def is_balanced(string):
    stack=Stack()
    stack.push(string[0])
    
    for i in range(1,len(string)-1):
        actual=string[i]

        if actual in forwards: #si esta en los signos hacia adelante, lo metemos en el stack
           stack.push(actual)
        
        else:
            if stack.is_empty(): #si no es hacia delante y esta vacio, no tiene nonguna pareja
               return "False, nonforward "+actual+" alone"

            else:
                 last=stack.get_last()
                 if actual==equals[last]: #si es hacia adelante y corresponde al opuesto del ultimo del stack, lo sacamos
                    stack.pop()
            
                 else:#si no corresponde, tambien esta mal
               
                    return "False "+ last + actual
     
    return True
        
print(is_balanced(bracks))"""

#----------------------------------------------------------------------------------------------------------------------------

"""#Next shortest element(incompleto)----------------Stack-----------------------------------------------------------------

def ns_element(lista):
    
    new_list=[]
    actual=lista[0]
    minors=[lista[0]]

    for i in range(1,len(lista)):
        for j in range(len(minors)):
            if minors[j]<lista[i]:
                new_list.append(minors[j])




A = [4, 5, 2, 10, 8]

result=ns_element(A)


#fijarse los menores

#ex  4,5,3,10

#agregamos 4
#5 es menor---no ----Lo agregamos
#3 es menor---si ----lo agregamos y sacamos el resto
#10 es menor---no ----lo agregamos"""


#----------------------------------------------------------------------------------------------------------------------------




