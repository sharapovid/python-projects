# by Sharapov Ilya
from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.a = 0
        self.points = 0
        self.text = canvas.create_text(420, 20, text='Your points: %s'% self.points, font=('Times', 15), fill='black')
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
       paddle_pos = self.canvas.coords(self.paddle.id)
       if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
       return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3 + self.a
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            time.sleep(0.5)
            self.canvas.create_rectangle(140, 230, 360, 170, fill='black', outline='grey')
            self.canvas.create_text(250, 200, text='GAME OVER', font=('Times', 25), fill='red')
        if self.hit_paddle(pos) == True:
            self.a = self.a + 0.1
            self.y = -3 - self.a
            self.points = self.points + 1
            self.canvas.itemconfig(self.text, text='Your points: %s'% self.points)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,
        fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.start_game)
        self.start_game = False

    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
    def start_game(self, evt):
        self.start_game = True
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0,
highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'red')
ball = Ball(canvas, paddle, 'gold')

while 1:
    if ball.hit_bottom == False and paddle.start_game == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)