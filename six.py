from tkinter import *
import time
root6 = Tk()
root6.geometry("1370x800")

menuf4=Frame(root6,height=150,width=1366)
c1=Canvas(menuf4,height=150,width=1366)
c1.pack()
logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
c1.create_image(683,75,image=logo1)
home1=Button(menuf4,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home1.place(x=1100,y=90)
localtime=time.asctime(time.localtime(time.time()))
c1.create_text(1100,50,text=localtime,fill="white",font=("default",16))
menuf4.pack(fill=BOTH,expand=0)
##
menuf5=Frame(root6,height=618,width=1366)
c2=Canvas(menuf5,height=618,width=1366)
c2.pack()
logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c2.create_image(683,309,image=logo2)
c2.create_rectangle(300, 50, 1000, 600,fill="white",outline="black",width=6)
#1
q12=StringVar()    
meal1=PhotoImage(file="D:\\Study\\Semester 4\\food\\value_meal.png")
c2.create_image(400,150,image=meal1)
c2.create_text(650,100,text="Value Meal",fill="#000000",font=("Cooper Black",22))
c2.create_text(875,100,text="₹144",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
qty12.place(x=650,y=140)
add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
add12.place(x=850,y=130)
#2
q12=StringVar()    
meal2=PhotoImage(file="D:\\Study\\Semester 4\\food\\happy_meal.png")
c2.create_image(400,320,image=meal2)
c2.create_text(650,270,text="Happy Meal",fill="#000000",font=("Cooper Black",22))
c2.create_text(875,270,text="₹150",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(590,320,text="Quantity : ",fill="#000000",font=("default",12))
qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
qty12.place(x=650,y=300)
add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
add12.place(x=850,y=300)
#3
q12=StringVar()    
meal=PhotoImage(file="D:\\Study\\Semester 4\\food\\fun_family_meal.png")
c2.create_image(400,490,image=meal)
c2.create_text(650,450,text="Fun family Meal",fill="#000000",font=("Cooper Black",22))
c2.create_text(875,450,text="₹492",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(590,500,text="Quantity : ",fill="#000000",font=("default",12))
qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
qty12.place(x=650,y=490)
add12=Button(menuf5,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",12,'bold'))
add12.place(x=850,y=480)

add1=Button(root6,text="Add More",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
add1.place(x=1100,y=390)
confirm1=Button(root6,text="Confirm",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
confirm1.place(x=1100,y=490)
   

menuf5.pack(fill=BOTH,expand=0)
root6.mainloop()


