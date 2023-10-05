# 考拉兹猜想 lambda 方法
n=int(input("请输入一个正整数："))
lst=[]
lst.append(n)
fun=lambda x:(x//2 if x%2==0 else 3*x+1)
while lst[-1]!=1:
    lst.append(fun(lst[-1]))
print(lst)
