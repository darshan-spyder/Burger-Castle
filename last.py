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
##
ans=IntVar();
menuf3=Frame(root,height=618,width=1366)
c2=Canvas(menuf3,height=618,width=1366)
c2.pack()
logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c2.create_image(683,309,image=logo2)
c2.create_rectangle(100, 50, 600, 600,fill="white",outline="black",width=6)
sum1=Label(root,text="Total",font=("cooper black",22),bg="black",fg="white")
sum1.place(x=700,y=420)
sum2=Entry(root,bg="white",font=("cooper black",22),bd=5 ,justify='left',textvariable=ans)
sum2.place(x=850,y=420)
###1
##q12=StringVar()    
##meal1=PhotoImage(file="D:\\Study\\Semester 4\\food\\value_meal.png")
##c2.create_image(400,150,image=meal1)
##c2.create_text(650,100,text="Value Meal",fill="#000000",font=("Cooper Black",22))
##c2.create_text(875,100,text="₹144",fill="#ff3838",font=("default",17,'bold'))
##c2.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
##qty12=Entry(menuf3,textvariable=q12,bg="white",font=("default",12),width=4)
##qty12.place(x=650,y=140)
##add12=Button(menuf3,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
##add12.place(x=850,y=130)
###2
##q12=StringVar()    
##meal2=PhotoImage(file="D:\\Study\\Semester 4\\food\\happy_meal.png")
##c2.create_image(400,320,image=meal2)
##c2.create_text(650,270,text="Happy Meal",fill="#000000",font=("Cooper Black",22))
##c2.create_text(875,270,text="₹150",fill="#ff3838",font=("default",17,'bold'))
##c2.create_text(590,320,text="Quantity : ",fill="#000000",font=("default",12))
##qty12=Entry(menuf3,textvariable=q12,bg="white",font=("default",12),width=4)
##qty12.place(x=650,y=300)
##add12=Button(menuf3,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
##add12.place(x=850,y=300)
###3
##q12=StringVar()    
##meal=PhotoImage(file="D:\\Study\\Semester 4\\food\\fun_family_meal.png")
##c2.create_image(400,490,image=meal)
##c2.create_text(650,450,text="Fun family Meal",fill="#000000",font=("Cooper Black",22))
##c2.create_text(875,450,text="₹492",fill="#ff3838",font=("default",17,'bold'))
##c2.create_text(590,500,text="Quantity : ",fill="#000000",font=("default",12))
##qty12=Entry(menuf3,textvariable=q12,bg="white",font=("default",12),width=4)
##qty12.place(x=650,y=490)
##add12=Button(menuf3,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
##add12.place(x=850,y=480)
   

menuf3.pack(fill=BOTH,expand=0)
root.mainloop()

