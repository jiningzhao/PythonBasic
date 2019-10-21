from flask import Flask
from flask import render_template
from pymongo import MongoClient
app=Flask(__name__)
conn=MongoClient('127.0.0.1',27017)
db=conn.user
my_china=db.case_china
my_break=db.case_break
my_trend=db.case_trend
my_type=db.case_type
my_all=db.all
k1=[]
@app.route('/')
def printInfo1():
    for i in my_china.find({}, {'_id': 0}):  # 去掉id段
        k1.append(i)
    for i in my_break.find({}, {'_id': 0}):
        k1.append(i)
    for i in my_trend.find({}, {'_id': 0}):
        k1.append(i)
    for i in my_type.find({}, {'_id': 0}):
        k1.append(i)
    return render_template('index.html', data=k1)
@app.route('/_china')
def _china():
    for i in my_china.find({},{'_id':0}):              # 去掉id段
        return render_template('china.html', data=i)

@app.route('/_break')
def _break():
    for i in my_break.find({},{'_id':0}):
        return render_template('break.html', data=i)

@app.route('/_trend')
def _trend():
    for i in my_trend.find({},{'_id':0}):
        return render_template('trend.html', data=i)

@app.route('/_type')
def _type():
    for i in my_type.find({},{'_id':0}):
        return render_template('type.html', data=i)

k=[]
@app.route('/_all')
def printInfo():
    for i in my_china.find({}, {'_id': 0}):  # 去掉id段
        k.append(i)
    for i in my_break.find({}, {'_id': 0}):
        k.append(i)
    for i in my_trend.find({}, {'_id': 0}):
        k.append(i)
    for i in my_type.find({}, {'_id': 0}):
        k.append(i)
    return render_template('index.html', data=k)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000)


