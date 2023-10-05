# 考拉兹猜想（Collatz Conjecture），也叫奇偶归一猜想、3n + 1猜想、冰雹猜想、角骨猜想、哈塞猜想、乌拉姆猜想、叙拉古猜想
# 算法介绍：
# 对于每一个正整数，如果他是奇数，就对他乘以3，再加1，如果是偶数则对他除以2，最终都能得到1

def collatz_conjecture(number):
    while number !=1:
        if number%2==0:
            # 偶数
            number/=2
            print(number)
        elif number%2==1:
            # 奇数
            number=3*number+1
            print(number)

collatz_conjecture(27)