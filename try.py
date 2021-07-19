from tkinter import *
import time

def six():
    try:
        root51.destroy()
        root56=Tk()
    except:
        try:
            root56=Tk()
        except:
            pass

##  root51.destroy()
##  root56 = Tk()
    root56.geometry("1370x800")

    menuf4=Frame(root56,height=150,width=1366)
    c3=Canvas(menuf4,height=150,width=1366)
    c3.pack()
    logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
    c3.create_image(683,75,image=logo1)
    home1=Button(menuf4,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
    home1.place(x=1100,y=90)
    localtime=time.asctime(time.localtime(time.time()))
    c3.create_text(1100,50,text=localtime,fill="white",font=("default",16))
    menuf4.pack(fill=BOTH,expand=0)
    ##
    menuf5=Frame(root56,height=618,width=1366)
    c4=Canvas(menuf5,height=618,width=1366)
    c4.pack()
    logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
    c4.create_image(683,309,image=logo2)
    c4.create_rectangle(300, 50, 1000, 600,fill="white",outline="black",width=6)
    #1
    q12=StringVar()    
    meal1=PhotoImage(file="D:\\Study\\Semester 4\\food\\value_meal.png")
    c4.create_image(400,150,image=meal1)
    c4.create_text(650,100,text="Value Meal",fill="#000000",font=("Cooper Black",22))
    c4.create_text(875,100,text="₹144",fill="#ff3838",font=("default",17,'bold'))
    c4.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
    qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
    qty12.place(x=650,y=140)
    add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
    add12.place(x=850,y=130)
    #2
    q12=StringVar()    
    meal2=PhotoImage(file="D:\\Study\\Semester 4\\food\\happy_meal.png")
    c4.create_image(400,320,image=meal2)
    c4.create_text(650,270,text="Happy Meal",fill="#000000",font=("Cooper Black",22))
    c4.create_text(875,270,text="₹150",fill="#ff3838",font=("default",17,'bold'))
    c4.create_text(590,320,text="Quantity : ",fill="#000000",font=("default",12))
    qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
    qty12.place(x=650,y=300)
    add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
    add12.place(x=850,y=300)
    #3
    q12=StringVar()    
    meal=PhotoImage(file="D:\\Study\\Semester 4\\food\\fun_family_meal.png")
    c4.create_image(400,490,image=meal)
    c4.create_text(650,450,text="Fun family Meal",fill="#000000",font=("Cooper Black",22))
    c4.create_text(875,450,text="₹492",fill="#ff3838",font=("default",17,'bold'))
    c4.create_text(590,500,text="Quantity : ",fill="#000000",font=("default",12))
    qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
    qty12.place(x=650,y=490)
    add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
    add12.place(x=850,y=480)

    add1=Button(root56,text="Add More",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'),command=lambda:five())
    add1.place(x=1100,y=390)
    confirm1=Button(root56,text="Confirm",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
    confirm1.place(x=1100,y=490)
   

    menuf5.pack(fill=BOTH,expand=0)
    root56.mainloop()

def five():
    try:
        root5.destroy()
        root51=Tk()
    except:
        try:
            root51=Tk()
        except:
            pass
##    root5.destroy()
##    root51 = Tk()
    root51.geometry("1370x800")

    menuf2=Frame(root51,height=150,width=1366)
    c1=Canvas(menuf2,height=150,width=1366)
    c1.pack()
    logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
    c1.create_image(683,75,image=logo1)
    home1=Button(menuf2,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
    home1.place(x=1100,y=90)
    localtime=time.asctime(time.localtime(time.time()))
    c1.create_text(1100,50,text=localtime,fill="white",font=("default",16))
    menuf2.pack(fill=BOTH,expand=0)

    menuf3=Frame(root51,height=618,width=1366)
    c2=Canvas(menuf3,height=618,width=1366)
    c2.pack()
    logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
    c2.create_image(683,309,image=logo2)
    c2.create_rectangle(100, 120, 1300, 450,fill="white",outline="white",width=6)
    
    meal=PhotoImage(file="D:\\Study\\Semester 4\\food\\extra.png")
    c2.create_image(230,250,image=meal)
    meal1=Button(menuf3,text="Meal",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'),command=lambda:six())
    meal1.place(x=170,y=390)
        
    burger=PhotoImage(file="D:\\Study\\Semester 4\\food\\burger.png")
    c2.create_image(530,250,image=burger)
    burger1=Button(menuf3,text="Burgers",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
    burger1.place(x=470,y=390)
    
    fries=PhotoImage(file="D:\\Study\\Semester 4\\food\\fries_sides.png")
    c2.create_image(830,250,image=fries)
    fries1=Button(menuf3,text="Sides",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
    fries1.place(x=770,y=390)
    
    coke=PhotoImage(file="D:\\Study\\Semester 4\\food\\coke.png")
    c2.create_image(1130,250,image=coke)
    coke1=Button(menuf3,text="Beverages",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
    coke1.place(x=1070,y=390)   

    menuf3.pack(fill=BOTH,expand=0)
    root51.mainloop()
    

    
try:
    root5=Tk()
except:
    pass
    

##root5 = Tk()

root5.geometry("1370x800")

menuf1=Frame(root5,height=150,width=1366)
c=Canvas(menuf1,height=150,width=1366)
c.pack()
logo=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
c.create_image(683,75,image=logo)
home=Button(menuf1,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home.place(x=1100,y=90)
localtime=time.asctime(time.localtime(time.time()))
c.create_text(1100,50,text=localtime,fill="white",font=("default",16))
menuf1.pack(fill=BOTH,expand=0)

menuf2=Frame(root5,height=618,width=1366)
c=Canvas(menuf2,height=618,width=1366)
c.pack()
logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c.create_image(683,309,image=logo1)
c.create_rectangle(350, 120, 1000, 450,fill="#EAECEE",outline="white",width=6)

pick=PhotoImage(file="D:\\Study\\Semester 4\\food\\pick.png")
c.create_image(530,250,image=pick)
pick1=Button(menuf2,text="Pick Up",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'),command=lambda:five())
pick1.place(x=470,y=390)

dev=PhotoImage(file="D:\\Study\\Semester 4\\food\\delivery.png")
c.create_image(830,250,image=dev)
dev1=Button(menuf2,text="Delivery",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'),command=lambda:five())
dev1.place(x=770,y=390)

menuf2.pack(fill=BOTH,expand=0)
root5.mainloop()



