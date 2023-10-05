# 考拉兹猜想 二进制实现方法
# 参考链接地址：
# https://www.ixigua.com/7145704388135223846?logTag=78df5ee1b0145db2f2cb

def addbin(astr):
    astr=lst[-1]
    bstr=astr+'1' # 在二进制字符串末尾增加1
    cstr=int(astr,2)+int(bstr,2) # 将二进制数转变成10进制数，进行加法运算
    cstr=str(bin(cstr))[2:] # 将计算结果转变成二进制数，并转换成字符串
    return cstr

def removeZero(c): # 将最后一位 1 右侧的 0 全部移除
    cstr=str(c)
    while len(cstr)>1:
        if cstr[-1]=='0':
            cstr=cstr[:-1] # -1 为最后一位，但是从开始到-1，但不包含-1，也即舍去最后一位0
        else:
            break
    lst.append(cstr)
lst=[]
num=int(input('请输入需要计算的整数：')) # 数字27是第一个出现高峰的自然数
lst.append(str(bin(num))[2:])
while len(lst[-1])!=1:
    removeZero(addbin(lst[-1]))
print(lst)
print("一共经历了",len(lst),"步骤")