from tkinter import *
import time
import sqlite3
import random
import datetime

root1 = Tk()
root1.geometry("1570x825")

def Ref():

    if (q1.get()==""):
        Coq1=0
    else:
        Coq1=float(q1.get())


    
    if (q2.get()==""):
        Coq2=0
    else:
        Coq2=float(q2.get())



    if (q3.get()==""):
        Coq3=0
    else:
        Coq3=float(q3.get())



    if (q4.get()==""):
        Coq4=0
    else:
        Coq4=float(q4.get())

        
    if (q5.get()==""):
        Coq5=0
    else:
        Coq5=float(q5.get())

     
    if (q6.get()==""):
        Coq6=0
    else:
        Coq7=float(q6.get())

    if (q7.get()==""):
        Coq7=0
    else:
        Coq7=float(q7.get())


    
    if (q8.get()==""):
        Coq8=0
    else:
        Coq8=float(q8.get())



    if (q9.get()==""):
        Coq9=0
    else:
        Coq9=float(q9.get())



    if (q10.get()==""):
        Coq10=0
    else:
        Coq10=float(q10.get())

        
    if (q11.get()==""):
        Coq11=0
    else:
        Coq11=float(q11.get())

     
    if (q12.get()==""):
        Coq12=0
    else:
        Coq12=float(q12.get())
        

    if (q13.get()==""):
        Coq13=0
    else:
        Coq13=float(q13.get())

     
    if (q14.get()==""):
        Coq14=0
    else:
        Coq14=float(q14.get())
                   
    costofq1 =Coq1 * 144
    costofq2 = Coq2 * 150
    costofq3 = Coq3 * 492
    costofq4 = Coq4 * 49
    costofq5=Coq5 * 74
    costofq6=Coq6 * 109
    costofq7 =Coq7 * 204
    costofq8 = Coq8 * 47
    costofq9 = Coq9 * 60
    costofq10 = Coq10 * 128
    costofq11=Coq11 * 79
    costofq12=Coq12 * 79
    costofq13=Coq13 * 151
    costofq14=Coq14 * 170

    CostofMeal= str('%.2f' % (costofq1+costofq2+costofq3+costofq4+costofq5+costofq6+costofq7+costofq8+costofq9+costofq10+costofq11+costofq12+costofq13+costofq14))

    PayTax=((costofq1+costofq2+costofq3+costofq4+costofq5+costofq6+costofq7+costofq8+costofq9+costofq10+costofq11+costofq12+costofq13+costofq14) * 0.2)

    TotalCost=(costofq1+costofq2+costofq3+costofq4+costofq5+costofq6+costofq7+costofq8+costofq9+costofq10+costofq11+costofq12+costofq13+costofq14)
 
    Ser_Charge= ((costofq1+costofq2+costofq3+costofq4+costofq5+costofq6+costofq7+costofq8+costofq9+costofq10+costofq11+costofq12+costofq13+costofq14)/99)

    Service = str ('%.2f' % Ser_Charge)

    OverAllCost = str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)
    
def qExit():
    root1.destroy()


