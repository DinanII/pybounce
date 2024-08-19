from tkinter import *
import random
import time
from Ball import Ball
from Paddle import Paddle

tk = Tk()

tk.title = 'Bounce'
tk.resizable(0,0) # Window is not resizable (vertically and horizontally)
tk.wm_attributes("-topmost",1) # Places the canvas window before every other window
canvas = Canvas(tk, width=500,height=400,bd=0,highlightthickness=0) # bd = border, so in tghis case, there's no border, there's also a thickness defined
canvas.pack() # initializes the window based on the earlier given params
tk.update() # Tkinter initializes itself for an animation.


paddle = Paddle(canvas,'blue')
ball = Ball(canvas,'red',paddle)
while True:
    if(ball.hitBottom == False):
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
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