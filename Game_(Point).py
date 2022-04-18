# by Sharapov Ilya
from tkinter import *
import random

root = Tk()
root["bg"] = "black"
root.title("point")
root.geometry("1000x500")
canvas = Canvas(root, width=1000, height=500, bd=0,
highlightthickness=0, bg="black")	
canvas.pack()


class Сircle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_oval(10, 10, 60, 60,
		fill=color)
		self.canvas.move(self.id, 500, 250)
		self.canvas.tag_bind(self.id, '<Button-1>', self.moving)
		self.points = 0
		self.text = canvas.create_text(500, 20, text='%s '% self.points, 
			font=('Times', 20), fill='White')

	def moving(self, canvas):
		self.x = random.randint(50, 950)
		self.y = random.randint(50, 450)
		self.canvas.coords(self.id, self.x, self.y, 
			self.x + 50, self.y + 50)	
		self.points = self.points + 1	
		self.canvas.itemconfig(self.text, text='%s'% self.points)

circle = Сircle(canvas, 'red')
root.mainloop()