def Submit():
    db = sqlite3.connect('items.db')
    cursor = db.cursor()
    cursor.execute("insert into DATA values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(q1.get(), q2.get(), q3.get(), q4.get(), q5.get(),q6.get(),q7.get(), q8.get(), q9.get(), q10.get(), q11.get(),q12.get(), q13.get(),q14.get() ,Tax.get(), Cost.get(), Total.get(), Service_Charge.get()))
    cursor.close()
    db.commit()
    db.close()
    

def Reset(): 
    q1.set("")
    q2.set("")
    q3.set("")
    q4.set("")
    q5.set("")
    q6.set("")
    q7.set("")
    q8.set("")
    q9.set("")
    q10.set("")
    q11.set("")
    q12.set("")
    q13.set("")
    q14.set("")
    Tax.set("")
    Cost.set("")
    Total.set("")
    Service_Charge.set("")


#######database#########
db = sqlite3.connect('items.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DATA
    (
      rand TEXT,
      q1 TEXT,
      q2 TEXT,
      q3 TEXT,
      q4 TEXT,
      q5 TEXT,
      q6 TEXT,
      q7 TEXT,
      q8 TEXT,
      q9 TEXT,
      q10 TEXT,
      q11 TEXT,
      q12 TEXT,
      q13 TEXT,
      q14 TEXT,
      Total TEXT,
      Service_Charge TEXT,
      Tax TEXT,
      Cost TEXT
    )''')
cursor.close()
db.commit()
db.close()
########################field###############

menuf4=Frame(root1,height=150,width=1570)
c1=Canvas(menuf4,height=150,width=1570)
c1.pack()
logo1=PhotoImage(file="D:\\Study\\Semester 4\\food\\title.png")
c1.create_image(780,75,image=logo1)
home1=Button(menuf4,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home1.place(x=1100,y=90)
localtime=time.asctime(time.localtime(time.time()))
c1.create_text(1100,50,text=localtime,fill="white",font=("default",16))
menuf4.pack(fill=BOTH,expand=0)
##
menuf5=Frame(root1,height=825,width=1570)
c2=Canvas(menuf5,height=825,width=1570)
c2.pack()
logo2=PhotoImage(file="D:\\Study\\Semester 4\\food\\bg.png")
c2.create_image(650,400,image=logo2)
#1
c2.create_rectangle(5, 5, 150, 340,fill="white",outline="black",width=4)
q1=StringVar()    
meal1=PhotoImage(file="D:\\Study\\Semester 4\\food\\value_meal.png")
c2.create_image(70,60,image=meal1)
c2.create_text(70,140,text="Value",fill="#000000",font=("Cooper Black",22))
c2.create_text(70,170,text="Meal",fill="#000000",font=("Cooper Black",22))
c2.create_text(73,280,text="₹144",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(50,230,text="Quantity : ",fill="#000000",font=("default",12))
qty1=Entry(menuf5,textvariable=q1,bg="white",font=("default",12),width=4)
qty1.place(x=80,y=220)

#2
c2.create_rectangle(150, 5, 300, 340,fill="white",outline="black",width=4)
q2=StringVar()    
meal2=PhotoImage(file="D:\\Study\\Semester 4\\food\\happy_meal.png")
c2.create_image(230,60,image=meal2)
c2.create_text(220,140,text="Happy",fill="#000000",font=("Cooper Black",22))
c2.create_text(220,170,text="Meal",fill="#000000",font=("Cooper Black",22))
c2.create_text(223,280,text="₹150",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(200,230,text="Quantity : ",fill="#000000",font=("default",12))
qty2=Entry(menuf5,textvariable=q2,bg="white",font=("default",12),width=4)
qty2.place(x=230,y=220)

#3
c2.create_rectangle(300, 5, 450, 340,fill="white",outline="black",width=4)
q3=StringVar()    
meal3=PhotoImage(file="D:\\Study\\Semester 4\\food\\fun_family_meal.png")
c2.create_image(380,60,image=meal3)
c2.create_text(375,140,text="Fun Family",fill="#000000",font=("Cooper Black",18))
c2.create_text(370,170,text="Meal",fill="#000000",font=("Cooper Black",18))
c2.create_text(373,280,text="₹492",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(350,230,text="Quantity : ",fill="#000000",font=("default",12))
qty3=Entry(menuf5,textvariable=q3,bg="white",font=("default",12),width=4)
qty3.place(x=380,y=220)

#4
c2.create_rectangle(450, 5, 600, 340,fill="white",outline="black",width=4)
q4=StringVar()    
meal4=PhotoImage(file="D:\\Study\\Semester 4\\food\\mac_allo_burger.png")
c2.create_image(530,60,image=meal4)
c2.create_text(525,140,text="Allo Tikki",fill="#000000",font=("Cooper Black",18))
c2.create_text(520,170,text="Burger",fill="#000000",font=("Cooper Black",18))
c2.create_text(523,280,text="₹49",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(500,230,text="Quantity : ",fill="#000000",font=("default",12))
qty4=Entry(menuf5,textvariable=q4,bg="white",font=("default",12),width=4)
qty4.place(x=530,y=220)

#5
c2.create_rectangle(600, 5, 750, 340,fill="white",outline="black",width=4)
q5=StringVar()    
meal5=PhotoImage(file="D:\\Study\\Semester 4\\food\\mac_allo_double_burger.png")
c2.create_image(680,70,image=meal5)
c2.create_text(675,140,text="Allo Tikki",fill="#000000",font=("Cooper Black",18))
c2.create_text(675,170,text="Double Petty",fill="#000000",font=("Cooper Black",16))
c2.create_text(675,200,text="Burger",fill="#000000",font=("Cooper Black",18))
c2.create_text(673,280,text="₹74",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(650,230,text="Quantity : ",fill="#000000",font=("default",12))
qty5=Entry(menuf5,textvariable=q5,bg="white",font=("default",12),width=4)
qty5.place(x=680,y=220)

#6
c2.create_rectangle(750, 5, 900, 340,fill="white",outline="black",width=4)
q6=StringVar()    
meal6=PhotoImage(file="D:\\Study\\Semester 4\\food\\veggie_burger.png")
c2.create_image(830,60,image=meal6)
c2.create_text(825,140,text="Veggie",fill="#000000",font=("Cooper Black",18))
c2.create_text(820,170,text="Burger",fill="#000000",font=("Cooper Black",18))
c2.create_text(823,280,text="₹109",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(800,230,text="Quantity : ",fill="#000000",font=("default",12))
qty6=Entry(menuf5,textvariable=q6,bg="white",font=("default",12),width=4)
qty6.place(x=830,y=220)

#7
c2.create_rectangle(900, 5, 1050, 340,fill="white",outline="black",width=4)
q7=StringVar()    
meal7=PhotoImage(file="D:\\Study\\Semester 4\\food\\mac_maharaja_burger.png")
c2.create_image(980,60,image=meal7)
c2.create_text(975,140,text="Veg",fill="#000000",font=("Cooper Black",18))
c2.create_text(970,170,text="Maharaja",fill="#000000",font=("Cooper Black",18))
c2.create_text(973,280,text="₹204",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(950,230,text="Quantity : ",fill="#000000",font=("default",12))
qty7=Entry(menuf5,textvariable=q7,bg="white",font=("default",12),width=4)
qty7.place(x=980,y=220)

#8
c2.create_rectangle(5, 340, 150, 670,fill="white",outline="black",width=4)
q8=StringVar()    
meal8=PhotoImage(file="D:\\Study\\Semester 4\\food\\masala_wedges_sides.png")
c2.create_image(80,400,image=meal8)
c2.create_text(70,480,text="Masala",fill="#000000",font=("Cooper Black",22))
c2.create_text(70,510,text="Wedges",fill="#000000",font=("Cooper Black",22))
c2.create_text(73,620,text="₹47",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(50,570,text="Quantity : ",fill="#000000",font=("default",12))
qty8=Entry(menuf5,textvariable=q8,bg="white",font=("default",12),width=4)
qty8.place(x=80,y=560)

#9
c2.create_rectangle(150, 340, 300, 670,fill="white",outline="black",width=4)
q9=StringVar()    
meal9=PhotoImage(file="D:\\Study\\Semester 4\\food\\fries_sides.png")
c2.create_image(230,400,image=meal9)
c2.create_text(220,480,text="Franch",fill="#000000",font=("Cooper Black",22))
c2.create_text(220,510,text="Fries",fill="#000000",font=("Cooper Black",22))
c2.create_text(223,620,text="₹60",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(200,570,text="Quantity : ",fill="#000000",font=("default",12))
qty9=Entry(menuf5,textvariable=q9,bg="white",font=("default",12),width=4)
qty9.place(x=230,y=560)

#10
c2.create_rectangle(300, 340, 450, 670,fill="white",outline="black",width=4)
q10=StringVar()    
meal10=PhotoImage(file="D:\\Study\\Semester 4\\food\\maxican_chessy_fries_sides.png")
c2.create_image(380,400,image=meal10)
c2.create_text(375,480,text="Maxican",fill="#000000",font=("Cooper Black",18))
c2.create_text(370,510,text="Cheesy Fries",fill="#000000",font=("Cooper Black",16))
c2.create_text(373,620,text="₹128",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(350,570,text="Quantity : ",fill="#000000",font=("default",12))
qty10=Entry(menuf5,textvariable=q10,bg="white",font=("default",12),width=4)
qty10.place(x=380,y=560)

#11
c2.create_rectangle(450, 340, 600, 670,fill="white",outline="black",width=4)
q11=StringVar()    
meal11=PhotoImage(file="D:\\Study\\Semester 4\\food\\coke.png")
c2.create_image(530,400,image=meal11)
c2.create_text(520,510,text="coke",fill="#000000",font=("Cooper Black",18))
c2.create_text(523,620,text="₹79s",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(500,570,text="Quantity : ",fill="#000000",font=("default",12))
qty11=Entry(menuf5,textvariable=q11,bg="white",font=("default",12),width=4)
qty11.place(x=530,y=560)

#12
c2.create_rectangle(600, 340, 750, 670,fill="white",outline="black",width=4)
q12=StringVar()    
meal12=PhotoImage(file="D:\\Study\\Semester 4\\food\\ice_tea.png")
c2.create_image(680,400,image=meal12)
c2.create_text(675,510,text="Ice Tea",fill="#000000",font=("Cooper Black",18))
c2.create_text(673,620,text="₹79",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(650,570,text="Quantity : ",fill="#000000",font=("default",12))
qty12=Entry(menuf5,textvariable=q12,bg="white",font=("default",12),width=4)
qty12.place(x=680,y=560)

#13
c2.create_rectangle(750, 340, 900, 670,fill="white",outline="black",width=4)
q13=StringVar()    
meal13=PhotoImage(file="D:\\Study\\Semester 4\\food\\stawbarry_shake.png")
c2.create_image(830,400,image=meal13)
c2.create_text(820,480,text="Stawbarry",fill="#000000",font=("Cooper Black",18))
c2.create_text(820,510,text="Shake",fill="#000000",font=("Cooper Black",18))
c2.create_text(823,620,text="₹151",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(800,570,text="Quantity : ",fill="#000000",font=("default",12))
qty13=Entry(menuf5,textvariable=q13,bg="white",font=("default",12),width=4)
qty13.place(x=830,y=560)

#14
c2.create_rectangle(900, 340, 1050, 670,fill="white",outline="black",width=4)
q14=StringVar()    
meal14=PhotoImage(file="D:\\Study\\Semester 4\\food\\mango_smoothi.png")
c2.create_image(980,400,image=meal14)
c2.create_text(975,480,text="Mango",fill="#000000",font=("Cooper Black",18))
c2.create_text(970,510,text="Smoothie",fill="#000000",font=("Cooper Black",18))
c2.create_text(973,620,text="₹170",fill="#ff3838",font=("default",17,'bold'))
c2.create_text(950,570,text="Quantity : ",fill="#000000",font=("default",12))
qty14=Entry(menuf5,textvariable=q14,bg="white",font=("default",12),width=4)
qty14.place(x=980,y=560)

c2.create_rectangle(1080, 15, 1420, 470,fill="white",outline="black",width=4)

#########total###########
#cost
Cost=StringVar()
lblCost= Label(menuf5, font=('arial', 19, 'bold'),text="Cost of Meal",bd=16,anchor="w",bg="white",fg="black")
lblCost.place(x=1100,y=20)
txtCost=Entry(menuf5, font=('arial',19,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="white",fg="black")
txtCost.place(x=1100,y=70)
#service
Service_Charge=StringVar()
lblService= Label(menuf5, font=('arial', 19, 'bold'),text="Service Charge",bd=16,anchor="w",bg="white")
lblService.place(x=1100,y=130)
txtService=Entry(menuf5, font=('arial',19,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="white",fg="black")
txtService.place(x=1100,y=180)
#state tax
Tax=StringVar()
lblStateTax= Label(menuf5, font=('arial', 19, 'bold'),text="State Tax",bd=16,anchor="w",bg="white")
lblStateTax.place(x=1100,y=240)
txtStateTax=Entry(menuf5, font=('arial',19,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="white",fg="black")
txtStateTax.place(x=1100,y=290)
#total cost
Total=StringVar()
lblTotalCost= Label(menuf5, font=('arial', 19, 'bold'),text="Total Cost",bd=16,anchor="w",bg="white")
lblTotalCost.place(x=1100,y=340)
txtTotalCost=Entry(menuf5, font=('arial',19,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="white",fg="black")
txtTotalCost.place(x=1100,y=390)
#########Button###########

confirm1=Button(root1,text="Total",padx=12,pady=5,bd=10,bg="#0b1335",cursor="hand2",fg="white",font=("default",16,'bold'),command=Ref)
confirm1.place(x=1100,y=650)

total1=Button(root1,text="Submit",padx=12,pady=5,bd=10,bg="#0b1335",cursor="hand2",fg="white",font=("default",16,'bold'),command=Submit)
total1.place(x=1280,y=650)

reset1=Button(root1,text="Reset",padx=12,pady=5,bd=10,bg="#0b1335",cursor="hand2",fg="white",font=("default",16,'bold'),command=Reset)
reset1.place(x=1100,y=750)

exit1=Button(root1,text="Exit",padx=12,pady=5,bd=10,bg="#0b1335",cursor="hand2",fg="white",font=("default",16,'bold'),command=qExit)
exit1.place(x=1280,y=750)
   

menuf5.pack(fill=BOTH,expand=0)
root1.mainloop()


