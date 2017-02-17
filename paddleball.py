from tkinter import *
import random
import time

STEP = 2
PA_STEP = 3
#create class Ball
class Ball:
    
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # starts = [-3, -2, -1, 1, 2, 3]
        starts = [x-STEP for x in range(0, STEP*2+1) if x != STEP]
        random.shuffle(starts) # change order randomly
        self.x = starts[0]
        self.y = STEP
        self.canvas_height = self.canvas.winfo_height() # get the height of current window
        self.canvas_width = self.canvas.winfo_width() # get the width of current window
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # return coords(x,y) of the id object
        if pos[1] <= 0:
            self.y = STEP
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -STEP # change direction
        if pos[0] <= 0:
            self.x = STEP
        if pos[2] >= self.canvas_width:
            self.x = -STEP

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

# create class Paddle
class Paddle:
    
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.start_game = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.click)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = PA_STEP
        elif pos[2] >= self.canvas_width:
            self.x = -PA_STEP


    def turn_left(self, evt):
        self.x = -PA_STEP

    def turn_right(self, evt):
        self.x = PA_STEP

    def click(self, evt):
        self.start_game = True

class Score:
   
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, fill=color)
        
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


tk = Tk()
tk.title("Game")
tk.resizable(0,0) # windows cannot be changed
tk.wm_attributes("-topmost",1) # windows on the top
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0) # no edge
canvas.pack()
tk.update() # preparer initialision

def re_start():
    canvas.delete("all")
    mainloop()

restart = Button(tk, text='restart', command=re_start).pack()
exit = Button(tk, text='exit', command=tk.destroy).pack()

def mainloop():
    # Create a canvas
    paddle = Paddle(canvas, 'blue')
    score = Score(canvas, 'green')
    ball = Ball(canvas, paddle, score, 'red')
    over_text = canvas.create_text(250, 200, text='GAME OVER!', state='hidden')
    # main loop
    while 1:    
        if ball.hit_bottom == False and paddle.start_game == True:
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            time.sleep(1)
            canvas.itemconfig(over_text, state='normal')
        tk.update_idletasks() # redraw the canvas
        tk.update()
        time.sleep(0.01) 


mainloop()


