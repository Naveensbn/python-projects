import mysql.connector



def insertstudent(*args):
    connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                         database='mywebsite')
    cursor = connection.cursor()
    sql=(f"insert into student_website(stu_name,stu_location,mark1,mark2,mark3)"
         f"values('{args[0]}','{args[1]}',{args[2]},{args[3]},{args[4]})")
    print(sql)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
#insertstudent('vijay','coimbatore',90,60,100)
def readallstudent():
    connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                         database='mywebsite')
    cursor = connection.cursor()
    sql='select * from student_website'
    cursor.execute(sql)
    rows=cursor.fetchall()
    #for a in cursor:
     #   print(a)
    return rows
readallstudent()
def readperticularstudent(*args):
    connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                         database='mywebsite')
    cursor = connection.cursor()
    sql=f"select * from student_website where stu_name='{args[0]}'"
    # sql=f"select * from student_website where stu_name='simbu'" #without args used


    cursor.execute(sql)
    rows=cursor.fetchall()
    return rows

# readperticularstudent(1)
# print(readallstudent())
def deletestudent(*args):
    connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                         database='mywebsite')
    cursor = connection.cursor()
    sql=f"delete from student_website where stu_id= {args[0]}"
    msg="student deleted"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    return msg
#deletestudent(2)
#readallstudent()
def updatestudent(*arg,**args):
#    statementfinal=""
    state=""

    for k,v in args.items():
        state+=k
        state+="="
        print(type(state))
        print(state)
        if isinstance(v,str):
            print('__________')
            state=state+"'"+v+"'"

        else:
            state=state+str(v)


        state+=","
    print(state)
    state=state.rstrip((state[-1]))   # strip means removes given args

    print(type(state))
    connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                         database='mywebsite')
    cursor = connection.cursor()
    sql=f"update student_website set {state} where stu_id={arg[0]}"
    #print(sql)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
# updatestudent(1,2,mark3=12,stu_name='kamal',stu_location='hosur',mark1=75)

# print(readallstudent())
r=readperticularstudent("simbu")
print(r)

print(readallstudent())

