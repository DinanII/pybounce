from random import randrange

class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,246,100)
        self.x = randrange(-3,3)
        self.y = -3
        self.hitBottom = False
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() 

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id) # x1,y1, x2, y2


        # Bounce off the top and bottom edge
        if(pos[1] <= 0): # Top edge, y1
            self.y = 3
        if(pos[3] >= self.canvas_height): # Bottom edge, y2
            self.y = -3
        if(pos[0] <= 0): # Left edge, x1
            self.x = 3
        if(pos[2] >= self.canvas_width): # Right edge, x2
            self.x = -3
        if(self.hitPaddle(pos)) == True:
            self.y = -3
        if(pos[3] >= self.canvas_height):
            self.hitBottom = True

    def hitPaddle(self,selfPos):
        paddlePos = self.canvas.coords(self.paddle.id)

        if(selfPos[2] >= paddlePos[0] and selfPos[0] <= paddlePos[2]):
            # If the right side of the ball (2,x2) is equal or bigger than the left side of the paddle (0,x1)
            # AND the left side of the ball (0,x1) is smaller than the right side of the paddle (2,x2) 
            if(selfPos[3] >= paddlePos[1] and selfPos[3] <= paddlePos[3]):
                return True
        return False

