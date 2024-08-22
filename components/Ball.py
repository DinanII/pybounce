from random import randrange

class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 246, 100)
        self.x = randrange(-3, 4)  # Changed to range (-3, 4) to include 3
        self.y = -3
        self.hitBottom = False
        self.missedPaddle = False
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() 

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)  # x1, y1, x2, y2
        # Debugging prints
        print(f"Ball position: {pos}, Velocity: ({self.x}, {self.y})")

        # Bounce off the top and bottom edges
        if pos[1] <= 0:  # Top edge, y1
            self.y = abs(self.y)
            print('Ball reached top edge')
        if pos[3] >= self.canvas_height:  # Bottom edge, y2
            self.y = -abs(self.y)
            self.hitBottom = True
            print('Ball reached bottom edge')
        if pos[0] <= 0:  # Left edge, x1
            self.x = abs(self.x)
            print('Ball reached left edge')
        if pos[2] >= self.canvas_width:  # Right edge, x2
            self.x = -abs(self.x)
            print('Ball reached right edge')
        
        # Check collision with the paddle
        if self.hitPaddle(pos):
            self.y = -abs(self.y)
            print('Ball reached Paddle')
        if pos[3] > self.canvas.coords(self.paddle.id)[3]:  # Ball below the paddle
                self.missedPaddle = True
                self.hitBottom = True


    def hitPaddle(self, selfPos):
        paddlePos = self.canvas.coords(self.paddle.id)

        if selfPos[2] >= paddlePos[0] and selfPos[0] <= paddlePos[2]:
            if selfPos[3] >= paddlePos[1] and selfPos[1] <= paddlePos[3]:
                return True
        return False
