from flask import*
from crud_operation import *
app=Flask(__name__)

@app.route('/')

def openhomepage():
    return render_template('homepage.html')

@app.route('/addstudent')
def openstudentpageaddition():
    return render_template('addstudentpage.html')

@app.route('/readallstudent')
def displaystudentdetails():
    rows=readallstudent()
    return render_template('displaystudentpage.html',rows=rows)

@app.route("/savetotable",methods=["POST","GET"])
def savedetailstodp():
    if request.method=='POST':
        print("i am here")
        a=request.form["stname"]
        b=request.form['stlocation']
        c=int(request.form['stmark1'])
        d=int(request.form['stmark2'])
        e=int(request.form['stmark3'])
        print(a,b,c,d,e)
        insertstudent(a,b,c,d,e)
        message="record inserted"
    return render_template('success.html',mmm=message)

@app.route('/<id>/deletestudent')
def deletestudentrecord(id):
    ms=deletestudent(id)
    print(ms)
    return render_template('success.html',dele=ms)

@app.route('/<id>/editstudent')
def editstudentrecord(id):
    row=readperticularstudent(id)
    for a in row:
        print(a)
    return render_template('editstudent.html',row=row)

@app.route("/updatedatatotable",methods=["POST","GET"])
def updatedetails():
    if request.method=='POST':
        print("i am here")
        id=request.form["stid"]
        a=request.form["stname"]
        b=request.form['stlocation']
        c=int(request.form['stmark1'])
        d=int(request.form['stmark2'])
        e=int(request.form['stmark3'])
        print(a,b,c,d,e)
        updatestudent(id,stu_location=b,mark1=c,stu_name=a,mark2=d,mark3=e)
        msg="record updated"
    return render_template('success.html',mmm=msg)



if __name__=='__main__':
    app.run(debug=True,port=4589)