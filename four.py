from tkinter import *
import time

root = Tk()

root.geometry("1370x800")

menuf1=Frame(root,height=150,width=1366)
c=Canvas(menuf1,height=150,width=1366)
c.pack()
logo=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
c.create_image(683,75,image=logo)
home=Button(menuf1,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home.place(x=1100,y=90)
localtime=time.asctime(time.localtime(time.time()))
c.create_text(1100,50,text=localtime,fill="white",font=("default",16))
menuf1.pack(fill=BOTH,expand=0)

menuf2=Frame(root,height=618,width=1366)
c=Canvas(menuf2,height=618,width=1366)
c.pack()
logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c.create_image(683,309,image=logo1)
c.create_rectangle(350, 120, 1000, 450,fill="#EAECEE",outline="white",width=6)

pick=PhotoImage(file="D:\\Study\\Semester 4\\food\\pick.png")
c.create_image(530,250,image=pick)
pick1=Button(menuf2,text="Pick Up",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
pick1.place(x=470,y=390)

dev=PhotoImage(file="D:\\Study\\Semester 4\\food\\delivery.png")
c.create_image(830,250,image=dev)
dev1=Button(menuf2,text="Delivery",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
dev1.place(x=770,y=390)

menuf2.pack(fill=BOTH,expand=0)
root.mainloop()


