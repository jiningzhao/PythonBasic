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
    if username=='admin' and password=='123456':
        for i in my_china.find({},{'_id':0}):              # 去掉id段
            k.append(i)
        for i in my_break.find({},{'_id':0}):
            k.append(i)
        for i in my_trend.find({},{'_id':0}):
            k.append(i)
        for i in my_type.find({},{'_id':0}):
            k.append(i)
        return render_template('index.html', data=k)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)