class nodo():
  def __init__(self,cords,size,dist_x,son):#cords del actual, size del actual, distancia de la flecha que desplego,
                                          #tamaño de los hijos
                                          #pasandole aca el tamaño de los hijos, luego cuando estemos en los hijos
                                          #podemos consultar su tamño consultando en el objeto padre
    self.y=10
    
    self.cords=cords
    self.size=size
    self.dist_x=dist_x
    self.size_son=son

    
  def get_son_cords(self,num):#aca devolvemos las coordenadas del actual en la esquina superior izquierda
      if num%2==0:#si es par
        x=self.cords[0]+self.size+self.dist_x
        y=self.cords[1]+self.size+self.y

      else:#si es impar
        x=self.cords[0]-self.dist_x-self.size_son
        y=self.cords[1]+self.size+self.y

      return x,y
