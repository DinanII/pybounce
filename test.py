from tkinter import *

tk = Tk()

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()

tk.geometry("%dx%d+0+0" % (w, h))


tk.mainloop()