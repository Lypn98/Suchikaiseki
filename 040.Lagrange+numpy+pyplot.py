#####学籍番号:1223033155
#####情報コース3年水越優友
#####ラグランジュ補間によるプログラム

import numpy as np
import matplotlib.pyplot as plt

###ラグランジュ補間関数
def Lagrange(px,py,x):
    N = len(px)
    y = 0.0
    for j in range(N):
        lj = np.prod([(x-px[i])/(px[j]-px[i])
                      for i in range(N) if i != j])
        y+= py[j]*lj

    return y

### 元の関数 y = 1 / (1 + 25x^2)
def function(x):
    return 1 / (1 + 25 * x**2)

###実行
px = np.array([0.2,0.6,0.8])
py = np.array([0.3,0.8,0.4])
M = 10

###グラフの描画
x_values = np.linspace(-1,1,M+1)
y_values = [Lagrange(px,py, x) for x in x_values]
original_y_values = [function(x) for x in x_values]

#plt.plot(x_values,y_values,'b-',label ='Interpolation')
plt.plot(x_values,original_y_values,'g--',label='y = 1 / (1 + 25x~2)')
#plt.scatter(px,py,color='red',label='Data points')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()