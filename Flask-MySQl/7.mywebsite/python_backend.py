import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root',
                                     password='admin', database='mywebsite')
cursor = connection.cursor()
sql=("create table if not exists student_website(stu_id int primary key auto_increment,"
     "stu_name varchar(255),"
     "stu_location varchar(255),"
     "mark1 int,mark2 int,mark3 int,"
     "total int generated always as (mark1+mark2+mark3),"
     "average decimal(5,2) generated always as(total/3),"
     "grade varchar(255) generated always as"
     "(case when total>290 then 'gradeA' "
     "      when total<=290 and total>=250 then 'gradeB' "
     "      when total<250 and total>=200 then 'gradeC' "
     "      else 'gradeD'"
     "end)stored)"
     )
print(sql)
cursor.execute(sql)
connection.commit()
cursor.close()