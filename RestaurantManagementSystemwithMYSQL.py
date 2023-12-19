from tkinter import *
import mysql.connector

window = Tk()
window.title("restaurant management system")
window.geometry('1600x800')
#window.resizable(0,0)

TopFrame=Frame(window,bg="red",width=1600, height=50)
TopFrame.pack(side=TOP)
BottomFrame=Frame(window,bg="blue",width=1600, height=50)
BottomFrame.pack(side=BOTTOM)
RightFrame=Frame(window,bg="white",width=1000, height=700)
RightFrame.pack(side=RIGHT)
LeftFrame=Frame(window,width=1000, height=700)
LeftFrame.pack(side=LEFT)

Label(TopFrame,text='restaurant management system', font=('algerian',30,'bold')).grid(row=0,column=0)
Label(TopFrame,text ='navin', font=('algerian',30,'bold')).grid(row=1,column=0)
Label(BottomFrame,text ='Tambaram, chennai', font=('algerian',20,'bold'),bg='white',justify='right').grid(row=0,column=0)
Label(BottomFrame,text ='9348393857', font=('algerian',20,'bold'),bg='white',justify='right').grid(row=1,column=0)
text_input = StringVar()
ti = Entry(RightFrame, textvariable=text_input,insertwidth=7,bd=5,relief=SUNKEN,font=('arial',25))
ti.grid(columnspan=4) #justify='right'
operator= ''   # global variable works in function inside and outside
def buttonclick(num):
    global operator
    operator+=num  # x = x+num
    print(operator)
    text_input.set(operator)
def cleardisplay():
    global operator
    print('iam here')
    operator=''
    text_input.set('')
def calculation():
    global operator
    result = str(eval(operator))
    print(result)
    text_input.set(result)
    operator=''




Button(RightFrame,text=7,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('7')).grid(row=1,column=0)
Button(RightFrame,text=8,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('8')).grid(row=1,column=1)
Button(RightFrame,text=9,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('9')).grid(row=1,column=2)
Button(RightFrame,text='+',padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('+')).grid(row=1,column=3)

Button(RightFrame,text=4,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('4')).grid(row=2,column=0)
Button(RightFrame,text=5,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('5')).grid(row=2,column=1)
Button(RightFrame,text=6,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('6')).grid(row=2,column=2)
Button(RightFrame,text='-',padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('-')).grid(row=2,column=3)

Button(RightFrame,text=1,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('1')).grid(row=3,column=0)
Button(RightFrame,text=2,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('2')).grid(row=3,column=1)
Button(RightFrame,text=3,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('3')).grid(row=3,column=2)
Button(RightFrame,text='*',padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('*')).grid(row=3,column=3)

Button(RightFrame,text=0,padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('0')).grid(row=4,column=0)
Button(RightFrame,text='clear',padx=16,pady=4,font=('algerian',20,'bold'),command=cleardisplay).grid(row=4,column=1)
Button(RightFrame,text='=',padx=16,pady=4,font=('algerian',20,'bold'),command=calculation).grid(row=4,column=2)
Button(RightFrame,text='/',padx=16,pady=4,font=('algerian',20,'bold'),command=lambda :buttonclick('/')).grid(row=4,column=3)
x1=IntVar()
x1.set('')
Label(LeftFrame,text='OrderNo', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=0, column=0)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x1).grid(row=0,column=1)
x2=StringVar()
x2.set('')
Label(LeftFrame,text='OrderPerson', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=1, column=0)
Entry(LeftFrame,font=('algerian',15,'bold'),fg='green',textvariable=x2).grid(row=1,column=1)
x3=IntVar()
x3.set('')
Label(LeftFrame,text='Milkshake', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=2, column=0)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x3).grid(row=2,column=1)
x4=IntVar()
x4.set('')
Label(LeftFrame,text='Pizza', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=3, column=0)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x4).grid(row=3,column=1)

x5=IntVar()
x5.set('')
Label(LeftFrame,text='Burger', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=0, column=2)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x5).grid(row=0,column=3)
x6=IntVar()
x6.set('')
Label(LeftFrame,text='Sandwich', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=1, column=2)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x6).grid(row=1,column=3)
x7=IntVar()
x7.set('')
Label(LeftFrame,text='Tea', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=2, column=2)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x7).grid(row=2,column=3)
x8=IntVar()
x8.set('')
Label(LeftFrame,text='Coffee', font=('algerian',15,'bold'),fg='blue',pady=4).grid(row=3, column=2)
Entry(LeftFrame,font=('algerian',15,'bold'),textvariable=x8).grid(row=3,column=3)
def clear():
    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    x5.set('')
    x6.set('')
    x7.set('')
    x8.set('')

def priceList():
    price = Tk()
    price.title('pricelist menu')
    price.geometry('500x500')
    Label(price,text='item').grid(row=0,column=0)
    Label(price,text='price').grid(row=0,column=1)

    Label(price,text='milkshake').grid(row=1,column=0)
    Label(price,text='pizza').grid(row=2,column=0)
    Label(price,text='burger').grid(row=3,column=0)
    Label(price,text='sandwich').grid(row=4,column=0)
    Label(price,text='tea').grid(row=5,column=0)
    Label(price,text='coffee').grid(row=6,column=0)
    Label(price,text='50').grid(row=1,column=1)
    Label(price,text='200').grid(row=2,column=1)
    Label(price,text='80').grid(row=3,column=1)
    Label(price,text='50').grid(row=4,column=1)
    Label(price,text='20').grid(row=5,column=1)
    Label(price,text='20').grid(row=6,column=1)
    price.mainloop()
def close():
    window.destroy()
def bill():
    a=x1.get()
    b=x2.get()
    c=x3.get()
    d=x4.get()
    e=x5.get()
    f=x6.get()
    g=x7.get()
    h=x8.get()
    total=(c*50)+(d*200)+(e*80)+(f*50)+(g*20)+(h*20)
    service_charge = total*0.05
    gst =total*0.10
    billamount = int((total+service_charge+gst))
    print(a,b,c,d,e,f,g,h,service_charge,gst,billamount)

    connection = mysql.connector.connect(host='localhost', user='root', password='admin', database='abcd')
    cursor = connection.cursor()
    sql = f"insert into rest values({a},'{b}',{c},{d},{e},{f},{g},{h},{billamount})"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    window.destroy()

Button(LeftFrame,text='Exit', font=('algerian',15,'bold'),pady=2,command=close).grid(row=4,column=0)
Button(LeftFrame,text='Clear',font=('algerian',15,'bold'),pady=2,command=clear).grid(row=4,column=1)
Button(LeftFrame,text='PriceList',font=('algerian',15,'bold'),pady=2,command=priceList).grid(row=4,column=2)
Button(LeftFrame,text='bill',font=('algerian',15,'bold'),pady=2,command=bill).grid(row=4,column=3)
window.mainloop()