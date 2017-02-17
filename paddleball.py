from tkinter import *
import random
import time

# Create a canvas
tk=Tk()
tk.title("Game")
tk.resizable(0,0) # windows cannot be changed
tk.wm_attributes("-topmost",1) # windows on the top
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0) # no edge
canvas.pack()
tk.update() # preparer initialision

