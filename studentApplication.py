from tkinter import*
import mysql.connector
from tkcalendar import DateEntry


def gender_selection():
    gender = gv.get()
    if gender == 1:
        return "male"
    else:
        return "female"


def country_selection():
    #x = cv.get()
    if cv.get() == 5:
        return "USA"
    elif cv.get() == 6:
        return "Russia"
    else:
        return "India"


def save_to_db():
    connection = mysql.connector.connect(host='localhost', user='root',
                                         password='admin', database='abcd')
    cursor = connection.cursor()
    a = idv.get()
    b = namev.get()
    c = sub1v.get()
    d = sub2v.get()
    e = sub3v.get()
    total = sub1v.get()+sub2v.get()+sub3v.get()
    avg = total / 3

    if total > 290:
        g = 'A grade'
    elif 275 <= total > 290:
        g = "B grade"
    elif 250 < total > 275:
        g = "C grade"
    elif 200 > total >= 250:
        g = "D grade"
    elif 105 <= total >= 200:
        g = "E grade"
    else:
        g = "F grade"
    # print(a,b,c,d,e,total,avg,g)
    ge = gender_selection()
    cty = country_selection()
    #de = degreeVar.get()
    de = y.get()
    ye = year_variable.get()
    c1 = check1.get()
    c2 = check2.get()
    c3 = check3.get()
    c4 = check4.get()
    ci = []
    if c1 == 1:
        ci.append('python')
    if c2 == 1:
        ci.append("java")
    if c3 == 1:
        ci.append('sql')
    if c4 == 1:
        ci.append('aws')
    CI = ','.join(ci)
    dj = doj.get_date()
    db = dob.get_date()

    sql = f"insert into student_example values({a},'{b}',{c},{d},{e},{total}," \
          f"{avg},'{g}','{ge}','{cty}','{de}','{ye}','{CI}','{dj}','{db}')"

    cursor.execute(sql)
    connection.commit()
    cursor.close()
    window.destroy()


window = Tk()
window.title("student application")
window.geometry("500x500")

Label(window,text="student_id").grid(row=0,column=0)
idv = IntVar()
idv.set("") # after submit integer entry box will be empty
Entry(window,textvariable=idv).grid(row=0,column=1)

Label(window,text="student_name").grid(row=1,column=0)
namev = StringVar()
Entry(window,textvariable=namev).grid(row=1,column=1)

Label(window,text="sub1").grid(row=2,column=0)
sub1v = IntVar()
sub1v.set('')
Entry(window,textvariable=sub1v).grid(row=2,column=1)

Label(window,text="sub2").grid(row=3,column=0)
sub2v = IntVar()
sub2v.set("")
Entry(window,textvariable=sub2v).grid(row=3,column=1)

Label(window,text="sub3").grid(row=4,column=0)
sub3v = IntVar()
sub3v.set("")
Entry(window,textvariable=sub3v).grid(row=4,column=1)

Label(window,text='gender',).grid(row=5,column=0)
gv = IntVar()
#gv.set('')
Radiobutton(window,text="male",value=1, variable=gv,
            command=gender_selection).grid(row=5,column=1)
Radiobutton(window,text="female",value=2, variable=gv,
            command=gender_selection).grid(row=5,column=2)

Label(window,text='country',).grid(row=6,column=0)
cv =IntVar()
Radiobutton(window,text='USA',variable=cv,value=5,command=country_selection).grid(row=6,column=1)
Radiobutton(window,text='Russia',variable=cv,value=6,command=country_selection).grid(row=6,column=2)
Radiobutton(window,text='India',variable=cv,value=7,command=country_selection).grid(row=6,column=3)

degree_completed = ["BE", 'MSC', "BA", 'B.COM', "MS"]
#degreeVar = StringVar(window)
y = StringVar(window)
Label(window,text='degree_selection',).grid(row=7,column=0)
#degreeVar.set("select an option")
y.set("select one")
OptionMenu(window, y, *degree_completed, ).grid(row=7,column=1)

year = ['2017', "2018", "2019", "2020", "2021", "2022", "2023"]
year_variable = StringVar(window)
Label(window,text="yop").grid(row=8,column=0)
year_variable.set("select year")
OptionMenu(window, year_variable, *year).grid(row=8,column=1)

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
Label(window,text='course_interested',).grid(row=9,column=0)
Checkbutton(window,text="Python",variable=check1,onvalue=1,offvalue=2).grid(row=9,column=1)
Checkbutton(window,text="Java",variable=check2,onvalue=1,offvalue=2).grid(row=9,column=2)
Checkbutton(window,text="SQL",variable=check3,onvalue=1,offvalue=2).grid(row=9,column=3)
Checkbutton(window,text="AWS",variable=check4,onvalue=1,offvalue=2).grid(row=9,column=4)

Label(window,text="date_of_joining").grid(row=10,column=0)
doj = DateEntry(window)
doj.grid(row=10,column=1)

Label(window,text="date_of_birth").grid(row=11,column=0)
dob = DateEntry(window)
dob.grid(row=11,column=1)


Button(window,text="submit", command=save_to_db).grid(row=12,column=1)#,columnspan=2)
# button place center of the column 1&2 use (columnspan=2)

window.mainloop()

