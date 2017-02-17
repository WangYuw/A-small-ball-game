from tkinter import *
import random
import time

#create class Ball
class Ball:
    
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


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
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)       