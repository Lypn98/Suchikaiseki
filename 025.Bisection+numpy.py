#####学籍番号:1223033155
#####情報コース3年水越優友
#####二分法のプログラム

import numpy as np

#関数 
def f(x):
    return np.exp(-x)-x*x

#初期化
a = 1
b = 0
 #収束判定値
eps = 1.0e-6
 #反復回数
n = 0 

#反復
while True:
    c = (a+b)/2
    n += 1
    print(f"{n:2d}{c:.7f}")

    if np.abs(a-b)/2 < eps:
        break
    fc = f(c)

    if fc > 0:
        b = c
    elif fc < 0:
        a = c
    else:
        break

print("|nc =",c)
