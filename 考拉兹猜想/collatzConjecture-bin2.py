# 考拉兹猜想 二进制实现方法，使用移位，然后加一，再加上自身，并判断是否2的整数次幂。
# 参考链接地址：
# https://www.ixigua.com/7145704388135223846?logTag=78df5ee1b0145db2f2cb


lst=[]
num=int(input('请输入需要计算的整数：')) # 数字27是第一个出现高峰的自然数
lst.append(str(bin(num))[2:])

while True:
    num=int(lst[-1],2)
    sum=int(bin(int(bin(num<<1),2)|1),2)+num
    while sum%2==0:
        sum=sum>>1
    binsum=bin(sum)
    n=len(binsum[2:])
    lst.append(binsum[2:])
    if int(binsum,2)==2**(n-1):
        break

print(lst)
print("一共经历了",len(lst),"步骤")