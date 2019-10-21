# 求1~10的和
def CalcSum(s,n):                 # s表示前几个已经求完和的结果，n表示需要加的数字
    if n>10:
        return s
    return CalcSum(s+n,n+1)
sum1=CalcSum(0,1)
print(sum1)