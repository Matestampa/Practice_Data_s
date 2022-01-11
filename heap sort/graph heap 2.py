from tkinter import *
from backend.build_heap import max_heap
from backend.sort import heap_sort
from frontend.graficos import show_tree

#itemconfigure

def int_list(lista):
  l=lista
  for i in range(len(lista)):
    l[i]=int(l[i])
  return l


def show(lista):#esto destruye el canvas para tener uno nuevo ,y llama a la func dibujar
    global cv
    cv.destroy()
    cv=Canvas(frame_canvas,width=800,height=500,bg="grey")
    cv.pack(expand=YES,fill=BOTH)
    show_tree(cv,lista)


def heap(lista):#esto convierte lo del entry a numeros, lurgo hace el max heap y luego llama a show
    global heap_list
    lista=int_list(lista)
    heap_list=max_heap(lista)
    
    print(heap_list)
    show(heap_list)


def sort():#utiliza el max heap de la func de arriba y hace el sort
  sort_list=heap_sort(heap_list)
  print(sort_list)
  show(sort_list)



#-----------------------inicial grafico-----------------------
raiz=Tk()

ancho=800
alto=500

#===================frame de arriba==================se ingresa el array
frame_superior=Frame(width=ancho,height=100)
frame_superior.pack()

label=Label(frame_superior,text="Numeros sep by comas:")
label.grid(row=0,column=0)

entry_array=Entry(frame_superior,width=30)
entry_array.grid(row=0,column=1)

boton_show=Button(frame_superior,text="show")#,command=lambda:show(entry.get().split(",")))
boton_show.grid(row=0,column=2)

boton_heapify=Button(frame_superior,text="heapify")
boton_heapify.grid(row=0,column=3)

boton_sort=Button(frame_superior,text="sort")
boton_sort.grid(row=0,column=4)

#===================canvas en el medio==============
frame_canvas=Frame()
frame_canvas.pack()

cv=Canvas(frame_canvas,width=ancho,height=alto,bg="grey")
cv.pack(expand=YES,fill=BOTH)

boton_show.config(command=lambda:show(entry_array.get().split(",")))
boton_heapify.config(command=lambda:heap(entry_array.get().split(",")))
boton_sort.config(command=sort)

#===================frame de abajo=================se modifica el array
frame_inferior=Frame(width=ancho,height=100)
frame_inferior.pack()

for i in range(10):
  entry=Entry(frame_inferior,width=3)
  entry.grid(row=0,column=i)
    

raiz.mainloop()
