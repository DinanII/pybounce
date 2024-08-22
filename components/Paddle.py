class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turnLeft)
        self.canvas.bind_all('<KeyPress-Right>',self.turnRight)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id) # x1,y1, x2, y2
        if(pos[0] <= 0): # Left edge, x1
            self.x = 3
        if(pos[2] >= self.canvas_width): # Right edge, x2
            self.x = -3

    def turnLeft(self,evt):
        self.x = -2

    def turnRight(self, evt):
        self.x = 2
