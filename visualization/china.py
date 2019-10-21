from flask import Flask, request, render_template
from pymongo import MongoClient
app=Flask(__name__)
conn=MongoClient('127.0.0.1',27017)
db=conn.user
my_china=db.case_china
my_break=db.case_break
my_trend=db.case_trend
my_type=db.case_type
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')
k=[]
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='china' and password=='111111':
        for i in my_china.find():
            return render_template('china.html',data=i)
    elif username=='break' and password=='222222':
        for i in my_break.find():
            return render_template('break.html',data=i)
    elif username=='type' and password=='333333':
        for i in my_type.find():
            return render_template('type.html',data=i)
    elif username=='trend' and password=='444444':
        for i in my_trend.find():
            return render_template('trend.html',data=i)
    elif username=='Echarts' and password=='000000':
        return render_template('Echarts.html')
    else:
        return render_template('form.html', message='Bad username or password', username=username)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8020)
