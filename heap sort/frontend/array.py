from tkinter import *

class draw_array():
	  def __init__(self,parent,array):
	  	  self.entrys=[]
	  	  for i in range(len(array)):
	  	  	  entry=Entry(parent,width=3,bg="red")
	  	  	  entry.grid(row=0,column=i)
	  	  	  entry.insert(0,array[i])

	  	  	  self.entrys.append(entry)

	  def delete():
	  	  for i in self.entrys:
	  	  	  i.destroy()


	  def highlight(self,ch1,ch2):
	  	  for i in self.entrys:
	  	  	  i.config(bg="red")
	  	  
	  	  self.entrys[ch1].config(bg="green")
	  	  self.entrys[ch2].config(bg="green")


	  def change(self,combo1,combo2):
	  	  self.entrys[combo1[0]].delete(0,END)
	  	  self.entrys[combo2[0]].delete(0,END)

	  	  self.entrys[combo1[0]].insert(0,combo2[1])
	  	  self.entrys[combo2[0]].insert(0,combo1[1])
	  	  

