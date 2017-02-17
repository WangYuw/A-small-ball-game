from tkinter import *
import random
import time

STEP = 3
#create class Ball
class Ball:
    
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # starts = [-3, -2, -1, 1, 2, 3]
        starts = [x-STEP for x in range(0, STEP*2+1) if x != STEP]
        random.shuffle(starts) # change order randomly
        self.x = starts[0]
        self.y = STEP
        self.canvas_height = self.canvas.winfo_height() # get the height of current window
        self.canvas_width = self.canvas.winfo_width() # get the width of current window

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # return coords(x,y) of the id object
        if pos[1] <= 0:
            self.y = STEP
        if pos[3] >= self.canvas_height:
            self.y = -STEP
        if pos[0] <= 0:
            self.x = STEP
        if pos[2] >= self.canvas_width:
            self.x = -STEP


# Create a canvas
tk = Tk()
tk.title("Game")
tk.resizable(0,0) # windows cannot be changed
tk.wm_attributes("-topmost",1) # windows on the top
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0) # no edge
canvas.pack()
tk.update() # preparer initialision

ball = Ball(canvas, 'red')
# main loop
while 1:
    ball.draw()
    tk.update_idletasks() # redraw the canvas
    tk.update()
    time.sleep(0.01)       