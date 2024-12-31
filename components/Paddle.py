class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        
        # Bind keys for movement
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)  # x1, y1, x2, y2

        # Debugging prints
        #print(f"Paddle position: {pos}, Velocity: {self.x}")

        if pos[0] <= 0:  # Left edge, x1
            self.x = 0
            print('Paddle reached left edge')

        if pos[2] >= self.canvas_width:  # Right edge, x2
            self.x = 0
            print('Paddle reached right edge')

    def turnLeft(self, evt):
        self.x = -2

    def turnRight(self, evt):
        self.x = 2

    def stop(self, evt):
        self.x = 0
