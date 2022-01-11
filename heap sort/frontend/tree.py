from tkinter import *
from frontend.extras import nodo

class draw_tree():#hacemos una clase, para no tener que crear un canvas cada vez que queremos cambiar algo
      def __init__(self,parent):
          self.canvas=Canvas(parent,width=800,height=500,bg="grey")
          self.canvas.pack(fill=BOTH,expand=YES)

#---------------dedicadas a modificarlo------------------------------------------------------      
      def delete(self):
          self.canvas.destroy()
      

      def change(self,combo1,combo2):#cada combo tiene su index con su valor. Entonces los cambiamos
          self.canvas.itemconfigure(str(combo1[0])+"text",text=combo2[1])
          self.canvas.itemconfigure(str(combo2[0])+"text",text=combo1[1])

      def highlight(self,num1,num2):#coloreamos los a cambiarse
          self.canvas.itemconfigure("square",fill="red")#ponemos tods en rojo para restablecer
          self.canvas.itemconfigure(str(num1)+"square",fill="green")
          self.canvas.itemconfigure(str(num2)+"square",fill="green")




#---------------------------dedicadas a crear el dibujo-----------------------------------
      def graph_son(self,x,y,clase,num,i):#metodo de antes
          dist_x=self.cons_figura
          dist_y=self.cons_figura
    
          #aca llevamos las coords a donde debe empezar el nuevo cudadrado(dependiendo de que lado este)
          if clase=="impar":
             new_x=x-self.dist_gen_x
             new_y=y+self.dist_gen_y
             dist_x*=-1
    
          if clase=="par":
             new_x=x+self.dist_gen_x
             new_y=y+self.dist_gen_y
    
          self.canvas.create_line(x,y,new_x,new_y)
          self.canvas.create_rectangle(new_x,new_y,new_x+dist_x,new_y+dist_y,fill="red",tags=(str(i)+"square","square"))
          self.canvas.create_text(new_x+(dist_x/2),new_y+(dist_y/2),text=num,font=("Arial",12),tags=(str(i)+"text","text"))
          #agregamos las etiquteas (num+square) o (num+text) depende si queremos cambiar el tetxo o el rectangulo




      def create(self,lista):#metodo de antes
          nodes=[]

          x=400
          y=20
          
          self.cons_figura=60
          self.dist_gen_x=80
          self.dist_gen_y=10

          anterior=0

          for i in range(len(lista)//2):
              if i==0:
                 self.canvas.create_rectangle(x,y, x+self.cons_figura, y+self.cons_figura,fill="red",tags=(str(i)+"square","square"))
                 self.canvas.create_text(x+(self.cons_figura/2),y+(self.cons_figura/2),text=lista[0],font=("Arial",12),
                                         tags=(str(i)+"text","text"))
                 size=self.cons_figura
          
                 self.cons_figura-=10
                 self.dist_gen_x-=10

                 new_node=nodo([x,y],size,self.dist_gen_x,self.cons_figura)
                 nodes.append(new_node)


              else:
                 if i%2==0:
                    padre=i//2-1

                 else:
                    padre=i//2
            
                 padre=nodes[padre] #tenemos el objeto padre
            
                 x,y=padre.get_son_cords(i) #pedimos las cordenadas del nodo enel que estamos
                 size=padre.size_son #definimos el tamaño del nodo en el que estamos

                 new_node=nodo([x,y],size,self.dist_gen_x,self.cons_figura)#creamos un objeto nuevo
                                                            #cons_figura seria el tamaño de los hijos, y disx de la flecha
                 nodes.append(new_node)
   
       
              hijo1=i*2+1
              hijo2=i*2+2

              self.graph_son(x , y+size,"impar",lista[hijo1],hijo1) #con esto ponemos 
        
              if hijo2<len(lista):
                 self.graph_son(x+size, y+size ,"par",lista[hijo2],hijo2)#las coords en las esquinas inferiores

              if i==0:
                 self.cons_figura-=10
                 self.dist_gen_x-=30

        
              if i==(2+(anterior*2)):#bajamos tamaño cuando bajamos de nivel 
                 self.dist_gen_x-=10
                 self.cons_figura-=10
                 anterior=i



'''def graph_son(x,y,clase,num):
    dist_x=cons_figura
    dist_y=cons_figura
    
    #aca llevamos las coords a donde debe empezar el nuevo cudadrado(dependiendo de que lado este)
    if clase=="impar":
       new_x=x-dist_gen_x
       new_y=y+dist_gen_y
       dist_x*=-1
    
    if clase=="par":
        new_x=x+dist_gen_x
        new_y=y+dist_gen_y
    
    cv.create_line(x,y,new_x,new_y)
    cv.create_rectangle(new_x,new_y,new_x+dist_x,new_y+dist_y,fill="red")
    cv.create_text(new_x+(dist_x/2),new_y+(dist_y/2),text=num,font=("Arial",12))


#-----------------------MAIN-----------------------------------------------------

def show_tree(obj,lista):
    global dist_gen_x
    global dist_gen_y
    global cons_figura
    global cv
    cv=obj
    nodes=[]

    x=400
    y=20

    cons_figura=60

    dist_gen_x=80
    dist_gen_y=10

    anterior=0

    for i in range(len(lista)//2):
        if i==0:
           cv.create_rectangle(x,y,x+cons_figura,y+cons_figura)
           cv.create_text(x+(cons_figura/2),y+(cons_figura/2),text=lista[0],font=("Arial",12))
           size=cons_figura
          
           cons_figura-=10
           dist_gen_x-=10

           new_node=nodo([x,y],size,dist_gen_x,cons_figura)
           nodes.append(new_node)


        else:
            if i%2==0:
               padre=i//2-1

            else:
               padre=i//2
            
            padre=nodes[padre] #tenemos el objeto padre
            
            x,y=padre.get_son_cords(i) #pedimos las cordenadas del nodo enel que estamos
            size=padre.size_son #definimos el tamaño del nodo en el que estamos

            new_node=nodo([x,y],size,dist_gen_x,cons_figura)#creamos un objeto nuevo
                                                            #cons_figura seria el tamaño de los hijos, y disx de la flecha
            nodes.append(new_node)
   
       
        hijo1=i*2+1
        hijo2=i*2+2

        graph_son(x , y+size,"impar",lista[hijo1]) #con esto ponemos 
        
        if hijo2<len(lista):
           graph_son(x+size, y+size ,"par",lista[hijo2])#las coords en las esquinas inferiores

        if i==0:
           cons_figura-=10
           dist_gen_x-=30

        
        if i==(2+(anterior*2)):#bajamos tamaño cuando bajamos de nivel 
           dist_gen_x-=10
           cons_figura-=10
           anterior=i'''


