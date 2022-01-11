from tkinter import *
from backend.build_heap import max_heap
from backend.sort import heap_sort
from frontend.tree import draw_tree
from frontend.array import draw_array
from random import randint
from time import sleep
#itemconfigure

#---------------------extras------------------------------
def int_list(lista):
    l=lista
    for i in range(len(lista)):
        l[i]=int(l[i])
    return l


def delete_canvas(**kwargs):#se encarga de destruir el canvas como de borra el objeto
    global dibujo
    try:
        dibujo.delete()
        del dibujo
        if kwargs[todos]==True: #cuando volvemos a hcer show, borramos el entry tmb para ahorra espacio
            anim_array.delete()
            del anim_array
    
    except NameError: #para cuando no lo definimos todavia
        pass


def show_changes(tree,array,ch1,ch2): #hace la animacion del arbol , como del array
    tree.highlight(ch1,ch2)
    anim_array.highlight(ch1,ch2)
    raiz.update()
    sleep(1)
    
    tree.change([ch1,array[ch1]], [ch2,array[ch2]])#[index,valor de ese index para ponerselo al contrario]
    anim_array.change([ch1,array[ch1]], [ch2,array[ch2]])
    raiz.update()
    sleep(1)

#----------------botones---------------------------------------
def show(lista):
    global dibujo
    global anim_array
    
    delete_canvas(todos=True)
    
    dibujo=draw_tree(frame_canvas)
    dibujo.create(lista)

    anim_array=draw_array(frame_inferior,lista)#creamos un objeto que se encarge de mostrar el array(solo hacemos uno)

    boton_heapify.config(state=ACTIVE)



def heap(lista):
    global heap_list
    global dibujo
    
    lista=int_list(lista)
    
    heap_list,fases=max_heap(lista)#obtenemos la lista ya heapizada, y las fases(dict:[array]   [fase])
                                                                                               #(cambios sobre ese array)
    len_fases=len(fases)

    delete_canvas()
    
    for i in range(1,len_fases):#por cada array,fase --> creamos un objeto(canvas) que dibuje el arbol. Cuando pasamos a otra fase lo borramos
        array=fases[i][0]
        fase=fases[i][1]
        
        largo=len(fase)
        
        dibujo=draw_tree(frame_canvas)
        dibujo.create(array)

        raiz.update()
        sleep(1)

        if largo>1:
           for j in range(largo-1):
               change1,change2=fase[j],fase[j+1]
           
               show_changes(dibujo,array,change1,change2)#esto hace tanto el highlight como el change, y hace las pausas
           
               array[change1],array[change2]=array[change2],array[change1]#luego de cambiar en el grafico hay que cambiar el array de la fase
        
        if i<(len_fases-1):#borramos todos menos el ultimo, asi queda hasta que pulsemos el sort
           delete_canvas()
    
    boton_sort.config(state=ACTIVE)


def sort():
    global dibujo
    
    delete_canvas()
    
    hp=heap_list
    fases=heap_sort(hp)

    dibujo=draw_tree(frame_canvas)
    dibujo.create(hp)
    
    raiz.update()
    sleep(1)
     
    for i in range(len(fases)):
        fase=fases[i]
        largo=len(fase)
        if largo>1:
           for j in range(largo-1):
               change1,change2=fase[j],fase[j+1]

               show_changes(dibujo,hp,change1,change2)

               hp[change1],hp[change2]=hp[change2],hp[change1]



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
frame_canvas=Frame(width=ancho,height=alto)
frame_canvas.pack()


boton_show.config(command=lambda:show(entry_array.get().split(",")))
boton_heapify.config(command=lambda:heap(entry_array.get().split(",")),state=DISABLED)
boton_sort.config(command=sort,state=DISABLED)

#===================frame de abajo=================se modifica el array
frame_inferior=Frame(width=ancho,height=100,bg="grey")
frame_inferior.pack()


raiz.mainloop()






