# 蒙特卡罗法对圆周率进行推算
# 蒙特卡罗法是指使用随机数对某种值进行估算的方法。由于使用了随机数，所以有时会输出正确的答案，与之相反，有时会输出不那么令人满意的结果。

import matplotlib.pyplot as plt
import numpy as np
import math
import time
#%matplotlib inline

np.random.seed(100)

X=0 # 满足条件的次数

# 请设置尝试执行的次数 N
N=2000
# 绘制四分之一圆的边界方程 [y=\sqrt{(1-x^2)} (0<=x<=1)]

circle_x=np.arange(0,1,0.001)
circle_y=np.sqrt(1-circle_x*circle_x)
plt.figure(figsize=(15,15))
plt.plot(circle_x,circle_y)

# 统计执行N次所花费的时间
start_time=time.time()

# 执行N次
for i in range(0,N):
    # 请在0到1之间生成均匀分布的随机数，并将其保存到变量score_x 中
    score_x=np.random.rand()
    # 请在0到1之间生成均匀分布的随机数，并将其保存到变量score_y 中
    score_y=np.random.rand()
    # 请对进入圆圈中的点和没有进入圆圈的点进行条件分支处理
    if score_x*score_x+score_y*score_y<1:
        # 请将进入圆圈中的点用黑色显示，没有进入圆圈中的点用蓝色显示
        plt.scatter(score_x,score_y,marker="o",color="k")
        # 如果点进入了圆圈中，请在上面定义的变量X中加上1个点
        X+=1
    else:
        plt.scatter(score_x,score_y,marker="o",color="b")

# 请在此处计算pi 的近似值
pi=4*float(X)/float(N)

# 请计算蒙特卡罗法的执行时间
end_time=time.time()
time=end_time-start_time

# 请显示圆周率的计算结果
print("执行时间:%f"%(time))

# 显示结果
print("圆周率:%.6f"%pi)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()