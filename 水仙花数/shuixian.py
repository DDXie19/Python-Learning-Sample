# 
import math
import time
n=int(input('请输入要求的水仙花数整数位数n：'))
time_start=time.time() # 开始计时
lst=[]
i=0
while i<=9:
    lst.append(int(math.pow(i,n)))
    i+=1
#print(lst)

m=n # 暂时保留 n 的值
k=[] # 生成k列表【权重列表】的时候，n发生了变化
while n>0:
    n-=1
    k.append(int(math.pow(10,n)))
    #print(k)

n=m # 生成k列表的时候，n发生了变化，恢复 n 的值
ind=0 # 用于记录 lst 列表的下标或者索引
for i in range(int(pow(10,n-1)),int(pow(10,n))):
    m=n
    sum=0
    while m>0:
        ind=i//k[m-1]%10 # 每位数的索引
        #print(ind)
        sum+=lst[ind] # 将 lst 列表中对应的 lst[ind] 相加
        #print(sum)
        m-=1
    if sum==i:
        print(sum)
# 程序结束计时
time_end=time.time()
time_cum=time_end-time_start
print(time_cum) # 输出耗费时间