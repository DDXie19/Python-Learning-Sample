import matplotlib.pyplot as plt
from numpy import array, pi, exp, log

N = 12000
def f(n):
    return n/10 + n**2/7 + n**3/17 
# 10为年份，7为月份，17为日期
z = array( [exp( 2*pi*1j*f(n) ) for n in range(3, N+3)] )
z = z.cumsum()

plt.plot(z.real, z.imag, color='#333399')
#plt.axes().set_aspect(1) # 增加比例可能会出现图片显示问题
plt.show()