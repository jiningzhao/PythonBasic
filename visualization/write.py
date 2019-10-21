# from pymongo import MongoClient
# conn=MongoClient('127.0.0.1',27017)
# db=conn.user
# my_china=db.case_china
# my_break=db.case_break
# my_trend=db.case_trend
# my_type=db.case_type
from flask import render_template
from flask import Flask
app=Flask(__name__)
@app.route('/',methods=('GET','POST'))
def Echarts():
    return render_template('Echarts.html')
if __name__=='__main__':
    app.run(host='0.0.0.0',port=2020)
