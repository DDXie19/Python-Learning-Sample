import matplotlib.pyplot as plt
from numpy import array, pi, exp, log

N = 12000
def f(n):
    return log(n)**8
#根据给定的方程生成图形
z = array( [exp( 2*pi*1j*f(n) ) for n in range(3, N+3)] )
z = z.cumsum()

plt.plot(z.real, z.imag, color='#333399')
#plt.axes().set_aspect(1) # 增加比例可能会出现图片显示问题
plt.show()