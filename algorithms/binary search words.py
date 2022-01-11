nombres=["colo","cule","culito","culitazo","culeozo","culon","culona","culonay"]

letras={}
cont=0
for i in "abcdefghijklmnopqrstuvwxyz":
    letras[i]=cont
    cont+=1

print(letras)


def compare(actual,target):
    len_target=len(target)
    iguales="false"
    
    for i in range(len_target):
        try:
            if letras[target[i]]<letras[actual[i]]:
               return "menor"

            elif letras[target[i]]>letras[actual[i]]:
                 return "mayor"

            else:
               iguales="true"

        except:
            return "mayor"
    
    if len(actual)>len_target:
       return "menor"

    else:
       return "iguales"




def binary(left,right,target):
    if (right-left)==0:
        return 0
    
    mitad=(right-left)//2
    mitad=left+mitad
     
    actual=nombres[mitad]
    
    result=compare(actual,target)

    if result=="menor":
       return binary(left,mitad,target)

    elif result=="mayor":
        return binary(mitad,right,target)

    else:
       return 1,mitad



print(binary(0,len(nombres),"culona"))




