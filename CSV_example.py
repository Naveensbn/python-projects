from tkinter import*
import random
import csv
import os
import os.path
import datetime as dt
from tkinter import colorchooser
c = dt.datetime.now()
print(c)
window = Tk()

window.geometry("1500x800")
# root.config(bg=colorchooser.askcolor()[1])
window.title("Restaurant Management System")
window.resizable(0,0)

Tops = Frame(window,width = 1600, height = 50)
Tops.pack(side = TOP)
Bottom = Frame(window,width = 1600, height = 50)
Bottom.pack(side = BOTTOM)

f1 = Frame(window, width = 900, height = 700)
f1.pack(side = LEFT)

f2 = Frame(window,width=400, height=700)
f2.pack(side = RIGHT)
Label(Tops,font=('aria',30,'bold'),text="Restaurant Management System", fg="steel blue", bd=10).grid(row=0,column=0)
Label(Tops,font=('aria',20,'bold'),text=c, fg="steel blue", bd=10).grid(row=1,column=0)
Label(Bottom,font=('aria',30,'bold'),text="Thank you, visit again", fg="dark blue", bd=10).grid(row=2,column=0)
Label(Bottom,font=('aria',20,'bold'),text="Welcome", fg="dark blue", bd=10).grid(row=3,column=0)

Username = StringVar()
Location = StringVar()
m1 = IntVar()
m2 = IntVar()
m3 = IntVar()
Label(f2,text = "Username").grid(row=0,column=0)
Entry(f2,textvariable=Username).grid(row=0, column=1)
Label(f2,text = "Location").grid(row=1,column=0)
Entry(f2,textvariable=Location).grid(row=1, column=1)
Label(f2,text = "m1").grid(row=2,column=0)
Entry(f2,textvariable=m1).grid(row=2, column=1)
Label(f2,text = "m2").grid(row=3,column=0)
Entry(f2,textvariable=m2).grid(row=3, column=1)
Label(f2,text = "m3").grid(row=4,column=0)
Entry(f2,textvariable=m3).grid(row=4, column=1)
m1.set('')
m2.set('')
m3.set('')
def Savetofile():
    nv = Username.get()
    lv = Location.get()
    a = m1.get()
    b = m2.get()
    c = m3.get()
    t = a+b+c
    av = t/3
    G = getgender()
    C = getcountry()
    Statesvalue = StatelistVar.get()
    c1 = Check1.get()
    c2 = Check2.get()
    c3 = Check3.get()
    o = []
    if c1 == 1:
        o.append('Python')
    if c2 == 1:
        o.append('SQL')
    if c3 == 1:
        o.append('Power BI')
    print(o)
    print(nv,lv,a,b,c,t,av, G, C, Statesvalue, o)
    if os.path.isfile('GUIoutput1.csv'):
        with open('GUIoutput1.csv', 'a', newline ="") as f:
            w = csv.writer(f)
            w.writerow([nv,lv,a,b,c,t,av, G, C, Statesvalue,o])
    else:
        with open('GUIoutput1.csv', 'a',newline="") as f:
            w = csv.writer(f)
            w.writerow(['Username', 'Location', 'mark1', 'mark2', 'mark3', 'total', 'avg', 'Gender','Country', 'State', 'Course interested'])
            w.writerow([nv,lv,a,b,c,t,av, G, C, Statesvalue, o])
    f2.destroy()   # right frame close
Label(f2, text = "Gender").grid(row = 5, column = 0)
Gv = IntVar()
def getgender():
    v = Gv.get()
    if v == 1:
        return "MALE"
    else:
        return "FEMALE"
Radiobutton(f2,text = "MALE", variable = Gv, value = 1, command = getgender).grid(row = 5, column = 1)
Radiobutton(f2,text = "FEMALE", variable = Gv, value = 2, command = getgender).grid(row = 5, column = 2)
Label(f2, text = "Country").grid(row = 6, column = 0)
Gvc = IntVar()
def getcountry():
    c = Gvc.get()
    if c == 1:
        return "INDIA"
    elif c == 2:
        return "AMERICA"
    else:
        return "AFRICA"
Radiobutton(f2,text = "INDIA", variable = Gvc, value = 1, command = getcountry).grid(row = 6, column = 1)
Radiobutton(f2,text = "AMERICA", variable = Gvc, value = 2, command = getcountry).grid(row = 6, column = 2)
Radiobutton(f2,text = "AFRICA", variable = Gvc, value = 3, command = getcountry).grid(row = 6, column = 3)
Statelist = ['Tamilnadu', 'Kerala', 'Karnataka','Andhrapradhesh', 'Rajasthan', 'Bihar', 'Punjab']
StatelistVar = StringVar(window)
StatelistVar.set("Select the option")
Label(f2,text = "State").grid(row = 7, column = 0)
OptionMenu(f2, StatelistVar, *Statelist).grid(row= 7, column=1)
Label(f2, text = "Course Interested").grid(row = 8, column=0)
Check1 = IntVar()
Check2 = IntVar()
Check3 = IntVar()
Checkbutton(f2, variable = Check1, text = "Python", onvalue=1, offvalue=0).grid(row = 8, column=1)
Checkbutton(f2, variable = Check2, text = "SQL", onvalue=1, offvalue=0).grid(row = 8, column=2)
Checkbutton(f2, variable = Check3, text = "Power BI", onvalue=1, offvalue=0).grid(row = 8, column=3)
Button(f2,text="Submit", command=Savetofile).grid(row=9,column=1)

