#####学籍番号:1223033155
#####情報コース3年水越優友
#####波動方程式のプログラム

import numpy as np
import matplotlib.pyplot as plt

def Phi(x):
    return 2*x*(1-x)

N = 20  # 空間分割数
dx = 1 / N
dt = 1 / 50
c = 1  # 波の速度
r = c * dt / dx
M = 50  # 時間分割数
draw = [0, 10, 15, 20, 25, 30, 35, 40, 50]  # 描画ステップ

x = np.linspace(0, 1, N + 1)
U = Phi(x)
new_U = np.zeros(N + 1)
U_prev = Phi(x)  # 初期条件としてのU_prev

plt.figure(figsize=(8, 6))
plt.xlim([0, 1])
plt.ylim([-1, 1])
plt.gca().set_aspect('equal')

for n in range(M+1):
    if n in draw:
        plt.plot(x, U, 'o-', clip_on=False, markersize=3)
    for j in range(1, N):
        new_U[j] = 2*(1 - r**2)*U[j] - U_prev[j] + r**2*(U[j+1] + U[j-1])
    new_U[0] = 0  # 境界条件を適用
    new_U[N] = 0
    U_prev[:] = U[:]  # 現在の状態を前の状態として保存
    U[:] = new_U[:]  # 新しい状態を現在の状態として保存

plt.show()
