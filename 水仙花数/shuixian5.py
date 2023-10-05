# 五位水仙花数，没有五位数的水仙花数？
# 四位水仙花数
# 个位：num%10
# 十位：num//10%10
# 百位: num//100%10
# 千位: num//1000%10
# 万位: num//10000%10
import math
for i in range(10000,100000):
    #print(i//10000%10)
    
    if math.pow(i//10000%10,5)+math.pow(i//1000%10,5)+math.pow(i//100%10,5)+math.pow(i//10%10,5)+math.pow(i%10,5)==i:
        print(i)
    
