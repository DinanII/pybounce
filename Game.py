from tkinter import *
import time
from components import Ball, Paddle

class Game:

    def __init__(self, wTitle='BounceGame'):

        # Window initialization
        self.tk = Tk()
        self.tk.title(wTitle) 
        #self.tk.resizable(0,0)  # Window is not resizable (vertically and horizontally)
        self.tk.wm_attributes('-topmost',1)
        w = self.tk.winfo_screenwidth() * 0.10
        h = self.tk.winfo_screenheight() * 0.30
        self.tk.geometry("%dx%d+0+0" % (w, h))
    
        # Canvas drawing
        self.canvas = Canvas(self.tk, width=w, height=h, bd=0, highlightthickness=0)
        self.canvas.pack()
        
        # Windows and Gameloop n
        self.tk.update()  # Initialize Tkinter for animation

        # Game components initialization
        self.paddle = Paddle(self.canvas, 'blue')
        self.ball = Ball(self.canvas, 'red', self.paddle)

        self.gameLoop()
    
    def gameLoop(self):
        while True:
            if not self.ball.hitBottom:
                self.ball.draw()
                self.paddle.draw()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

# Ideas for update
# Highscores
# Only move the pan-thing for a bit when the player presses the arrow key
# Ball moves quicker as time progresses
# Scoring system
# High scores
# Post game screen where player can choose whether fullscreen should be enabled, maybe highscores overview, ask player for it's name
# Main menu for game itself
# Calculate element sizes on basis of canvas size, so it doesn't looks scuffed on fullscreen for example.
# A JSON or some other config to mutate game
#   Ball speed
#   Pad color
#   background (maybe parallax effect?!??!?!)