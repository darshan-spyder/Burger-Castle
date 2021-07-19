from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry("1500x800")

b = Button(root)
b.pack(fill = X, expand = True, ipady = 10)

# filename = PhotoImage(file = "D:\\Study\\Semester 4\\food\\sprite.jfif")
# background_label = Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
# img = ImageTk.PhotoImage(Image.open("ball.png"))
# canvas.create_image(20, 20, anchor=NW, image=img)
my=PhotoImage(file='D:\\Study\\Semester 4\\food\\extra.png')
canvas.create_image(0,0,anchor=NW,image=my)

b1 = Button(root, text = "Click me !")
b1.place(in_= b, relx = 0.45, rely = 0.5, anchor = CENTER)

b2 = Button(root, text = "Click me !")
b2.place(in_= b, relx = 0.55, rely = 0.5, anchor = CENTER)

root.mainloop()
