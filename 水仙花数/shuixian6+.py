# https://baike.baidu.com/item/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0/2746160
# 五位水仙花数
# 个位：num%10
# 十位：num//10%10
# 百位: num//100%10
# 千位: num//1000%10
# 万位: num//10000%10

# 更多位数的权重都保存在 k 中，求和保存在 sum 中，n_sub 保存最初的n
# 注意，当 n>8 时，速度就很慢了。在n=3和n=8的时候出现了相邻两个数都是水仙花数
# n=3 153,370,371,407
# n=4 1634,8208,9474
# n=5 54748,92727,93084
# n=6 548834
# n=7 1741725,4210818,9800817,9926315
# n=8 24678050，24678051，88593477

import math
import time
n=int(input('请输入要求的水仙花数整数位数n：'))-1
time_start=time.time() # 开始计时
n_sub=n
k=[] # 生成k列表的时候，n发生了变化
while n>-1:
    k.append(int(math.pow(10,n)))
    #print(k)
    n-=1

n=n_sub
for i in range(int(pow(10,n)),int(pow(10,n+1))):
    sum=0
    m=n # m 做为索引比 n 小 1
    #print(i,m)
    while m>=0:
        sum += math.pow(i//k[m]%10,n+1) # m 索引比 n 小 1
            #print(k[m])
        m-=1
        #print(int(sum))
    if int(sum)==i:
        print(i)

# 结束计时
time_end=time.time()
time_cum=time_end-time_start
print(time_cum) # 输出程序运行时间