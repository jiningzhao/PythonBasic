
import json
from pymongo import MongoClient
conn=MongoClient('127.0.0.1',27017)
db=conn.user
one=db.case_break
two=db.case_china
three=db.case_type
four=db.case_trend
one.remove()
two.remove()
three.remove()
four.remove()
def info():
    with open(r'E:\PYTHON代码练习\visualization\static\json\case_break.json','r') as f:
        one.insert(json.load(f,encoding='UTF-8'))
    with open(r'E:\PYTHON代码练习\visualization\static\json\case_china.json','r') as f1:
        two.insert(json.load(f1,encoding='UTF-8'))
    with open(r'E:\PYTHON代码练习\visualization\static\json\case_type.json','r') as f2:
        three.insert(json.load(f2,encoding='UTF-8'))
    with open(r'E:\PYTHON代码练习\visualization\static\json\case_trend.json','r') as f3:
        four.insert(json.load(f3,encoding='UTF-8'))

if __name__=='__main__':
    info()