rand = StringVar()
Fries = StringVar()
Lunch = StringVar()
Pizza = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10).grid(row=0,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand, bd=6,insertwidth=4,bg="powder blue" ).grid(row=0,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w').grid(row=1,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries, bd=6,insertwidth=4,bg="powder blue").grid(row=1,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w').grid(row=2,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lunch, bd=6,insertwidth=4,bg="powder blue").grid(row=2,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w').grid(row=3,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger, bd=6,insertwidth=4,bg="powder blue").grid(row=3,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w').grid(row=4,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pizza, bd=6,insertwidth=4,bg="powder blue").grid(row=4,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese Burger",fg="steel blue",bd=10,anchor='w').grid(row=5,column=0)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger, bd=6,insertwidth=4,bg="powder blue").grid(row=5,column=1)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w').grid(row=0,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks, bd=6,insertwidth=4,bg="powder blue").grid(row=0,column=3)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10,anchor='w').grid(row=1,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost, bd=6,insertwidth=4,bg="powder blue").grid(row=1,column=3)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w').grid(row=2,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_charge , bd=6,insertwidth=4,bg="powder blue").grid(row=2,column=3)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w').grid(row=3,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax, bd=6,insertwidth=4,bg="powder blue").grid(row=3,column=3)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w').grid(row=4,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal, bd=6,insertwidth=4,bg="powder blue").grid(row=4,column=3)
Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w').grid(row=5,column=2)
Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total, bd=6,insertwidth=4,bg="powder blue").grid(row=5,column=3)

def close():
    window.destroy()
def clear():
    rand.set('')
    Fries.set('')
    Lunch.set('')
    Burger.set('')
    Pizza.set('')
    Cheese_burger.set('')
    Drinks.set('')
    cost.set('')
    Service_charge.set('')
    Tax.set('')
    Subtotal.set('')
    Total.set('')

def price_list():
    roo = Tk()
    roo.geometry("600x800")
    roo.title("Price List")
    Label(roo, text = "Fries meal    :", font=( 'aria' ,16, 'bold' ),fg="steel blue",bd=10,anchor='w').grid(row=0, column=0)
    Label(roo, text= "   80", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=0,column=1)
    Label(roo, text="Lunch meal    :", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=1,column=0)
    Label(roo, text="   40", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=1, column=1)
    Label(roo, text="Burger meal    :", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=2,column=0)
    Label(roo, text="   35", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=2, column=1)
    Label(roo, text="Pizza meal    :", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=3,column=0)
    Label(roo, text="   45", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=3, column=1)
    Label(roo, text="Cheese_Burger Meal    :", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=4,column=0)
    Label(roo, text="   55", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=4, column=1)
    Label(roo, text="Drinks    :", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=5, column=0)
    Label(roo, text="   15", font=('aria', 16, 'bold'), fg="steel blue", bd=10, anchor='w').grid(row=5, column=1)

    roo.mainloop()
def Total_calculation():
    a = int(Fries.get())*80
    b = int(Lunch.get())*40
    c = int(Burger.get())*35
    d = int(Pizza.get())*45
    e = int(Cheese_burger.get())*55
    f = int(Drinks.get())*15
    t = a+b+c+d+e+f
    sc = t*0.10
    tx = t*0.05
    final_total = t+sc+tx
    s_total = t
    cost.set(t)
    Service_charge.set(sc)
    Tax.set(tx)
    Subtotal.set(s_total)
    Total.set(final_total)
    if os.path.isfile('GUIoutput2.csv'):
        with open('GUIoutput2.csv', 'a', newline ="") as f1:
            w = csv.writer(f1)
            w.writerow([a,b,c,d,e,f,t,sc,tx,s_total,final_total])
    else:
        with open('GUIoutput2.csv', 'a',newline="") as f1:
            w = csv.writer(f1)
            w.writerow(['Fries Meal', 'Lunch Meal', 'Burger Meal', 'Pizza Meal', 'Cheese_burger Meal', 'Drinks', 'Service_charge','Tax', 'Sub_Total', 'Total'])
            w.writerow([a,b,c,d,e,f,t,sc,tx,s_total,final_total])

Button(f1,text="PRICE",font=('ariel' ,16,'bold'),bd=6,bg="powder blue", command = price_list).grid(row=6,column=0)
Button(f1,text="TOTAL", font=('ariel' ,16,'bold'),bd=6,bg="powder blue", command = Total_calculation).grid(row=6,column=1)
Button(f1,text="RESET", font=('ariel' ,16,'bold'),bd=6,bg="powder blue", command = clear).grid(row=6,column=2)
Button(f1,text="EXIT", font=('ariel' ,16,'bold'), bd=6,bg="powder blue", command = close).grid(row=6,column=3)

window.mainloop()