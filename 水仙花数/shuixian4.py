# 四位水仙花数
# 个位：num%10
# 十位：num//10%10
# 百位: num//100%10
# 千位: num//1000%10
import math
'''
for i in range(1000,10000):
    #print(i//1000%10)
    if math.pow(i//1000,4)+math.pow(i//100%10,4)+math.pow(i//10%10,4)+math.pow(i//1000%10,4)==i:
        print(i)
    
'''
# 为何两段程序的结果不同？

for i in range(1000,10000):
    if math.pow(i//1000%10,4)+math.pow(i//100%10,4)+math.pow(i//10%10,4)+math.pow(i%10,4)==i:
        print(i)