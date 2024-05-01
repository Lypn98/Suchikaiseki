#####学籍番号:1223033155
#####情報コース3年水越優友
#####ニュートン法のプログラム

import numpy as np

#関数
def f(x):
    return np.exp(-x)-x*x
def g(x):
    return -np.exp(-x)-2*x

#初期値の設定
x = 1
eps = 1.0e-6
n = 0

#反復
while True:
    print(f"{n:2d} {x:.15f}")
    new_x = x - f(x)/g(x)
    n+=1

    if np.abs(new_x - x) < eps* np.abs(new_x):
        break
    x = new_x

#終了
print(f"{n:2d} {new_x:.15f}")