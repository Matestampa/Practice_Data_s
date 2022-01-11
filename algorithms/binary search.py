def binary(num,s,f):
    if s>=f:
       return -1

    mitad=(f-s)//2
    if num<lista[mitad]:
       return binary(num,s,mitad-1)

    elif num>lista[mitad]:
         return binary(2,mitad+1,s)

    else:
         return 0,mitad




print(binary(-2,0,len(lista)))