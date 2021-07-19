from tkinter import *
import time
root = Tk()
root.geometry("1370x800")

menuf2=Frame(root,height=150,width=1366)
c1=Canvas(menuf2,height=150,width=1366)
c1.pack()
logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
c1.create_image(683,75,image=logo1)
home1=Button(menuf2,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home1.place(x=1100,y=90)
localtime=time.asctime(time.localtime(time.time()))
c1.create_text(1100,50,text=localtime,fill="white",font=("default",16))
menuf2.pack(fill=BOTH,expand=0)

menuf3=Frame(root,height=618,width=1366)
c2=Canvas(menuf3,height=618,width=1366)
c2.pack()
logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c2.create_image(683,309,image=logo2)
c2.create_rectangle(100, 120, 1300, 450,fill="white",outline="white",width=6)
    
meal=PhotoImage(file="D:\\Study\\Semester 4\\food\\extra.png")
c2.create_image(230,250,image=meal)
meal1=Button(menuf3,text="Meal",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
meal1.place(x=190,y=390)
        
burger=PhotoImage(file="D:\\Study\\Semester 4\\food\\burger.png")
c2.create_image(530,250,image=burger)
burger1=Button(menuf3,text="Burgers",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
burger1.place(x=470,y=390)
    
fries=PhotoImage(file="D:\\Study\\Semester 4\\food\\fries_sides.png")
c2.create_image(830,250,image=fries)
fries1=Button(menuf3,text="Sides",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
fries1.place(x=790,y=390)
    
coke=PhotoImage(file="D:\\Study\\Semester 4\\food\\coke.png")
c2.create_image(1130,250,image=coke)
coke1=Button(menuf3,text="Beverages",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
coke1.place(x=1070,y=390)   

menuf3.pack(fill=BOTH,expand=0)
root.mainloop()


